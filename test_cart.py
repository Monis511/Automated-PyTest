import pytest
from cart import ShoppingCart

def test_calculate_total_with_tax():
    cart = ShoppingCart()
    cart.add_item(100)
    cart.add_item(50)
    assert cart.calculate_total() == 157.5

# New test for edge case: Empty cart
def test_empty_cart():
    cart = ShoppingCart()
    assert cart.calculate_total() == 0

# New test for newly introduced logic: Discounts
def test_calculate_total_with_discount():
    cart = ShoppingCart()
    cart.add_item(100)
    assert cart.calculate_total(discount=20) == 84.0 # (100 - 20) + 5% tax