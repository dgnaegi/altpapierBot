from datetime import datetime
from telegram import base
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
      bot.SendMessage(userDataSet.chatId, "Cardboard and paper disposal will be tomorrow!")
    if userDataSet.areaCode in todayDisposalAreaCodes and datetime.now().hour < 12:
      bot.SendMessage(userDataSet.chatId, text="Cardboard and paper disposal is today!") 
  except:
    logf.write("An exception occurred for basel area code: " + str(userDataSet.areaCode) + "\r\n")
