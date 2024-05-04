import json
from enum import Enum
import logging

logging.basicConfig(level=logging.ERROR, filename='translation_errors.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TranslationKeys(Enum):
    CONFIRMATION = "confirmation"
    REGISTRATION_ERROR = "registration_error"

def load_translations(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        translations = json.load(file)
    return translations

translations = load_translations('translations.json')

def get_translation(locale: str, message_key: TranslationKeys) -> str:
    try:
        translation = translations.get(locale, {}).get(message_key.value, None)
        if translation is None:
            raise ValueError(f"Translation not found for locale '{locale}' and key '{message_key.value}'")
        return translation
    except ValueError as e:
        logging.error(str(e))
        return "error"
