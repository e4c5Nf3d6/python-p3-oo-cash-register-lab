#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)
        self.total += price * quantity
        self.last_transaction = {"title": title, "price": price, "quantity": quantity}
    
    def apply_discount(self):
        if self.discount:
            self.total -= self.total * self.discount / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.items = self.items[: len(self.items) - self.last_transaction["quantity"]]
        self.total -= self.last_transaction['price'] * self.last_transaction['quantity']

