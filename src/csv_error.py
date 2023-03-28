class InstantiateCSVError(Exception):
    """Класс-исключение для проверки файлов .csv"""

    def __init__(self, *args) -> None:
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self) -> str:
        return self.message
