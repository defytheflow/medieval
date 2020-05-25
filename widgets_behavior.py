import abc

from typing import Dict


class Bilingual(abc.ABC):

    @abc.abstractmethod
    def __init__(self, text_dict: Dict[str, str]):
        self.text_dict = text_dict

    @abc.abstractmethod
    def switch_lang(self, lang: str):
        raise NotImplementedError
