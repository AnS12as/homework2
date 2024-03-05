from abc import ABC, abstractmethod

class ObjectCreationInfoMixin:
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, '{self.category}')"

class Category:
    total_categories = 0
    total_unique_products = set()

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)

    def get_products(self):
        products_info = ""
        for product in self.__products:
            products_info += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_info


class Product(ABC, ObjectCreationInfoMixin):
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
    def __init__(self, name, price, category, performance, model, memory, color, quantity):
        super().__init__(name, price, category)
        self.performance = performance
        self.model = model
        self.color = color
        self.memory = memory
        self.quantity = quantity


    def __str__(self):
        return f"{self.name} - ${self.price} - {self.category} - {self.model} - {self.color}"


class Grass(Product):
    def __init__(self, name, price, category, country_of_origin, germination_period, color, quantity):
        super().__init__(name, price, category)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.category} - {self.country_of_origin} - {self.color}"

class PurchaseInfo(ABC):
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @abstractmethod
    def display_info(self):
        pass

class Order(PurchaseInfo):
    def __init__(self, product, quantity):
        super().__init__(product, quantity)
        self.total_cost = product.price * quantity

    def display_info(self):
        return f"Order: {self.product.name}, Quantity: {self.quantity}, Total cost: ${self.total_cost}"



smartphone1 = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро", 5)
smartphone2 = Smartphone("Samsung Galaxy", 899, "Электроника", "Высокий", "S21", "128GB", "Черный", 3)
grass1 = Grass("Kentucky Bluegrass", 10, "Садоводство", "USA", "14 days", "Зеленый", 100)


print(str(smartphone1))
print(str(smartphone2))
print(str(grass1))

order1 = Order(smartphone1, 2)
print(order1.display_info())
