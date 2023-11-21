class Shop:
    cart = [] #cart is an class attribute
    def add_to_cart(self, item):
        self.cart.append(item)

isharak = Shop()
isharak.add_to_cart('Shoe')
isharak.add_to_cart('Mobile')

print(isharak.cart)

khandakar = Shop()
khandakar.add_to_cart('Wallet')
khandakar.add_to_cart('Head Phone')

print(khandakar.cart)