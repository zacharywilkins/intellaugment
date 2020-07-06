from typing import List
import logging

from augment.augmentors.models import Augmentor
from augment.augmentors.translation.translate_text import Translator


class TranslationAugmentor(Augmentor):

    augmentation_type: str = 'translation'

    def augment_using_spanish(self, text: str) -> str:
        new_text = Translator(text, 'es').translate_and_re_translate()
        # logging.debug(f"    From Spanish: {new_text}")
        return new_text

    def augment_using_german(self, text: str) -> str:
        new_text = Translator(text, 'de').translate_and_re_translate()
        # logging.debug(f"    From German: {new_text}")
        return new_text

    def augment(self, text: str) -> List[str]:
        augmented_examples = [
            self.augment_using_spanish(text), self.augment_using_german(text)
        ]
        return augmented_examples
