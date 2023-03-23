from src.item import Item
from src.mixin import MixinLanguage


class KeyBoard(Item, MixinLanguage):
    """
    Класс для товара “клавиатура”
    """

    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.language = language
