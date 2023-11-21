class Shop:
    
    # shopping_mall = 'jamuna'
    
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []
    
    def add_to_cart(self, item):
        self.cart.append(item)


khandaker = Shop('Khandaker Golam Rabbi ')
khandaker.add_to_cart('Mobile')
khandaker.add_to_cart('Razor')
khandaker.add_to_cart('Balti')
print(khandaker.cart)

rasel = Shop('Rasel uddin a')
rasel.add_to_cart('Chair')
rasel.add_to_cart('Hariken')
rasel.add_to_cart('Table')
print(rasel.cart)