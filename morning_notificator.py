import asyncio
from datetime import datetime
import json
from telegram import Bot

from helpers.erz_api_helper import DisposalType, get_disposal_postal_codes
from helpers.translator import get_translation, get_translation_key
from infrastructure.subscription_manager import get_subscriptions

async def send_notifications(bot):
    date = datetime.now()
    subscriptions = get_subscriptions()

    for disposal_type in DisposalType:
        postal_codes = get_disposal_postal_codes(date, disposal_type)
        postal_codes = {str(code).strip() for code in postal_codes}

        for subscription in subscriptions:
            if subscription.area in postal_codes:
                translation_key = get_translation_key(disposal_type, "today")
                message = get_translation(subscription.culture, translation_key)
                await bot.send_message(chat_id=subscription.chat_id, text=message)

async def main():
    with open('config_prod.json') as config_file:
        config = json.load(config_file)

    token = config["telegram"]["token"]
    bot = Bot(token)

    await send_notifications(bot)

if __name__ == '__main__':
    asyncio.run(main())