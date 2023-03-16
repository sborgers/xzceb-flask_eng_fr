'''
This module provides a proof of concept implementation of the IBM Waton translation service
Translating from Englih to French and back to English again
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


def englishToFrench(english_text="No English text provided to translate"):
    '''
    englishToFrench translates an English text to French using IBM
    Watson translation services

    Args:
    a (string) English Text

    Return:
    string: French text
    '''

    french_text = language_translator.translate(
                     text=english_text,
                     model_id='en-fr').get_result()
    return french_text["translations"][0]["translation"]

def frenchToEnglish(french_text="No French text provided to translate"):
    '''
    frenchToenglish translates a French text to English using IBM
    Watson translation services

    Args:
    a (string) French Text

    Return:
    string: English text
    '''

    english_text = language_translator.translate(
                     text=french_text,
                     model_id='fr-en').get_result()
    return english_text["translations"][0]["translation"]


load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

french_translation = englishToFrench("Hello world")
print(french_translation)

english_translation = frenchToEnglish(french_translation)
print(english_translation)
