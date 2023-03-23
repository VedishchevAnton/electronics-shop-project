class Mixinlanguage:

    """
    Класс по хранению и изменению раскладки клавиатуры
    """

    def __init__(self):
        self.__language = None

    def change_lang(self):
        """
        Метод изменения языка на клавиатуре
        """
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, selected_lang):
        if selected_lang == "EN" or selected_lang == "RU":
            self.__language = selected_lang
        else:
            return AttributeError("Всего поддерживается два языка: `EN` и `RU`")
