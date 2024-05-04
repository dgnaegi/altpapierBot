import json
import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from postal_code_helper import get_postal_code, VALID_POSTAL_CODES
from subscription_manager import add_subscription, Subscription
from translator import get_translation, TranslationKeys

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")

async def registration_en(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    postal_code = get_postal_code(context.args)
    chat_id = context._chat_id
    culture = "en-CH"

    if(postal_code is None):
        message = get_translation(culture, TranslationKeys.REGISTRATION_ERROR)
        valid_entries = ", ".join(str(code.value) for code in VALID_POSTAL_CODES)
        print(valid_entries)
        return

    new_subscription = registration(chat_id, postal_code, culture)
    message = get_translation(culture, TranslationKeys.CONFIRMATION)

    await update.message.reply_html(
        rf"{message}{new_subscription.area}",
        reply_markup=ForceReply(selective=True),
    )

async def registration_de(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    postal_code = get_postal_code(context.args)
    chat_id = context._chat_id
    culture = "de-CH"

    new_subscription = registration(chat_id, postal_code, culture)
    message = get_translation(culture, TranslationKeys.CONFIRMATION)

    await update.message.reply_html(
        rf"{message}{new_subscription.area}",
        reply_markup=ForceReply(selective=True),
    )

async def registration(chat_id: int, postal_code: int, culture: str) -> Subscription:
    region = "Zurich"
    area = postal_code
    enable_notifications = True

    return add_subscription(chat_id, region, area, enable_notifications, culture)

async def send_registration_error(culture: str, update: Update) -> None:
    message = get_translation(culture, TranslationKeys.REGISTRATION_ERROR)
    valid_entries = ", ".join(str(code.value) for code in VALID_POSTAL_CODES)
    await update.message.reply_html(
        rf"{message}",
        reply_markup=ForceReply(selective=True),
    )
    await update.message.reply_html(
        rf"{valid_entries}",
        reply_markup=ForceReply(selective=True),
    )

def main() -> None:
    with open('config_prod.json') as data_file:    
        data = json.load(data_file)
        token = data["telegram"]["token"]

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("plz", registration_de))
    application.add_handler(CommandHandler("postalcode", registration_en))
    application.add_handler(CommandHandler("help", help))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()