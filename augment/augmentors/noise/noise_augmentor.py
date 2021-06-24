from typing import List
import yaml
import re

from augment.augmentors.models import Augmentor
from augment.utils import AUGMENT_HOME

class NoiseAugmentor(Augmentor):

    augmentation_type: str = 'noise'
    clause_boundary_discourse_markers: list = []
    discourse_marker_counter: int = 0

    def __init__(self):
        self.discourse_markers = self.load_discourse_markers()
        self.num_discourse_markers = len(self.discourse_markers)

    def load_discourse_markers(self) -> List[str]:
        """
            Discourse marker list taken from https://www.thoughtco.com/sentence-adverb-1692084
        """
        pragmatic_fillers_filepath = AUGMENT_HOME / 'augmentors' / 'noise' / 'pragmatic_fillers.yml'
        with open(pragmatic_fillers_filepath, "r") as stream:
            try:
                all_pragmatic_fillers = yaml.safe_load(stream)
                discourse_markers = all_pragmatic_fillers.get("discourse_markers")
            except yaml.YAMLError:
                discourse_markers = []
        return discourse_markers

    def prepend_noise(self, text: str) -> str:
        discourse_markers = self.load_discourse_markers()
        discourse_marker = discourse_markers[self.discourse_marker_counter]

        new_text = ""
        if discourse_marker.lower() not in text.lower():
            new_text = discourse_marker + " " + text[0].lower() + text[1:]
            self.discourse_marker_counter += 1
            # Need to implement counter re-starter
        return new_text

    def append_noise(self, text: str) -> str:
        discourse_markers = self.load_discourse_markers()
        discourse_marker = discourse_markers[self.discourse_marker_counter]

        new_text = ""
        re_end_of_sentence = r"\w[.!?]?$"
        ends_with_word = re.match(re_end_of_sentence, text, re.IGNORECASE)
        if discourse_marker.lower() not in text.lower() and ends_with_word:
            new_text = re.sub(re_end_of_sentence, text[:-1] + discourse_marker.lower() + text[-1], text)
            self.discourse_marker_counter += 1
        return new_text

    def augment(self, text: str) -> List[str]:
        # augmented_examples = [self.prepend_noise(text), self.append_noise(text)]
        augmented_examples = [self.append_noise(text)]
        return augmented_examples
