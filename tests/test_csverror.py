import pytest
from src.csverror import CSVError


def test_csv_error():
    with pytest.raises(CSVError):
        raise CSVError('Файл item.csv поврежден')
