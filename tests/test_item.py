"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_item_init():
    """
    Тест инициации класса Item
    """
    item1 = Item("Смартфон", 10000, 20)

    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20

