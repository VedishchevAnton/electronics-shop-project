from src.item import Item


class Keyboard(Item):

    def __init__(self, name: str, price: float, quantity: int, language="EN") -> None:
        """
        Создание экземпляра класса Keyboard
        """
        super().__init__(name, price, quantity)
        self.language = language


class MixinLanguage:

    def __init__(self):
        self.language = None

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        else:
            raise ValueError("Invalid language")
