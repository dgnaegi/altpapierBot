import json
from enum import Enum

from helpers.erz_api_helper import DisposalType

class TranslationKeys(Enum):
    CONFIRMATION = "confirmation"
    REGISTRATION_ERROR = "registration_error"
    ALREADY_SUBSCRIBED_ERROR = "already_subscribed_error"
    NO_SUBSCRIPTION_FOUND = "no_subscription_found"
    UNSUBSCRIBE_CONFIRMATION = "unsubscribe_confirmation"
    LANGUAGE_CHANGE = "language_change"
    START_SPAM_CONFIRMATION = "start_spam_confirmation"
    STOP_SPAM_CONFIRMATION = "stop_spam_confirmation"
    WELCOME = "welcome"
    HELP = "help"
    PAPER_TODAY = "paper_today"
    PAPER_TOMORROW = "paper_tomorrow"
    CARDBOARD_TODAY = "cardboard_today"
    CARDBOARD_TOMORROW = "cardboard_tomorrow"
    SERVICE_NOTIFICATION = "service_notification"

def load_translations(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        translations = json.load(file)
    return translations

translations = load_translations('/home/dgnaegi/altpapierBot/helpers/translations.json')

def get_translation(locale: str, message_key: TranslationKeys) -> str:
    return translations[locale][message_key.value]
        
def get_translation_key(disposal_type: DisposalType, date: str) -> TranslationKeys:
    key_name = f"{disposal_type.value.upper()}_{date.upper()}"
    return TranslationKeys[key_name]