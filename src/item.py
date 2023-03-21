from src.utils import take_from_csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {int(self.price)}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(self.__name) <= 10:
            self.__name = name
        else:
            raise ValueError("Длина наименования товара должна быть не больше 10 символов!")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return int(self.price) * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.price * self.pay_rate)

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Класс-метод, инициализирующий экземпляры класса
        """
        cls.all = []
        for data in take_from_csv():
            cls(*data)

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Cтатический метод, возвращающий число из числа-строки
        """
        return round(int(value[0]), 2)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError('Складывать можно только объекты Item и дочерние от них')



