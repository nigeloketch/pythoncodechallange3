# main.py

# This is the main program file for the shopping cart application.
# It imports classes and functions from other files and interacts with the user.

# Import the ShoppingCart class from shopping_cart.py
from shopping_cart import ShoppingCart

# Create a new shopping cart
cart = ShoppingCart()

# Display a welcome message
print("Welcome to the Shopping Cart App!")

# Offer a menu to the user
while True:
    print("\nMenu:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        cart.add_item(item_name, item_price)
        print(f"{item_name} added to the cart.")

    elif choice == "2":
        item_name = input("Enter item name to remove: ")
        cart.remove_item(item_name)
        print(f"{item_name} removed from the cart.")

    elif choice == "3":
        cart.view_cart()

    elif choice == "4":
        total_cost = cart.checkout()
        print(f"Total cost: ${total_cost:.2f}")
        break

    elif choice == "5":
        print("Thank you for using the Shopping Cart App!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
