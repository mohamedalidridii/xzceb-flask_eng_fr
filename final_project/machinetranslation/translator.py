import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

VERSION = "2018-05-01"

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    """
    English to French Translator
    """
    french_text = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """
    French to English Translator
    """
    english_text = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")