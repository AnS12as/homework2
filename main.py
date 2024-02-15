class Category:
    total_categories = 0
    total_unique_products = set()

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # делаем список приватным
        Category.total_categories += 1

    def add_product(self, product):
        self.__products.append(product)

    def get_products(self):
        products_info = ""
        for product in self.__products:
            products_info += f"{product}, 80 руб. Остаток: 15 шт.\n"

category = Category("Электроника", "Товары электроники")
category.add_product("Смартфон")
category.add_product("Ноутбук")
print(category.get_products())


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректная")
        else:
            if new_price < self.__price:
                confirm = input("Вы уверены, что хотите понизить цену? (y/n): ")
                if confirm.lower() == "y":
                    self.__price = new_price
                    print("Цена успешно понижена")
                else:
                    print("Действие отменено пользователем")
            else:
                self.__price = new_price



    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, product_list):
        for product in product_list:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        return cls(name, description, price, quantity)

products = []
product1 = Product.create_product("Смартфон", "Мощный смартфон", 500, 10, products)
products.append(product1)
product2 = Product.create_product("Ноутбук", "Легкий и компактный ноутбук", 800, 5, products)
products.append(product2)
product3 = Product.create_product("Смартфон", "Мощный смартфон", 600, 8, products)
if product3 not in products:
    products.append(product3)

product = Product("Смартфон", "Мощный смартфон", 500, 10)
print(product.price)
product.price = 600
print(product.price)
product.price = -100
print(product.price)
product.price = 400
print(product.price)