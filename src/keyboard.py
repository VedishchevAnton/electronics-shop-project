from src.item import Item


class Keyboard(Item):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Keyboard
        """
        super().__init__(name, price, quantity)
        self.language = "EN"
