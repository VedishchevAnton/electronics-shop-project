from src.item import Item
from src.mixin import Mixinlanguage


class KeyBoard(Item, Mixinlanguage):
    """
    Класс для товара “клавиатура”
    """

    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.language = language
