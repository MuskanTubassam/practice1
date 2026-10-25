class InsufficientFundsError(Exception):
  pass

class BankAccount:

  def __init__(self, owner, balance = 0):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if amount > self.balance:
      raise InsufficientFundsError(f"cannot withdraw {amount}, balance is {self.balance}")
    self.balance -= amount
account = BankAccount("Ali", 1000)

account.deposit(500)
account.withdraw(300)

print(account.balance)

try:
    account.withdraw(5000)
except InsufficientFundsError as e:
    print(f"Error: {e}")