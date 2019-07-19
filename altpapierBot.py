from datetime import datetime
from datetime import date
from datetime import timedelta
from helper.wasteDisposal import wasteDisposal
from helper.bot import bot
import json

with open('config.json') as data_file:    
    data = json.load(data_file)
    zip = data["zip"]
    chatId = data["chatId"]
    token = data["token"]

bot = bot(token)
disposals = [wasteDisposal("paper", zip), wasteDisposal("cardboard", zip)]

for disposal in disposals:
    if disposal.GetNextDisposalDate() == date.today() and datetime.now().hour < 12:
      bot.SendMessage(chatId, disposal.GetName + "disposal is today!")
    if (disposal.GetNextDisposalDate() - timedelta(days=1)).date() == date.today() and datetime.now().hour > 12:
      bot.SendMessage(chatId, disposal.GetName + "disposal will be tomorrow!")   