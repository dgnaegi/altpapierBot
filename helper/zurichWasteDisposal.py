from datetime import datetime
from datetime import date
from datetime import timedelta
from urllib.request import urlopen
import json

class zurichWasteDisposal:
    def __init__(self, name, zip):
        self.name = name
        self.zip = zip
        currentDate = date.today()
        currentDateAsString = currentDate.strftime("%Y-%m-%d")
        self.url = "http://openerz.metaodi.ch/api/calendar/" + name + ".json?zip=" + zip + "&start=" + currentDateAsString + "&sort=date&offset=0&limit=1"
        
    def GetNextDisposalDate(self):
        return datetime.strptime(json.load(urlopen(self.url))['result'][0]['date'], "%Y-%m-%d")

    def GetName(self):
        return self.name

    def DisposalIsToday(self):
        return datetime.strptime(GetNextDisposalDate(), "%Y-%m-%d").date() == currentDate

    def DisposalIsTomorrow(self):
        return (datetime.strptime(GetNextDisposalDate(), "%Y-%m-%d") - timedelta(days=1)).date() == currentDate
