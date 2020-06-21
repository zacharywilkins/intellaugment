import argparse
import logging

from augment.augmentors.translation.translation_augmentor import TranslationAugmentor

# logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description="Test an Augmentor from the command line. Defaults to TranslationAugmentor.")
parser.add_argument("-c", "--csv", default=False, action='store_true', help="Run Augmentor against static sample CSV.")
parser.add_argument("-s", "--string", help="Pass in an example string to augment from the command line.")


if __name__ == '__main__':
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    if args.csv:
        TranslationAugmentor().test_augmentation_on_sample_csv()
        # TranslationAugmentor().augment_csv(args.csv)
    if args.string:
        TranslationAugmentor().test_augmentation_on_string(args.string)
        # Try out "I am calm, glad, surprised and content"
