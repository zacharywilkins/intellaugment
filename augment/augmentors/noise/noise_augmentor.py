from typing import List
import yaml
import re

from augment.augmentors.models import Augmentor
from augment.utils import AUGMENT_HOME


class NoiseAugmentor(Augmentor):
    """
        This augmentor adds pragmatic linguistic "noise",
        i.e. content that can affect an utterance's
        contextual meaning, but has no material impact
        on its standalone semantic content.
    """
    augmentation_type: str = 'noise'
    clause_boundary_discourse_markers: list = []
    discourse_marker_counter: int = 0

    def __init__(self):
        self.discourse_markers = self.load_discourse_markers()
        self.num_discourse_markers = len(self.discourse_markers)

    def increment_discourse_marker_counter(self):
        self.discourse_marker_counter += 1
        if self.discourse_marker_counter == self.num_discourse_markers:
            self.discourse_marker_counter = 0

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

        if discourse_marker.lower() not in text.lower():
            new_text = discourse_marker + " " + text[0].lower() + text[1:]
            self.increment_discourse_marker_counter()
            # Need to implement counter re-starter
            return new_text
        return text

    def append_noise(self, text: str) -> str:
        discourse_markers = self.load_discourse_markers()
        discourse_marker = discourse_markers[self.discourse_marker_counter]

        # Regex excludes exclamatives/interrogatives to improve naturalness:
        re_end_of_declarative = re.compile(r"(?<=\w)\s*\.?\s*$")
        ends_with_word = re_end_of_declarative.search(text, re.IGNORECASE)

        if discourse_marker.lower() not in text.lower() and ends_with_word:
            new_text = text
            new_text = re_end_of_declarative.sub(" " + discourse_marker.lower(), new_text)
            if text.endswith("."):
                new_text = new_text + "."
            self.increment_discourse_marker_counter()
            return new_text
        return text

    def augment(self, text: str) -> List[str]:
        augmented_examples = [self.prepend_noise(text), self.append_noise(text)]
        return augmented_examples
