class Pen:
    manufactured = 'Chaina'

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def send_sms(self, no, sms):
        text = f'sending sms to {no} and the sms is {sms}' 
        print(text)

pen1 = Pen('Matador', 10, 'Black')
print(pen1.brand, pen1.color, pen1.price, pen1.manufactured)
pen2 = Pen('All Time', 5, 'Red')
print(pen2.brand, pen2.color, pen2.price, pen2.manufactured)
pen3 = Pen('Nokia', 2, 'White')
print(pen3.brand, pen3.color, pen3.price, pen3.manufactured)
