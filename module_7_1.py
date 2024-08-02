from pprint import pprint

print()     # Отступ


# Необходимо реализовать 2 класса Product и Shop,
# с помощью которых будет производиться запись в файл с продуктами.

# Объекты класса Product будут создаваться следующим образом -

# Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return str(products)

    def add(self, *products):
        file = open(self.__file_name, 'a')
        current_products = self.get_products()
        for product in products:
            if product.name not in current_products:
                file.write(str(product) + '\n')
                current_products += product.name + '\n'
            else:
                print(f"Продукт {product.name} уже есть в магазине")

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

