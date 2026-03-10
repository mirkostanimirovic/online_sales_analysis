#main.py
from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager = ProductManager()

product1 = Product("Laptop", 1000, 5)
product2 = Product("Phone", 500, 10)
product3 = Product("Tablet", 300, 7)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

print("Products:")

manager.display_products()

manager.total_inventory_value()

cart = Cart()

random_products = random.sample(manager.products, 3)

for p in random_products:
    cart.add_to_cart(p)

cart.display_cart()

print("Total price:", cart.total_price())