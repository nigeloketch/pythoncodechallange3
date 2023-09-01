# shopping_cart.py

# This file contains the ShoppingCart class, which represents a shopping cart.

class ShoppingCart:
    def __init__(self):
        # Initialize an empty cart as a dictionary
        self.cart = {}

    def add_item(self, item_name, item_price):
        # Add an item to the cart
        if item_name in self.cart:
            self.cart[item_name] += item_price
        else:
            self.cart[item_name] = item_price

    def remove_item(self, item_name):
        # Remove an item from the cart
        if item_name in self.cart:
            del self.cart[item_name]
        else:
            print(f"{item_name} is not in the cart.")

    def view_cart(self):
        # View the items in the cart
        print("\nItems in Cart:")
        for item_name, item_price in self.cart.items():
            print(f"{item_name}: ${item_price:.2f}")

    def checkout(self):
        # Calculate and return the total cost of items in the cart
        total_cost = sum(self.cart.values())
        return total_cost
