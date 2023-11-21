class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 1000
        self.max_withdraw = 10000000
    
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount

    def get_balance(self):
        return(self.balance)
    
    def withdraw(self, amount):
        if self.min_withdraw > amount:
            print(f'Tumi Gorib, minimum withdrawal amount {self.min_withdraw}')
        elif self.max_withdraw < amount:
            print(f'Bank Gorib, Mximum withdrawal amount {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'here is your money {amount}')
            print(f'you balance after withdraw {self.balance}')

brac = Bank(10)
brac.deposite(5555000)
brac.withdraw(590876578696)
brac.withdraw(5000)

dbbl = Bank(5000)
dbbl.deposite(2000)
dbbl.deposite(2000)
print(dbbl.get_balance())