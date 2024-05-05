import json
from enum import Enum

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

def load_translations(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        translations = json.load(file)
    return translations

translations = load_translations('helpers/translations.json')

def get_translation(locale: str, message_key: TranslationKeys) -> str:
    return translations[locale][message_key.value]
        
