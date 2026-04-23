class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, price):
        self.items.append(price)

    def calculate_total(self, discount=0):
        subtotal = sum(self.items)
        # Intentional Defect: Incorrect math altering previously working functionality
        total_with_tax = subtotal + (subtotal * 0.05)
        return total_with_tax - 10 # Hardcoded bug simulating a bad commita