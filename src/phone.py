from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, sim_count: int, quantity: int):
        """
        Создание экземпляров класса Phone
        @type sim_count: integer
        """
        super().__init__(name, price, quantity)
        if sim_count > 0:
            self.__sim_count = sim_count
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @property
    def sim_count(self):
        return self.__sim_count

    @sim_count.setter
    def sim_count(self, sim_count: int):
        if sim_count > 0:
            self.__sim_count = sim_count
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f'Phone({self.name}, {self.price}, {self.quantity}, {self.sim_count}'
