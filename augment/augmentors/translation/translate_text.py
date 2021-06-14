import logging
from googletrans import Translator as GoogleTranslator

logger = logging.getLogger(__name__)


class Translator:

    def __init__(self, text: str, to_lang='de', from_lang='en'):
        self.original_text = text
        self.to_lang = to_lang
        self.from_lang = from_lang

    @property
    def detected_lang(self) -> str:
        try:
            response = GoogleTranslator().detect(self.original_text)
            lang = response.lang
        except:
            lang = 'en'
        return lang

    def handle_google_translate_call(self, text, to_lang, from_lang) -> str:
        try:
            response = GoogleTranslator().translate(
                text, to_lang, from_lang
            )
            translation = response.text
        except Exception as e: # Fall back to returning original string
            logger.warning(f"Call to Google Translate failed with this error: {e}")
            translation = text
        return translation

    def translate_and_re_translate(self) -> str:
        if self.detected_lang != self.from_lang:
            logger.warning(f"Original input not in expected language('{self.from_lang}')")
            return self.original_text

        translation_response = self.handle_google_translate_call(
            self.original_text, self.to_lang, self.from_lang
        )
        translated_text = translation_response
        retranslation_response = self.handle_google_translate_call(
            translated_text, self.from_lang, self.to_lang
        )

        return retranslation_response
