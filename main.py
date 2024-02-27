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
        self.color = color
        self.memory = memory

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.category} - {self.model} - {self.color}"


class Grass(Product):
    def __init__(self, name, price, category, country_of_origin, germination_period, color):
        super().__init__(name, price, category)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.category} - {self.country_of_origin} - {self.color}"


smartphone1 = Smartphone("iPhone", 999, "Электроника", "Высокий", "12 Pro", "256GB", "Серебро")
smartphone2 = Smartphone("Samsung Galaxy", 899, "Электроника", "Высокий", "S21", "128GB", "Черный")
grass1 = Grass("Kentucky Bluegrass", 10, "Садоводство", "USA", "14 days", "Зеленый")

print(smartphone1 + smartphone2)
try:
    print(smartphone1 + grass1)
except TypeError as e:
    print(e)
