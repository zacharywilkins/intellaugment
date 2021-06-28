from typing import List
import yaml

from augment.augmentors.models import Augmentor
from augment.utils import AUGMENT_HOME


class RelocationAugmentor(Augmentor):
    """
        This augmentor moves core semantic content from
        one part of an utterance to a different part of
        the utterance, in such a way that the truth-
        conditional meaning of the utterance is
        unchanged.
    """
    augmentation_type: str = 'relocation'

    def load_transitive_phrasal_verbs(self) -> List[str]:
        """
            Adapted from https://www.skypeenglishclasses.com/english-phrasal-verbs/
            The phrasal verbs chosen from the site above are exclusively transitive,
            i.e. they are *not* intransitive or ditransitive. In other words,
            the verbs normally take only a direct object and not an indirect object
        """
        phrasal_verbs_filepath = AUGMENT_HOME / 'augmentors' / 'relocation' / 'phrasal_verbs.yml'
        with open(phrasal_verbs_filepath, "r") as stream:
            try:
                all_phrasal_verbs = yaml.safe_load(stream)
                transitive_phrasal_verbs = all_phrasal_verbs.get("transitive_phrasal_verbs")
            except yaml.YAMLError:
                transitive_phrasal_verbs = []
        return transitive_phrasal_verbs

    def thing(self, text: str) -> List[str]:
        thing = [text]
        return thing

    def augment(self, text: str) -> List[str]:
        augmented_examples = [text]
        return augmented_examples
