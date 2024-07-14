class Bankacc:
    def __init__(self,acc_number,acc_holder,balance=0.0):
        self.acc_number=acc_number
        self.acc_holder=acc_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited Rs {amount}. Updated balance is Rs {self.balance}.")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs {amount}. New balance is Rs {self.balance}.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

account1 = Bankacc("5678", "Baibhabi", 10000)
account1.deposit(2000)
account1.withdraw(200)
print("Current balance: Rs", account1.get_balance())