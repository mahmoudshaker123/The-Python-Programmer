# Exercise 15_03 - Thread-Safe Bank Account
# You are given a simple bank account class that supports deposit
# and withdraw operations.
# Modify the class to make it thread-safe so that it can handle
# concurrent deposits and withdrawals correctly.


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance = new_balance

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            self.balance = new_balance
        else:
            raise ValueError("Insufficient funds")


account = BankAccount()
account.deposit(100)
account.withdraw(50)
print(account.balance)
