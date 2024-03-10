from abc import ABC, abstractmethod

class ObjectCreationInfoMixin:
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}', '{self.category}')"

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

    def get_category(self):
        return self.category

class Product(AbstractProduct):
    def get_description(self):
        return f"{self.name} - ${self.price} - {self.category}"

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
        return f"Category '{self.name}' info displayed."

class Grass(Product):
    def __init__(self, name, price, category, country_of_origin, germination_period, color, quantity):
        super().__init__(name, price, category)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color
        self.quantity = quantity

    def get_description(self):
        return f"{self.name} - ${self.price} - {self.category} - {self.country_of_origin} - {self.color}"

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
        return f"Order for '{self.product.name}' info displayed."


electronics = Category("Electronics", "Electronic devices")
lawn = Category("Gardening", "Lawn products")

grass1 = Grass("Kentucky Bluegrass", 10, "Gardening", "USA", "14 days", "Green", 50)
lawn.add_product(grass1)

order = Order(grass1, 5)

print(electronics.get_products())
print(lawn.get_products())
print(order.display_info())
