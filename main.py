"""User interface for the store"""

import products
import store

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def print_menu():
    """Print the main menu"""
    print("Store Menu")
    print("----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store_obj):
    """Print all active products with their numbers."""
    for number, product in enumerate(store_obj.get_all_products(), start=1):
        print(f"{number}. {product.show()}")


def show_total_amount(store_obj):
    """Show the total quantity of items in the store."""
    print(f"Total of {store_obj.get_total_quantity()} items in store")


def make_order(store_obj):
    """Ask user for products and amounts, then make the order."""
    active_products = store_obj.get_all_products()
    list_products(store_obj)
    print("When you want to finish order, enter empty line.")

    shopping_list = []
    while True:
        product_choice = input("Which product # do you want? ")
        if product_choice == "":
            break
        amount_choice = input("What amount do you want? ")

        if not product_choice.isdecimal() or not amount_choice.isdecimal():
            print("Error adding product!\n")
            continue

        product_number = int(product_choice)
        amount = int(amount_choice)
        if not 1 <= product_number <= len(active_products) or amount < 1:
            print("Error adding product!\n")
            continue

        product = active_products[product_number - 1]
        already_ordered = 0
        for listed_product, listed_amount in shopping_list:
            if listed_product is product:
                already_ordered += listed_amount
        if already_ordered + amount > product.get_quantity():
            print("Not enough items in stock!\n")
            continue

        shopping_list.append((product, amount))
        print("Product added to list!\n")

    if shopping_list:
        total = store_obj.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: {total} $")


def start(store_obj):
    """Show the menu repeatedly and run the chosen action."""
    while True:
        print_menu()
        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            show_total_amount(store_obj)
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 4.")


if __name__ == "__main__":
    start(best_buy)
