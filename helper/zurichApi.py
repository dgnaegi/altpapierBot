from datetime import datetime
from datetime import date
from datetime import timedelta
from urllib.request import urlopen
import json

class zurichApi:
    @staticmethod
    def GetTomorrowPaperDisposalZipCodes():
        requestedDate = str((datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
        url = "http://openerz.metaodi.ch/api/calendar/paper.json?region=zurich&start=" + requestedDate + "&end=" + requestedDate + "&offset=0&limit=100"

        records = json.load(urlopen(url))['result']
        zipCodes =[]
        for record in records:
            if 'zip' not in record:
                continue
            zipCodes.append(record['zip'])

        return zipCodes

    @staticmethod
    def GetTodayPaperDisposalZipCodes():
        requestedDate = str((datetime.now()).strftime('%Y-%m-%d'))
        url = "http://openerz.metaodi.ch/api/calendar/paper.json?region=zurich&start=" + requestedDate + "&end=" + requestedDate + "&offset=0&limit=100"

        records = json.load(urlopen(url))['result']
        zipCodes =[]
        for record in records:
            if 'zip' not in record:
                continue
            zipCodes.append(record['zip'])

        return zipCodes

    @staticmethod
    def GetTomorrowCardboardDisposalZipCodes():
        requestedDate = str((datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
        url = "http://openerz.metaodi.ch/api/calendar/cardboard.json?region=zurich&start=" + requestedDate + "&end=" + requestedDate + "&offset=0&limit=100"

        records = json.load(urlopen(url))['result']
        zipCodes =[]
        for record in records:
            if 'zip' not in record:
                continue
            zipCodes.append(record['zip'])

        print(zipCodes)

        return zipCodes

    @staticmethod
    def GetTodayCardboardDisposalZipCodes():
        requestedDate = str((datetime.now()).strftime('%Y-%m-%d'))
        url = "http://openerz.metaodi.ch/api/calendar/cardboard.json?region=zurich&start=" + requestedDate + "&end=" + requestedDate + "&offset=0&limit=100"

        records = json.load(urlopen(url))['result']
        zipCodes =[]
        for record in records:
            if 'zip' not in record:
                continue
            zipCodes.append(record['zip'])

        return zipCodes
