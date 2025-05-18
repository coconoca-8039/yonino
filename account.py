import time

def create_account(func):
    def inner(self, *args, **kwargs):
        name = kwargs.get("name", "Unknown")  # 安全に取り出す
        print("")
        print("+----------------------------+")
        print(f"| Creating Account: {name:<10} |")
        result = func(self, *args, **kwargs)
        print(f"| Account No: {self.account_number:<16} |")
        print("+----------------------------+")
        print("")
        return result
    return inner

class Account:

    count = 0

    @create_account
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.transaction_history = []
        Account.count += 1
    
    def withdraw(self, price):
        tmp = self.balance
        if price <= self.balance:
            self.balance -= price
            print(f"   withdraw: {tmp} -> {self.balance}")
            self.add_transaction(-price)
        else:
            print("   You cannot withdraw")
        
    
    def deposit(self, price):
        tmp = self.balance
        self.balance += price
        self.add_transaction(price)
        print(f"   deposit: {tmp} -> {self.balance}")
    
    def show_balance(self):
        #print(f"Number {self.account_number} {self.name}'s balance is {self.balance}")
        pass

    def add_transaction(self, price):
        transaction = {
            'withdraw/deposit': price,
            'new_balance': self.balance,
            'time': Account.get_time_str()
        }
        self.transaction_history.append(transaction)
    
    @staticmethod
    def get_time_str(): 
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d-%H-%M")
    
    def show_transaction_history(self):
         print("")
         for transaction in self.transaction_history:
            transaction_str_list = []
            for k, v  in transaction.items():
                transaction_str_list.append(f"{k}: {v}")
            print(", ".join(transaction_str_list))

myaccount = Account(name = "my account", balance = 1000)
myaccount.withdraw(100)
myaccount.deposit(100)
myaccount.show_balance()
#print(myaccount.transaction_history)
print(Account.get_time_str())
myaccount.show_transaction_history()
# youraccount = Account(name = "your account", balance = 10000)
# youraccount.withdraw(100)
# youraccount.deposit(100)
# youraccount.show_balance()