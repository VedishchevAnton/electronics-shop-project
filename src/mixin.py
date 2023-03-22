class MixinLanguage:
    """
    Класс для смены языка на клавиатуре
    """

    def __init__(self):
        self.language = None

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        else:
            raise ValueError("Invalid language")
