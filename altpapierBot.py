import telegram
from datetime import datetime
from datetime import date
from datetime import timedelta
from urllib.request import urlopen
import json

bot = telegram.Bot(token='doNotCommitTokens')

currentDate = date.today()
currentDateAsString = currentDate.strftime("%Y-%m-%d")

zip = "yourZip"

nextPaperDate = json.load(urlopen("http://openerz.metaodi.ch/api/calendar/paper.json?zip=" + zip + "&start=" + currentDateAsString + "&sort=date&offset=0&limit=1"))['result'][0]['date']
nextCardboard = json.load(urlopen("http://openerz.metaodi.ch/api/calendar/cardboard.json?zip=" + zip + "&start=" + currentDateAsString + "&offset=0&limit=1"))['result'][0]['date']

cardboardToday = datetime.strptime(nextCardboard, "%Y-%m-%d").date() == currentDate
paperToday = datetime.strptime(nextPaperDate, "%Y-%m-%d").date() == currentDate
cardboardTomorrow = (datetime.strptime(nextCardboard, "%Y-%m-%d") - timedelta(days=1)).date() == currentDate
paperTomorrow = (datetime.strptime(nextPaperDate, "%Y-%m-%d") - timedelta(days=1)).date() == currentDate

chatId = doNotCommitChatIds

if cardboardToday and datetime.now().hour < 12:
  bot.sendMessage(chatId, "Hüt isch imfall Karton!")

if paperToday and datetime.now().hour < 12:
  bot.sendMessage(chatId, "Hüt isch imfall Papier!")

if cardboardTomorrow and datetime.now().hour > 12:
  bot.sendMessage(chatId, "Morn isch imfall Karton!")

if paperTomorrow and datetime.now().hour > 12:
  bot.sendMessage(chatId, "Morn isch imfall Papier!")
