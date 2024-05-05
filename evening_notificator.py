import asyncio
from datetime import datetime, timedelta
import json
import logging
from telegram import Bot

from helpers.erz_api_helper import DisposalType, get_disposal_postal_codes
from helpers.translator import get_translation, get_translation_key
from infrastructure.subscription_manager import get_subscriptions

async def send_notifications(bot):
    date = datetime.now() + timedelta(days=1)
    subscriptions = get_subscriptions()
    
    for disposal_type in DisposalType:
        try:
            postal_codes = get_disposal_postal_codes(date, disposal_type)
            postal_codes = {str(code).strip() for code in postal_codes}
        
            for subscription in subscriptions:
                if subscription.area in postal_codes:
                    try:
                        translation_key = get_translation_key(disposal_type, "tomorrow")
                        message = get_translation(subscription.culture, translation_key)
                        await bot.send_message(chat_id=subscription.chat_id, text=message)
                    except Exception as e:
                        logging.error(f"Failed to send message for chat_id {subscription.chat_id}: {str(e)}")
                        continue
        except Exception as e:
            logging.error(f"Error processing disposal type {disposal_type}: {str(e)}")
            continue

async def main():
    logging.basicConfig(level=logging.ERROR)
    with open('config_prod.json') as config_file:
        config = json.load(config_file)

    token = config["telegram"]["token"]
    bot = Bot(token)

    await send_notifications(bot)

if __name__ == '__main__':
    asyncio.run(main())