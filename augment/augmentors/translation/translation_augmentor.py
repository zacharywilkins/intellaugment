from typing import List

from augment.augmentors.models import Augmentor
from augment.augmentors.translation.translate import Translator


class TranslationAugmentor(Augmentor):

    augmentation_type: str = 'translation'

    def augment_using_portuguese(self, text: str) -> str:
        new_text = Translator(text, 'pt').translate_and_re_translate()
        return new_text

    def augment_using_german(self, text: str) -> str:
        new_text = Translator(text, 'de').translate_and_re_translate()
        return new_text

    def augment(self, text: str) -> List[str]:
        augmented_examples = [
            self.augment_using_portuguese(text), self.augment_using_german(text)
        ]
        return augmented_examples

