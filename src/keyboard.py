from src.item import Item


class LanguageMixin:
    LanguageMixin = {"EN", "RU"}

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Меняет атрибут клавиатуры language.
        """
        if self.language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        """
        Создание экземпляра класса Keyboard.
        name: Название товара.
        price: Цена за единицу товара.
        quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)
