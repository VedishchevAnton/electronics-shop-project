import pytest
from src.utils import take_from_csv


@pytest.fixture
def data_csv():
    return take_from_csv()


def test_take_from_csv_exists(data_csv):
    assert data_csv is not None


def test_take_from_csv_exists_2(data_csv):
    with pytest.raises(FileNotFoundError):
        raise FileNotFoundError('Отсутствует файл item.csv')


def test_take_from_csv_correct_data(data_csv):
    data_list = data_csv
    assert len(data_list) > 0
    assert isinstance(data_list[0], list)
    assert isinstance(data_list[0][0], str)
