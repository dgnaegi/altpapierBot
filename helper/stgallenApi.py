from datetime import datetime
from datetime import date
from datetime import timedelta
from urllib.request import urlopen
import json

class stgallenApi:
    def GetTomorrowPaperDisposalAreaCodes():
        requestedDate = str((datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
        url = "https://daten.stadt.sg.ch/api/records/1.0/search/?dataset=abfuhrdaten-stadt-stgallen&q=&rows=100&sort=-datum&facet=gebiets_id&facet=datum&refine.sammlung=Papier&refine.datum=" + "2020-07-01"

        records = json.load(urlopen(url))['records']
        areaCodes =[]
        for record in records:
            areaCodes.append(record['fields']['gebiets_id'].upper())
    
        return areaCodes

    def GetTodayPaperDisposalAreaCodes():
        requestedDate = str((datetime.now()).strftime('%Y-%m-%d'))
        url = "https://daten.stadt.sg.ch/api/records/1.0/search/?dataset=abfuhrdaten-stadt-stgallen&q=&rows=100&sort=-datum&facet=gebiets_id&facet=datum&refine.sammlung=Papier&refine.datum=" + requestedDate

        records = json.load(urlopen(url))['records']
        areaCodes =[]
        for record in records:
            areaCodes.append(record['fields']['gebiets_id'].upper())
    
        return areaCodes




