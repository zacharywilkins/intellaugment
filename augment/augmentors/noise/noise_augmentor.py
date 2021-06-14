from typing import List
import yaml

from augment.augmentors.models import Augmentor
from augment.utils import AUGMENT_HOME

class NoiseAugmentor(Augmentor):

    augmentation_type: str = 'noise'

    def load_discourse_markers(self) -> List[str]:
        """
            Discourse marker list taken from https://www.thoughtco.com/sentence-adverb-1692084
        """
        discourse_markers_filepath = AUGMENT_HOME / 'augmentors' / 'noise' / 'discourse_markers.yml'
        with open(discourse_markers_filepath, "r") as stream:
            try:
                discourse_markers = yaml.safe_load(stream)
                clause_boundary_discourse_markers = discourse_markers.get("clause_boundary")
            except yaml.YAMLError:
                clause_boundary_discourse_markers = ["Error"]
        return clause_boundary_discourse_markers


    def augment(self, text: str) -> List[str]:
        augmented_examples = self.load_noisy_discourse_markers()
        return augmented_examples
