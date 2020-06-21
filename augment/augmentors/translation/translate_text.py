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
        response = GoogleTranslator().detect(self.original_text)
        return response.lang

    def translate_and_re_translate(self) -> str:
        if self.detected_lang != self.from_lang:
            logger.warning(f"Original input not in expected language('{self.from_lang}')")
            return self.original_text

        translation_response = GoogleTranslator().translate(
            self.original_text, self.to_lang, self.from_lang
        )
        translated_text = translation_response.text
        retranslation_response = GoogleTranslator().translate(
            translated_text, self.from_lang, self.to_lang
        )

        return retranslation_response.text
