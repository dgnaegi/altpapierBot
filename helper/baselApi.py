from datetime import datetime
from datetime import date
from datetime import timedelta
from urllib.request import urlopen
import json

class baselApi:
    @staticmethod
    def GetTomorrowDisposalAreaCodes():
        requestedDate = str((datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
        url = "https://data.bs.ch/api/records/1.0/search/?dataset=100096&q=termin%3A[" + requestedDate + "+TO+" + requestedDate + "]&sort=termin&facet=termin&facet=wochentag&facet=art&facet=zone&facet=dayofweek&refine.art=Papierabfuhr"
        records = json.load(urlopen(url))['records']
        areaCodes =[]
        for record in records:
            areaCodes.append(record['fields']['zone'].upper())
            
        return areaCodes

    @staticmethod
    def GetTodayDisposalAreaCodes():
        requestedDate = str((datetime.now()).strftime('%Y-%m-%d'))
        url = "https://data.bs.ch/api/records/1.0/search/?dataset=100096&q=termin%3A[" + requestedDate + "+TO+" + requestedDate + "]&sort=termin&facet=termin&facet=wochentag&facet=art&facet=zone&facet=dayofweek&refine.art=Papierabfuhr"
        records = json.load(urlopen(url))['records']

        areaCodes =[]
        for record in records:
            areaCodes.append(record['fields']['zone'].upper())
        
        return areaCodes