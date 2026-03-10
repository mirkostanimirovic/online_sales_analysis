#cart.py
class Cart:

    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def display_cart(self):
        print("Cart contents:")
        for product in self.cart_items:
            print(product.name, product.price)

    def total_price(self):
        total = 0

        for product in self.cart_items:
            total += product.price

        return total