from datetime import datetime, timedelta

from helpers.erz_api_helper import DisposalType, get_disposal_postal_codes
from infrastructure.subscription_manager import get_subscriptions

date = datetime.now() + timedelta(days=1)
subscriptions = get_subscriptions()

for disposal_type in DisposalType:
    postal_codes = get_disposal_postal_codes(date, disposal_type)
    postal_codes = {str(code).strip() for code in postal_codes}

    for subscription in subscriptions:
        if subscription.area in postal_codes:
            print("Subscription contains postal code for ")
            print(disposal_type.value)