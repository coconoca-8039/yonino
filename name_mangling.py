class Account:

    def __init__(self, _balance):
        self.__balance = _balance
    
    def deposit(self, price):
        self.__balance += price
        self.show_balance()
    
    def withdraw(self, price):
        if self.__balance < price:
            print("Insufficient _balance")
        else:
            self.__balance -= price
            self.show_balance()
    
    def show_balance(self):
        print(f"The balance is {self.__balance} yen")

myaccount = Account(10000)
myaccount.deposit(1000)
myaccount.withdraw(3000)