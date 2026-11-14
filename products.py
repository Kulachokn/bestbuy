class Product:
    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Enter the product name")
        self.name = name
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = float(price)
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity < 1:
            raise ValueError("Quantity cannot be less than one")
        if quantity > self.quantity:
            raise ValueError(f"Purchase is not possible; there are only {self.quantity} items in stock.")

        total = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()