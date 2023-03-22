from src.item import Item


class Keyboard(Item):

    def __init__(self, name: str, price: float, quantity: int, language="EN") -> None:
        """
        Создание экземпляра класса Keyboard
        """
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        pass
