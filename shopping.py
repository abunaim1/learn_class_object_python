class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        product = {'item' : item, 'price' : price, 'quantity' : quantity}
        self.cart.append(product)
    
    def remove_item(self, item):
        for x in self.cart:
            if x['item'] == item:
                print(f'Removing the {item}')
                self.cart.remove(x)
                break
            else:
                print("This item is not include your cart")


    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('Total Price:', total)
        if total > amount:
            print(f'Provide more, {total - amount} money' )
        elif total < amount:
            print(f'Your changes {amount - total}, Thank you')
        else:
            print('Thank you, sir')


naim = Shopping('Naim')
naim.add_to_cart('shampoo', 200, 2)
naim.add_to_cart('cream', 30, 4)
naim.add_to_cart('dim', 20, 3)

print(naim.cart)
naim.checkout(10000)

naim.remove_item('shampoo')
print(naim.cart)