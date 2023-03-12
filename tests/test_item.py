"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_item_init(item):
    """
    Тест инициации класса Item
    """
    assert item.name == 'Смартфон'
    assert item.price == 10000
    assert item.quantity == 20
    assert isinstance(item.name, str)
    assert isinstance(item.price, float)
    assert isinstance(item.quantity, int)


def test_item_calculate_total_price(item):
    """
    Тест расчета общей стоимости конкретного товара
    """
    assert item.calculate_total_price() == 200000


def test_item_apply_discount(item):
    """
    Тест расчета скидки конкретного товара
    """
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'




