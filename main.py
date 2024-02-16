class Category:
    def __init__(self, name):
        self.__products = []
        self.name = name

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return self.__products

    def get_products_info(self):
        products_info = ""
        for product in self.__products:
            products_info += f"{product.name}, {product.price} руб. Остаток: {product.stock} шт.\n"
        return products_info



class Product:
    def __init__(self, name: str, price: str, stock: int):
        self.name = name
        self.__price = price
        self.stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Ошибка: Цена должна быть больше нуля.")
            return
        elif new_price < self.__price:
            confirmation = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if confirmation.lower() != 'y':
                print("Действие отменено.")
                return

            self.__price = new_price

    @classmethod
    def create_product(cls, name, price, stock, product_list):
        for existing_product in product_list:
            if existing_product.name == name:
                existing_product.stock += stock
                existing_product.price = max(existing_product.price, price)
                return existing_product
            return cls(name, price, stock)


product = Product("Laptop", 1000, 10)
print(product.price)
product.price = 900
product.price = 1000
