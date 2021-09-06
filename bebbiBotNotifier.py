from datetime import datetime
from helper.baselApi import baselApi
from dataStorage.dataAccessBasel import dataAccess
from helper.bot import bot
import json

with open('config.json') as data_file:    
    data = json.load(data_file)
    token = data["bebbiToken"]
    
logf = open("error.log", "w")
bot = bot(token)

userDataSets = dataAccess.getUserData()

tomorrowDisposalAreaCodes = baselApi.GetTomorrowDisposalAreaCodes()
todayDisposalAreaCodes = baselApi.GetTodayDisposalAreaCodes()

for userDataSet in userDataSets:
  try:    
    if userDataSet.areaCode in tomorrowDisposalAreaCodes and datetime.now().hour > 12:
      bot.SendMessage(userDataSet.chatId, "Morn isch Karton- und Papierentsorgig!")
    if userDataSet.areaCode in todayDisposalAreaCodes and datetime.now().hour < 12:
      bot.SendMessage(userDataSet.chatId, text="Hüt isch Karton- und Papierentsorgig!") 
  except:
    logf.write("An exception occurred for basel area code: " + str(userDataSet.areaCode) + "\r\n")
