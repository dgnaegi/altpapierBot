import asyncio
from datetime import datetime, timedelta
import json
import logging
from telegram import Bot

from helpers.translator import get_translation, TranslationKeys
from infrastructure.subscription_manager import get_subscriptions

async def send_notifications(bot):
    subscriptions = get_subscriptions()
    
    for subscription in subscriptions:
        if subscription.enable_service_notifications == True:
            try:
                message = get_translation(subscription.culture, TranslationKeys.SERVICE_NOTIFICATION)
                await bot.send_message(chat_id=subscription.chat_id, text=message)
            except Exception as e:
                logging.error(f"Failed to send message for chat_id {subscription.chat_id}: {str(e)}")
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