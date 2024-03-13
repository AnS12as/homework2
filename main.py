from abc import ABC, abstractmethod

class ObjectCreationInfoMixin:
    @property
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, '{self.category}')"

class Manageable(ABC):
    @abstractmethod
    def display_info(self):
        pass

class AbstractProduct(ABC, ObjectCreationInfoMixin):
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_category(self):
        pass

class Product(AbstractProduct):
    def get_description(self):
        return f"{self.name} - ${self.price} - {self.category}"

    def get_category(self):
        return self.category

class Category(Manageable):
    total_categories = 0
    total_unique_products = set()

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Can only add instances of Product or its subclasses")
        self.products.append(product)

    def get_products(self):
        products_info = ""
        for product in self.products:
            products_info += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_info

    def display_info(self):
        return f"Category '{self.name}': {self.description}."

class Smartphone(Product):
    def __init__(self, name, price, category, performance, model, memory, color, quantity):
        super().__init__(name, price, category)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        self.quantity = quantity

    def get_description(self):
        return f"{self.name} {self.model} - {self.memory}, {self.color}, Performance: {self.performance}"

    def get_category(self):
        return super().get_category()

class Grass(Product):
    def __init__(self, name, price, category, country_of_origin, germination_period, color, quantity):
        super().__init__(name, price, category)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color
        self.quantity = quantity

    def get_description(self):
        return f"{self.name} - ${self.price} - {self.category} - {self.country_of_origin} - {self.color}"

    def get_category(self):
        return super().get_category()

class Order(Manageable):
    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("Order can only add instances of Product")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        self.product = product
        self.quantity = quantity
        self.total_cost = self.product.price * quantity

    def display_info(self):
        return f"Order for '{self.product.name}' x {self.quantity} for ${self.total_cost}"


electronics = Category("Электроника", "Устройства и гаджеты")
garden = Category("Садоводство", "Товары для сада")

smartphone1 = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро", 5)
electronics.add_product(smartphone1)

grass1 = Grass("Kentucky Bluegrass", 10, "Садоводство", "США", "14 дней", "Зеленый", 100)
garden.add_product(grass1)

order1 = Order(smartphone1, 2)
print(order1.display_info())

order2 = Order(grass1, 50)
print(order2.display_info())

print(electronics.get_products())
print(garden.get_products())
