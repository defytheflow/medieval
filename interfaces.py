"""

"""

from abc import ABC, abstractmethod


class Bilingual(ABC):

    @abstractmethod
    def switch_lang(self, lang: str):
        pass
