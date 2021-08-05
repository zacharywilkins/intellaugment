from abc import ABC
from typing import List

from .augmentors.relocation.relocation_augmentor import RelocationAugmentor
from .augmentors.translation.translation_augmentor import TranslationAugmentor
from .augmentors.noise.noise_augmentor import NoiseAugmentor


class AugmentorConfig(ABC):

    augmentor_keys: list = []
    augmentor_classes : list = []
    augmentor_keys_to_classes: dict = {
        'relocation': RelocationAugmentor,
        'translation': TranslationAugmentor,
        'noise': NoiseAugmentor
    }
    all_augmentor_keys = augmentor_keys_to_classes.keys()

    def __init__(self, augmentor_keys: list):
        if augmentor_keys is None:
            self.augmentor_keys = augmentor_keys
        else:
            self.augmentor_keys = augmentor_keys
        self.map_augmentor_keys_to_classes()

    def map_augmentor_keys_to_classes(self, augmentor_keys: List[str]) -> None:
        """
            Takes a list of augmentor keys as input and saves the corresponding
             Python classes in a list. If augmentor_keys is not provided,
             this method defaults to including all augmentor classes in the
             output.
        """
        if not augmentor_keys:
            augmentor_keys = self.all_augmentor_keys
        augmentor_classes = []
        for key in augmentor_keys:
            if key in self.augmentor_keys_to_classes:
                augmentor_classes.append(self.augmentor_keys_to_classes[key])
        self.augmentor_classes = augmentor_classes

    def augment_example(self, text: str) -> List[str]:
        """
            Takes a single string as input and returns a list of
             augmented example strings.
        """
        new_texts = []
        for Augmentor in self.augmentor_classes:
            new_texts.extend(Augmentor.augment(text))
        return new_texts

    def validate_csv(self, csv_file) -> bool:
        return True

    def augment_csv(self, csv_file) -> None:
        """
            Takes a csv file as input and saves an augmented version of that
             csv to the current working directory. Returns nothing.
        """
        if self.validate_csv(csv_file) is False:
            raise NotImplementedError
        else:
            output_filename = 'augmented_data.csv'


