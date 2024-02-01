import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """
        Прверка длинны наименования товара,
        чтобы было не более 10 символов.
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :total_price: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Добавление экземпляра класса из csv файла.
        """
        cls.all = []
        path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(path, 'r', newline="\n") as csv_file:
            reader = csv.DictReader(csv_file)
            items = list(reader)
            for item in items:
                cls(str(item["name"]), float(item["price"]), int(item["quantity"]))

    @staticmethod
    def string_to_number(str_number):
        """
        Возвращает число из числа-строки.
        """
        number = float(str_number)
        return int(number)
