from src.item import Item


class Phone(Item):
    """
    Унаследованный класс от 'Item',
    с новым товаром и новым атрибутом
    """

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """
        Возвращает количество SIM-карт.
        :return: количество SIM-карт
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, testing_data):
        if int(testing_data) >= 0:
            self.__number_of_sim = int(testing_data)
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса в режиме отладки
        :return: Выводит строку с названием товара, ценой, колличеством и колличеством сим карт
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self) -> str:
        """
        Выводит название товара
        """
        return f'{self.name}'
