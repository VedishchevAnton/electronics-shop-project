from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, sim_count: int, quantity: int):
        """
        Создание экземпляров класса Phone
        """
        super().__init__(name, price, quantity)
        self.sim_count = sim_count
