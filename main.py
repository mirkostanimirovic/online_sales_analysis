#main.py
from product import Product
from product_manager import ProductManager


manager = ProductManager()

product1 = Product("Laptop", 1000, 5)
product2 = Product("Phone", 500, 10)
product3 = Product("Tablet", 300, 7)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

print("Products:")

