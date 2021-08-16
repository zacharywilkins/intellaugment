import unittest

from augment.augmentors.translation.translation_augmentor import TranslationAugmentor
from augment.augmentors.noise.noise_augmentor import NoiseAugmentor


class TestAugmentors(unittest.TestCase):

    def test_translation_augmentor(self):
        original_sample = "A man inspects the uniform of a figure in some East Asian country."
        expected_augmented_sample = "A man inspects the uniform of a figure in an eastern Asian country."
        actual_augmentated_samples = TranslationAugmentor().try_augmentation_on_string(original_sample)
        self.assertIn(expected_augmented_sample, actual_augmentated_samples)

    def test_noise_augmentor(self):
        original_sample = "A man inspects the uniform of a figure in some East Asian country."
        expected_augmented_sample = "Actually a man inspects the uniform of a figure in some East Asian country."
        actual_augmentated_samples = NoiseAugmentor().try_augmentation_on_string(original_sample)
        self.assertIn(expected_augmented_sample, actual_augmentated_samples)
