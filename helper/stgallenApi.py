from datetime import datetime
from datetime import date
from datetime import timedelta
from urllib.request import urlopen
import json

class stgallenApi:
    @staticmethod
    def GetTomorrowPaperDisposalAreaCodes():
        requestedDate = str((datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
        url = "https://daten.stadt.sg.ch/api/records/1.0/search/?dataset=abfuhrdaten-stadt-stgallen&q=&rows=100&sort=-datum&facet=gebiets_id&facet=datum&refine.sammlung=Papier&refine.datum=" + requestedDate

        records = json.load(urlopen(url))['records']
        areaCodes =[]
        for record in records:
            areaCodes.append(record['fields']['gebiets_id'].upper())
    
        return areaCodes

    @staticmethod
    def GetTodayPaperDisposalAreaCodes():
        requestedDate = str((datetime.now()).strftime('%Y-%m-%d'))
        url = "https://daten.stadt.sg.ch/api/records/1.0/search/?dataset=abfuhrdaten-stadt-stgallen&q=&rows=100&sort=-datum&facet=gebiets_id&facet=datum&refine.sammlung=Papier&refine.datum=" + requestedDate

        records = json.load(urlopen(url))['records']
        areaCodes =[]
        for record in records:
            areaCodes.append(record['fields']['gebiets_id'].upper())
    
        return areaCodes

    @staticmethod
    def GetTomorrowCardboardDisposalAreaCodes():
        requestedDate = str((datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
        url = "https://daten.stadt.sg.ch/api/records/1.0/search/?dataset=abfuhrdaten-stadt-stgallen&q=&rows=100&sort=-datum&facet=gebiets_id&facet=datum&refine.sammlung=Karton&refine.datum=" + requestedDate

        records = json.load(urlopen(url))['records']
        areaCodes =[]
        for record in records:
            areaCodes.append(record['fields']['gebiets_id'].upper())
    
        return areaCodes

    @staticmethod
    def GetTodayCardboardDisposalAreaCodes():
        requestedDate = str((datetime.now()).strftime('%Y-%m-%d'))
        url = "https://daten.stadt.sg.ch/api/records/1.0/search/?dataset=abfuhrdaten-stadt-stgallen&q=&rows=100&sort=-datum&facet=gebiets_id&facet=datum&refine.sammlung=Karton&refine.datum=" + requestedDate

        records = json.load(urlopen(url))['records']
        areaCodes =[]
        for record in records:
            areaCodes.append(record['fields']['gebiets_id'].upper())
    
        return areaCodes