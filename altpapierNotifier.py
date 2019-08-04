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

for userDataSet in userDataSets:
  disposals = [wasteDisposal("paper", str(userDataSet.zipCode)), wasteDisposal("cardboard", str(userDataSet.zipCode))]
  for disposal in disposals:
      if disposal.GetNextDisposalDate() == date.today() and datetime.now().hour < 12:
        bot.SendMessage(userDataSet.chatId, disposal.GetName() + " disposal is today!")
      elif (disposal.GetNextDisposalDate() - timedelta(days=1)).date() == date.today() and datetime.now().hour > 12:
        bot.SendMessage(userDataSet.chatId, disposal.GetName() + " disposal will be tomorrow!")   
