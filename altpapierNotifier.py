from datetime import datetime
from datetime import date
from datetime import timedelta
from helper.zurichWasteDisposal import zurichWasteDisposal
from helper.stgallenApi import stgallenApi
from dataStorage.dataAccess import dataAccess
from helper.bot import bot
import json

with open('config.json') as data_file:    
    data = json.load(data_file)
    token = data["token"]

bot = bot(token)

zhUserDataSets = dataAccess.getZurichUserdata()
logf = open("error.log", "w")
sentMessageZurich = 0
for userDataSet in zhUserDataSets:
  disposals = [zurichWasteDisposal("paper", str(userDataSet.zipCode)), zurichWasteDisposal("cardboard", str(userDataSet.zipCode))]
  for disposal in disposals:
    try:  
      if disposal.GetNextDisposalDate().date() == date.today() and datetime.now().hour < 12:
        bot.SendMessage(userDataSet.chatId, disposal.GetName() + " disposal is today!")
        sentMessageZurich = sentMessageZurich + 1
      elif (disposal.GetNextDisposalDate() - timedelta(days=1)).date() == date.today() and datetime.now().hour > 12:
        bot.SendMessage(userDataSet.chatId, disposal.GetName() + " disposal will be tomorrow!")
        sentMessageZurich = sentMessageZurich + 1
    except:
      logf.write("An exception occurred for ZIP: " + str(userDataSet.zipCode) + "\r\n")

sgUserDataSets = dataAccess.getStGallenUserdata()

tomorrowPaperDisposalAreaCodes = stgallenApi.GetTomorrowPaperDisposalAreaCodes()
todayPaperDisposalAreaCodes = stgallenApi.GetTodayPaperDisposalAreaCodes()

tomorrowCardboardDisposalAreaCodes = stgallenApi.GetTomorrowCardboardDisposalAreaCodes()
todayCardboardDisposalAreaCodes = stgallenApi.GetTodayCardboardDisposalAreaCodes()

sentMessageStGallen = 0
for userDataSet in sgUserDataSets:
  if userDataSet.areaCode in tomorrowPaperDisposalAreaCodes and datetime.now().hour > 12:
    bot.SendMessage(userDataSet.chatId, "Paper disposal will be tomorrow!")
    sentMessageStGallen = sentMessageStGallen + 1
  if userDataSet.areaCode in todayPaperDisposalAreaCodes and datetime.now().hour < 12:
    bot.SendMessage(userDataSet.chatId, "Paper disposal is today!") 
    sentMessageStGallen = sentMessageStGallen + 1
  if userDataSet.areaCode in tomorrowCardboardDisposalAreaCodes and datetime.now().hour > 12:
    bot.SendMessage(userDataSet.chatId, "Cardboard disposal will be tomorrow!")
    sentMessageStGallen = sentMessageStGallen + 1
  if userDataSet.areaCode in todayCardboardDisposalAreaCodes and datetime.now().hour < 12:
    bot.SendMessage(userDataSet.chatId, "Cardboard disposal is today!") 
    sentMessageStGallen = sentMessageStGallen + 1

sendLog = open("send.log", "w")
sendLog.write("Sent messages Zurich: " + str(sentMessageZurich) + "\r\n")
sendLog.write("Sent messages St.Gallen: " + str(sentMessageStGallen) + "\r\n")
