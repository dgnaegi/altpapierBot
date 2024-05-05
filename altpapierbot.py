import json
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from helpers.postal_code_helper import get_postal_code, VALID_POSTAL_CODES
from infrastructure.subscription_manager import add_subscription, get_subscription_by_chat_id, delete_subscription, update_subscription
from helpers.translator import get_translation, TranslationKeys

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = context._chat_id
    subscription = get_subscription_by_chat_id(chat_id)
    if subscription is not None:
        message = get_translation(subscription.culture, TranslationKeys.WELCOME)
        await update.message.reply_html(message)
        return

    message_de = get_translation("de-CH", TranslationKeys.WELCOME)
    message_en = get_translation("en-CH", TranslationKeys.WELCOME)
    await update.message.reply_html("ENGLISH BELOW")
    await update.message.reply_html(message_de)
    await update.message.reply_html("------------")
    await update.message.reply_html(message_en)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = context._chat_id
    subscription = get_subscription_by_chat_id(chat_id)
    if subscription is not None:
        message = get_translation(subscription.culture, TranslationKeys.HELP)
        await update.message.reply_html(message)
        return
    
    message_de = get_translation("de-CH", TranslationKeys.HELP)
    message_en = get_translation("en-CH", TranslationKeys.HELP)
    await update.message.reply_html("ENGLISH BELOW")
    await update.message.reply_html(message_de)
    await update.message.reply_html("------------")
    await update.message.reply_html(message_en)

async def de(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = context._chat_id
    culture = "de-CH"

    message = language_update(chat_id, culture)

    await update.message.reply_html(
        rf"{message}",
    )

async def en(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = context._chat_id
    culture = "en-CH"

    message = language_update(chat_id, culture)

    await update.message.reply_html(
        rf"{message}",
    )

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = context._chat_id

    subscription = get_subscription_by_chat_id(chat_id)
    if subscription is None:
        error = get_translation("en-CH", TranslationKeys.NO_SUBSCRIPTION_FOUND)
        await update.message.reply_html(
            rf"{error}",
        )
        return
    
    delete_subscription(chat_id)
    message = get_translation(subscription.culture, TranslationKeys.UNSUBSCRIBE_CONFIRMATION)
    await update.message.reply_html(
        rf"{message}",
    )

async def start_spam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = context._chat_id
    subscription = get_subscription_by_chat_id(chat_id)
    message = ""

    if subscription is None:
        message = get_translation("de-CH", TranslationKeys.NO_SUBSCRIPTION_FOUND)
    else:
        update_subscription(chat_id=subscription.chat_id, enable_notifications=1)
        message = get_translation(subscription.culture, TranslationKeys.START_SPAM_CONFIRMATION)

    await update.message.reply_html(
        rf"{message}",
    )

async def stop_spam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = context._chat_id
    subscription = get_subscription_by_chat_id(chat_id)
    message = ""

    if subscription is None:
        message = get_translation("de-CH", TranslationKeys.NO_SUBSCRIPTION_FOUND)
    else:
        update_subscription(chat_id=subscription.chat_id, enable_notifications=0)
        message = get_translation(subscription.culture, TranslationKeys.STOP_SPAM_CONFIRMATION)

    await update.message.reply_html(
        rf"{message}",
    )

async def registration_en(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = context._chat_id
    culture = "en-CH"

    message = registration(chat_id, context.args, culture)

    await update.message.reply_html(
        rf"{message}",
    )

async def registration_de(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = context._chat_id
    culture = "de-CH"

    message = registration(chat_id, context.args, culture)

    await update.message.reply_html(
        rf"{message}",
    )

def registration(chat_id: int, args: list[str], culture: str) -> str:
    region = "Zurich"
    enable_notifications = True

    subscription = get_subscription_by_chat_id(chat_id)

    if subscription is not None:
        error = get_translation(subscription.culture, TranslationKeys.ALREADY_SUBSCRIBED_ERROR)
        return rf"{error}{subscription.area}"

    postal_code = get_postal_code(args)
    area = postal_code
    
    if postal_code is None:
        message = get_translation(culture, TranslationKeys.REGISTRATION_ERROR)
        valid_entries = ", ".join(str(code) for code in VALID_POSTAL_CODES)
        return rf"{message}{valid_entries}"

    subscription = add_subscription(chat_id, region, area, enable_notifications, culture)
    message = get_translation(culture, TranslationKeys.CONFIRMATION)
    return rf"{message}{subscription.area}"

def language_update(chat_id: int, culture: str) -> str:
    subscription = get_subscription_by_chat_id(chat_id)

    if subscription is None:
        return get_translation(culture, TranslationKeys.NO_SUBSCRIPTION_FOUND)
    
    update_subscription(chat_id=subscription.chat_id, culture=culture)
    return get_translation(culture, TranslationKeys.LANGUAGE_CHANGE)

def main() -> None:
    with open('/home/dgnaegi/altpapierBot/config_prod.json') as data_file:    
        data = json.load(data_file)
        token = data["telegram"]["token"]

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("plz", registration_de))
    application.add_handler(CommandHandler("postalcode", registration_en))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("de", de))
    application.add_handler(CommandHandler("en", en))
    application.add_handler(CommandHandler("start_spam", start_spam))
    application.add_handler(CommandHandler("stop_spam", stop_spam))
    application.add_handler(CommandHandler("help", help))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()