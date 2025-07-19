class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.acc = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


cust1 = Account(1000, 23)
cust1.debit(2000)
cust1.credit(3000)