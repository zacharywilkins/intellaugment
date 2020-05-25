from typing import List

from augment.augmentors.models import Augmentor


class TranslationAugmentor(Augmentor):

    augmentation_type: str = 'translation'

    def augment(self, text: str) -> List[str]:
        return [text, text, text]
