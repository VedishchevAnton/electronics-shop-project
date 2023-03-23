import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def test_keyboard():
    return KeyBoard('DEXP Sparkle', 4500, 2)


def test__init__(test_keyboard):
    """
    Тест инициализации класса KeyBoard
    """
    assert str(test_keyboard.name) == "DEXP Sparkle"
    assert str(test_keyboard.language) == "EN"


def test_change_lang(test_keyboard):
    """Тест метода смены языка"""
    test_keyboard.change_lang()
    assert str(test_keyboard.language) == "RU"


def test_change_lang_2(test_keyboard):
    test_keyboard.change_lang().change_lang()
    assert str(test_keyboard.language) == "EN"
