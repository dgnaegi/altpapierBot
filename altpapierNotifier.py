from datetime import datetime
from datetime import date
from datetime import timedelta
from helper.zurichApi import zurichApi
from helper.stgallenApi import stgallenApi
from dataStorage.dataAccess import dataAccess
from helper.bot import bot
import json

with open('config.json') as data_file:    
    data = json.load(data_file)
    token = data["token"]

bot = bot(token)
logf = open("error.log", "w")

zhUserDataSets = dataAccess.getZurichUserdata()

tomorrowZHPaperDisposalZipCodes = zurichApi.GetTomorrowPaperDisposalZipCodes()
todayZHPaperDisposalZipCodes = zurichApi.GetTodayPaperDisposalZipCodes()

tomorrowZHCardboardDisposalZipCodes = zurichApi.GetTomorrowCardboardDisposalZips()
todayCardboardZHDisposalZipCodes = zurichApi.GetTodayPaperDisposalZipCodes()

sentMessageZurich = 0

for userDataSet in zhUserDataSets:
  if userDataSet.zipCode in tomorrowZHPaperDisposalZipCodes and datetime.now().hour > 12:
    bot.SendMessage(userDataSet.chatId, "Paper disposal will be tomorrow!")
    sentMessageZurich = sentMessageZurich + 1
  if userDataSet.zipCode in todayZHPaperDisposalZipCodes and datetime.now().hour < 12:
    bot.SendMessage(userDataSet.chatId, "Paper disposal is today!") 
    sentMessageZurich = sentMessageZurich + 1
  if userDataSet.zipCode in tomorrowZHCardboardDisposalZipCodes and datetime.now().hour > 12:
    bot.SendMessage(userDataSet.chatId, "Cardboard disposal will be tomorrow!")
    sentMessageZurich = sentMessageZurich + 1
  if userDataSet.zipCode in todayCardboardZHDisposalZipCodes and datetime.now().hour < 12:
    bot.SendMessage(userDataSet.chatId, "Cardboard disposal is today!") 
    sentMessageZurich = sentMessageZurich + 1

sgUserDataSets = dataAccess.getStGallenUserdata()

tomorrowSGPaperDisposalAreaCodes = stgallenApi.GetTomorrowPaperDisposalAreaCodes()
todaySGPaperDisposalAreaCodes = stgallenApi.GetTodayPaperDisposalAreaCodes()

tomorrowSGCardboardDisposalAreaCodes = stgallenApi.GetTomorrowCardboardDisposalAreaCodes()
todaySGCardboardDisposalAreaCodes = stgallenApi.GetTodayCardboardDisposalAreaCodes()

sentMessageStGallen = 0

for userDataSet in sgUserDataSets:
  if userDataSet.areaCode in tomorrowSGPaperDisposalAreaCodes and datetime.now().hour > 12:
    bot.SendMessage(userDataSet.chatId, "Paper disposal will be tomorrow!")
    sentMessageStGallen = sentMessageStGallen + 1
  if userDataSet.areaCode in todaySGPaperDisposalAreaCodes and datetime.now().hour < 12:
    bot.SendMessage(userDataSet.chatId, "Paper disposal is today!") 
    sentMessageStGallen = sentMessageStGallen + 1
  if userDataSet.areaCode in tomorrowSGCardboardDisposalAreaCodes and datetime.now().hour > 12:
    bot.SendMessage(userDataSet.chatId, "Cardboard disposal will be tomorrow!")
    sentMessageStGallen = sentMessageStGallen + 1
  if userDataSet.areaCode in todaySGCardboardDisposalAreaCodes and datetime.now().hour < 12:
    bot.SendMessage(userDataSet.chatId, "Cardboard disposal is today!") 
    sentMessageStGallen = sentMessageStGallen + 1

sendLog = open("send.log", "w")
sendLog.write("Sent messages Zurich: " + str(sentMessageZurich) + "\r\n")
sendLog.write("Sent messages St.Gallen: " + str(sentMessageStGallen) + "\r\n")
