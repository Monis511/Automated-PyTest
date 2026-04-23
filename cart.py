class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, price):
        self.items.append(price)

    def calculate_total(self, discount=0):
        if not self.items:
            return 0 # Fixes the -10.0 == 0 error
        subtotal = sum(self.items) - discount
        # Correct logic: Apply 5% tax to the discounted subtotal
        return subtotal + (subtotal * 0.05)