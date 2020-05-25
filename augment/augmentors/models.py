from abc import ABC
from typing import List
import csv

from augment.utils import AUGMENT_HOME


class Augmentor(ABC):

    augmentation_type: str = 'augmentation type not specified on Augmentor child class'

    @property
    def input_csv_filepath(self):
        sample_inference_data = AUGMENT_HOME / 'augment' / 'data' / 'sample_inference.csv'
        return sample_inference_data

    def test_augmentation_on_sample(self):
        file = csv.DictReader(open(self.input_csv_filepath))
        print(f"Testing augmentation for Augmentor '{self.augmentation_type}'")
        for line in file:
            print("-------------------------------")
            print("Original text:")
            original_text = line['text']
            print('0:', original_text)
            print("Augmentations of original text:")
            for i, augmented_sample in enumerate(self.augment(original_text)):
                print(f'{i+1}:', augmented_sample)

    def augment(self, text: str) -> List[str]:
        raise NotImplementedError
