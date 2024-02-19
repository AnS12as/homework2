import pytest


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.category}"

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can't add {type(other)} to {self.__class__}")
        total_price = self.price + other.price
        return f"Total price: ${total_price}"


class Smartphone(Product):
    def __init__(self, name, price, category, performance, model, memory, color):
        super().__init__(name, price, category)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class Grass(Product):
    def __init__(self, name, price, category, country_of_origin, germination_period, color):
        super().__init__(name, price, category)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color


def test_add_same_type():
    smartphone1 = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро")
    smartphone2 = Smartphone("Samsung Galaxy", 899, "Электроника", "Высокий", "S21", "128GB", "Черный")
    assert smartphone1 + smartphone2 == "Total price: $1898"


def test_add_different_types():
    smartphone = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро")
    grass = Grass("Kentucky Bluegrass", 10, "Садоводство", "USA", "14 days", "Зеленый")
    with pytest.raises(TypeError):
        smartphone + grass

    with pytest.raises(TypeError):
        grass + smartphone


if __name__ == "__main__":
    test_add_same_type()
    test_add_different_types()
    print("Все тесты пройдены!")
