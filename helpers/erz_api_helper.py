from datetime import datetime
from enum import Enum
import json
from urllib.request import urlopen

class DisposalType(Enum):
    CARDBOARD = "cardboard"
    PAPER = "paper"

def get_disposal_postal_codes(date: datetime, disposal_type: DisposalType) -> list[str]:
    requested_date = date.strftime('%Y-%m-%d')
    url = f"http://openerz.metaodi.ch/api/calendar.json?types={disposal_type.value}&region=zurich&start={requested_date}&end={requested_date}&offset=0&limit=100"

    response = urlopen(url)
    records = json.load(response)['result']
    zip_codes = []
    for record in records:
        if 'zip' in record:
            try:
                zip_code = record['zip']
                zip_codes.append(zip_code)
            except ValueError:
                continue

    return zip_codes