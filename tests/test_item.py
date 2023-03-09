"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


#
def test_item_init():
    """
    Тест инициации класса Item
    """
    item1 = Item("Смартфон", 10000, 20)

    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20
    assert isinstance(item1.name, str)
    assert isinstance(item1.price, float)
    assert isinstance(item1.quantity, int)


def test_item_apply_discount():
    """
    Тест расчета общей стоимости конкретного товара
    """
    item1 = Item("Смартфон", 10000, 20)
    assert int(item1.price * item1.quantity) == 200000

