import argparse
import logging

from augment.augmentors.translation.translation_augmentor import TranslationAugmentor


parser = argparse.ArgumentParser(description="Test an Augmentor from the command line. Defaults to TranslationAugmentor.")
parser.add_argument("-c", "--csv", default=False, help="Run Augmentor on CSV filepath given from the command line.")
parser.add_argument("-s", "--sample", default=False, action='store_true', help="Run Augmentor against static sample CSV.")
parser.add_argument("-t", "--text", default=False, help="Pass in an example string to augment from the command line.")


if __name__ == '__main__':
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    if args.csv:
        TranslationAugmentor().augment_csv(args.csv)
    if args.sample:
        TranslationAugmentor().try_augmentation_on_sample_csv()
    if args.text:
        TranslationAugmentor().try_augmentation_on_string(args.text)
        # Try out "I am calm, glad, surprised and content"