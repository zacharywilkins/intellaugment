from abc import ABC
from typing import List
import csv
import logging

from augment.utils import AUGMENT_HOME

# logger = logging.getLogger(__name__)


class Augmentor(ABC):

    augmentation_type: str = 'augmentation type not specified on Augmentor child class'

    @property
    def input_csv_filepath(self):
        sample_inference_data = AUGMENT_HOME / 'data' / 'sample_inference.csv'
        return sample_inference_data

    @property
    def output_csv_filepath(self):
        sample_inference_data = AUGMENT_HOME / 'output' / 'sample_inference_augmented.csv'
        return sample_inference_data

    def augment(self, text: str) -> List[str]:
        raise NotImplementedError

    def augment_unique(self, text: str) -> List[str]:
        new_examples = self.augment(text)
        all_examples = new_examples + [text]
        return list(set(all_examples))

    def test_augmentation_on_string(self, text:str) -> List[str]:
        print(self.augment_unique(text))

    def test_augmentation_on_sample_csv(self):
        file = csv.DictReader(open(self.input_csv_filepath))
        logging.debug(f"Testing augmentation for Augmentor '{self.augmentation_type}'")

        for line in file:
            original_text = line["text"]

            logging.debug("-------------------------------")
            logging.debug("Original text:")
            logging.debug(f"0: {original_text}")
            logging.debug("Augmentations of original text:")

            for i, augmented_sample in enumerate(self.augment_unique(original_text)):
                logging.debug(f"{i+1}: {augmented_sample}")
