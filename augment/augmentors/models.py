from abc import ABC


class Augmentor(ABC):

    augmentation_type: str

    def augment(self):
        raise NotImplementedError
