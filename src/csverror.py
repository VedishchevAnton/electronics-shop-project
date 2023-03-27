class CSVError(Exception):
    """Класс-исключение для проверки файлов .csv"""

    def __init__(self, *args):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message

