class Category:
    def __init__(self, name):
        self.__products = []
        self.name = name

    def add_product(self, product):
        self.__products.append(product)

    def __len__(self):
        return len(self.__products)

    def __iter__(self):
        return iter(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)}"


class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        total_price = self.price * self.quantity + other.price * other.quantity
        total_quantity = self.quantity + other.quantity
        return Product("Combined Product", total_price, total_quantity)
