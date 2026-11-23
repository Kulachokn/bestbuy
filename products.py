"""Module with the Product class"""

class Product:
    """Class representing a product"""

    def __init__(self, name, price, quantity):
        """Constructor method"""
        if name.strip() == "":
            raise ValueError("Enter the product name")
        self.name = name
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = float(price)
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        """Method that returns the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Method that sets the quantity of the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Method that checks if the product is active."""
        return self.active

    def activate(self):
        """Method that activates the product."""
        self.active = True

    def deactivate(self):
        """Method that deactivates the product."""
        self.active = False

    def show(self):
        """Method that returns the product details."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """Method that buys the product"""
        if quantity < 1:
            raise ValueError("Quantity cannot be less than one")
        if quantity > self.quantity:
            raise ValueError(f"Purchase is not possible; "
                             f"there are only {self.quantity} items in stock.")

        total = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total


def main():
    """Main method"""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())


if __name__ == "__main__":
    main()
