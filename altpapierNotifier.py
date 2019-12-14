from datetime import datetime
from datetime import date
from datetime import timedelta
from helper.wasteDisposal import wasteDisposal
from dataStorage.dataAccess import dataAccess
from helper.bot import bot
import json

with open('config.json') as data_file:    
    data = json.load(data_file)
    token = data["token"]

bot = bot(token)

userDataSets = dataAccess.getAllUserdata()
logf = open("error.log", "w")
for userDataSet in userDataSets:
  disposals = [wasteDisposal("paper", str(userDataSet.zipCode)), wasteDisposal("cardboard", str(userDataSet.zipCode))]
  for disposal in disposals:
    try:  
      if disposal.GetNextDisposalDate().date() == date.today() and datetime.now().hour < 12:
        bot.SendMessage(userDataSet.chatId, disposal.GetName() + " disposal is today!")
      elif (disposal.GetNextDisposalDate() - timedelta(days=1)).date() == date.today() and datetime.now().hour > 12:
        bot.SendMessage(userDataSet.chatId, disposal.GetName() + " disposal will be tomorrow!")  
    except:
      logf.write("An exception occurred for ZIP: " + str(userDataSet.zipCode) + "\r\n")
     
