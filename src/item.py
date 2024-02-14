import csv
import os


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = 'Файл item.csv поврежден'


class FileNotFoundError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = 'Отсутствует файл item.csv'


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
        """
        Вывод класса, названия товара,
        а также его цены и кол-ва
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Вывод названия товара с помощью метода str
        """
        return f"{self.__name}"

    @property
    def name(self):
        """
        Приват отрибута name
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Прверка длинны наименования товара,
        чтобы было не более 10 символов.
        """
        self.__name = new_name[:10]

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
    def instantiate_from_csv(cls):
        """
        Добавление экземпляра класса из csv файла.
        """
        if not os.path.join(os.path.dirname(__file__), 'item.csv'):
            raise FileNotFoundError('Отсутствует файл item.csv')
        else:
            cls.all.clear()
        path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(path, 'r', newline="\n") as csv_file:
            reader = csv.DictReader(csv_file)
            items = list(reader)
            for item in items:
                if item['name'] not in items or item['price'] not in items or item['quantity'] not in items:
                    raise InstantiateCSVError('Файл item.csv поврежден')
                else:
                    print(cls(name=item.get('name'),
                              price=item.get('price'),
                              quantity=item.get('quantity')))

    @staticmethod
    def string_to_number(str_number):
        """
        Возвращает число из числа-строки.
        """
        number = float(str_number)
        return int(number)

    def __add__(self, other):
        """
        Магический метод, который позволяет прибавлять к экземпляру класса объект произвольного типа данных
        :param other: Принимает остаток товара Phone и складывает с общим остатком товара в магазине
        :return: Выводит общие колличество
        """
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        raise TypeError("Складывать можно только объекты классов с родительским классом Item")
