from dataStorage.dataAccess import dataAccess
from helper.bot import bot
import json

with open('config.json') as data_file:    
    data = json.load(data_file)
    token = data["token"]

bot = bot(token)

zhUserDataSets = dataAccess.getZurichUserdata()

for userDataSet in zhUserDataSets:
  try:
    bot.SendMessage(userDataSet.chatId, "Unfortunately, due to a technical problem, no notifications have been sent for the past two weeks. The problem has been fixed in the meantime. My creator is working on a solution so that such issues will be detected earlier. For updates about altpapierBot you can follow him on Twitter: https://twitter.com/dgnaegi")
    bot.SendMessage(userDataSet.chatId, "PS: Tell your friends about me (and that you love them)")
  except:
    continue
