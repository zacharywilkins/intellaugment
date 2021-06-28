import argparse
import logging

from augment.augmentors.relocation.relocation_augmentor import RelocationAugmentor
from augment.augmentors.translation.translation_augmentor import TranslationAugmentor
from augment.augmentors.noise.noise_augmentor import NoiseAugmentor


parser = argparse.ArgumentParser(description="Test an Augmentor from the command line. Defaults to TranslationAugmentor.")
parser.add_argument("-a", "--augmentor", default=False, help="")
parser.add_argument("-c", "--csv", default=False, help="Run Augmentor on CSV filepath given from the command line.")
parser.add_argument("-s", "--sample", default=False, action='store_true', help="Run Augmentor against static sample CSV.")
parser.add_argument("-t", "--text", default=False, help="Pass in an example string to augment from the command line.")

all_augmentors = [TranslationAugmentor(), NoiseAugmentor(), RelocationAugmentor()]

if __name__ == '__main__':
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    libraries_to_suppress = ["urllib3", "hpack", "httpx"]
    for library in libraries_to_suppress:
        logging.getLogger(library).setLevel(logging.WARNING)

    if args.csv:
        TranslationAugmentor().augment_csv(args.csv)
    if args.sample:
        # TranslationAugmentor().try_augmentation_on_sample_csv()
        # NoiseAugmentor().try_augmentation_on_sample_csv()
        RelocationAugmentor().try_augmentation_on_sample_csv()
    if args.text:
        TranslationAugmentor().try_augmentation_on_string(args.text)
        # Try out "I am calm, glad, surprised and content"
