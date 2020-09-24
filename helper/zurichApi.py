from datetime import datetime
from datetime import date
from datetime import timedelta
from urllib.request import urlopen
import json

class zurichApi:
    @staticmethod
    def GetTomorrowPaperDisposalZipCodes():
        requestedDate = str((datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
        url = "http://openerz.metaodi.ch/api/calendar/paper.json?start=" + requestedDate + "&end=" + requestedDate + "&offset=0&limit=0"

        records = json.load(urlopen(url))['result']
        zipCodes =[]
        for record in records:
            zipCodes.append(record['zip'])
    
        return zipCodes

    @staticmethod
    def GetTodayPaperDisposalZipCodes():
        requestedDate = str((datetime.now()).strftime('%Y-%m-%d'))
        url = "http://openerz.metaodi.ch/api/calendar/paper.json?start=" + requestedDate + "&end=" + requestedDate + "&offset=0&limit=0"

        records = json.load(urlopen(url))['result']
        zipCodes =[]
        for record in records:
            zipCodes.append(record['zip'])
    
        return zipCodes

    @staticmethod
    def GetTomorrowCardboardDisposalZips():
        requestedDate = str((datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
        url = "http://openerz.metaodi.ch/api/calendar/cardboard.json?start=" + requestedDate + "&end=" + requestedDate + "&offset=0&limit=0"

        records = json.load(urlopen(url))['result']
        zipCodes =[]
        for record in records:
            zipCodes.append(record['zip'])

        print(zipCodes)
    
        return zipCodes

    @staticmethod
    def GetTodayCardboardDisposalZips():
        requestedDate = str((datetime.now()).strftime('%Y-%m-%d'))
        url = "http://openerz.metaodi.ch/api/calendar/cardboard.json?start=" + requestedDate + "&end=" + requestedDate + "&offset=0&limit=0"

        records = json.load(urlopen(url))['result']
        zipCodes =[]
        for record in records:
            zipCodes.append(record['zip'])
    
        return zipCodes