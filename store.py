"""Module with the Store class"""

from typing import List
import products


class Store:
    """Class to store the products"""
    def __init__(self, product_list=None):
        """Constructor method"""
        if product_list is None:
            product_list = []
        self.products = product_list

    def add_product(self, product):
        """Method to add a product to a store."""
        self.products.append(product)

    def remove_product(self, product):
        """Method to remove a product from a store."""
        if product not in self.products:
            raise ValueError("Product is not in the store")
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Method to return the total amount in the store."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[products.Product]:
        """Method to return all the products in the store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """Method to order all items from a shopping list.

        Checks every item first, so nothing is bought if any item is invalid.
        """

        for product, quantity in shopping_list:
            if quantity < 1:
                raise ValueError("Quantity cannot be less than one")
            if quantity > product.get_quantity():
                raise ValueError(
                    f"Purchase is not possible; there are only "
                    f"{product.get_quantity()} items of {product.name} in stock."
                )

        total = 0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total


def main():
    """Main method"""
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()
