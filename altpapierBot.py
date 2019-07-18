import telegram
from datetime import datetime
from datetime import date
from datetime import timedelta
from helper.wasteDisposal import wasteDisposal
import json

zip = "doNotCommit"
chatId = doNotCommit
bot = telegram.Bot(token='doNotCommit')

disposals = [wasteDisposal("paper", zip), wasteDisposal("cardboard", zip)]

for disposal in disposals:
    if disposal.GetNextDisposalDate() == date.today() and datetime.now().hour < 12:
      print(disposal.GetName + "disposal is today!")
    if (disposal.GetNextDisposalDate() - timedelta(days=1)).date() == date.today() and datetime.now().hour > 12:
      print (disposal.GetName + "disposal will be tomorrow!")   
