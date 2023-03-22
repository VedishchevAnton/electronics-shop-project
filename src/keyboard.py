from src.item import Item
from src.mixin import MixinLanguage


class Keyboard(Item, MixinLanguage):

    def __init__(self, name: str, price: float, quantity: int, language="EN") -> None:
        """
        Создание экземпляра класса Keyboard
        """
        super().__init__(name, price, quantity)
        self.language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        if lang == "EN" or lang == "RU":
            self.__language = lang
        else:
            raise AttributeError("Unsupported language")
