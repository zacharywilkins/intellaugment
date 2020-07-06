from abc import ABC
from typing import List
from copy import deepcopy
import os
import csv
import logging

from augment.utils import AUGMENT_HOME


class Augmentor(ABC):

    csv_filename: str

    augmentation_type: str = 'augmentation type not specified on Augmentor child class'
    max = 10 # Maximum number of new samples from a single augmentor

    @property
    def input_csv_filepath(self):
        sample_inference_data = AUGMENT_HOME / 'data' / 'input' / self.csv_filename
        return sample_inference_data

    @property
    def output_csv_filepath(self):
        sample_inference_data = AUGMENT_HOME / 'data' / 'output' / self.csv_filename
        return sample_inference_data

    def augment(self, text: str) -> List[str]:
        raise NotImplementedError

    def augment_unique(self, text: str) -> List[str]:
        new_examples = self.augment(text)
        all_examples = new_examples + [text]
        return list(set(all_examples))

    def try_augmentation_on_string(self, text: str) -> List[str]:
        print(self.augment_unique(text))

    def try_augmentation_on_sample_csv(self):
        logging.debug(f" Testing augmentation for Augmentor '{self.augmentation_type}'")

        sample_csv_filename = 'sample_inference.csv'

        self.augment_csv(sample_csv_filename)

    def augment_csv(self, filename: str):
        self.csv_filename = filename

        # Raise error if input string is not a csv filepath
        try:
            file = open(self.input_csv_filepath)
            file.close()
        except:
            raise OSError(
                f"Input file '{self.csv_filename}' must be added to '{AUGMENT_HOME/'data'/'input'}'"
            )

        # Delete any previously generated output file
        if os.path.exists(self.output_csv_filepath):
            os.remove(self.output_csv_filepath)

        file_reader = csv.DictReader(open(self.input_csv_filepath))
        augmented_sample_key = "augmented_text"

        # Create empty file with new header names
        new_fieldnames = file_reader.fieldnames + [augmented_sample_key]
        file_writer = csv.DictWriter(
            open(self.output_csv_filepath, 'w', newline=''), fieldnames=new_fieldnames
        )
        file_writer.writeheader()

        for line in file_reader:
            original_text = line["text"]
            new_line = deepcopy(line)

            logging.debug(" Original text:")
            logging.debug(f" 0: {original_text}")
            logging.debug(" Augmentations of original text:")

            new_examples = self.augment_unique(original_text)
            for i, augmented_sample in enumerate(new_examples):
                logging.debug(f" {i+1}: {augmented_sample}")

                new_line[augmented_sample_key] = augmented_sample
                file_writer.writerow(new_line)

            logging.debug(" -------------------------------")
