def cell():
    print('I have no cell phone')
    return 'No phone'
class Phone:
    price = 10398297049
    color = 'Black'
    brand = 'samsung'
    features = ['hammer', 'no heat', 'camera']
    def cell(self):
        print('No Phone now')
        return 'Dash Dash'
    def send_sms(self, phone, sms):
        text = f"sending a messege to: {phone} and the sms is: {sms}"
        return text
my_phone = Phone()
# print(my_phone.features)
# print(my_phone.cell())

result = my_phone.send_sms (4252, 'I forgot to miss you')
print(result)


# def hell():
#     print('Naim amr name')

# class hello:
#     def hell(self):
#         print('dudu khaw?')
#     price = 'nai ekdom'

# hel_1 = hello()
# print(hel_1.price)
# print(hel_1.hell())