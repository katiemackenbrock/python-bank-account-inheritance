class BankAccount():
  def __init__(self):
    self.balance = 0
    # balance = 0
    self.interest_rate = 0.2
    # interest_rate = 0.2

  def deposit(self, number):
    if number > 0:
      self.balance = self.balance + number
    else:
      return False
    # self.balance += number
    # return self.balance

  def withdraw(self, number):
    if number < 0:
      return False
    self.balance -= number
    return number

  def accumulate_interest(self):
    # if self.balance < 0:
    self.balance += (self.balance * self.interest_rate)
    return self.balance

class ChildrensAccount(BankAccount):
  def __init__(self):
    BankAccount.__init__(self)
    self.interest_rate = 0
    self.balance = 0

  def accumulate_interest(self):
    self.balance += 10
    return self.balance

class OverdraftAccount(BankAccount):
  def __init__(self):
    BankAccount.__init__(self)
    self.overdraft_penalty = 40

  def withdraw(self, number):
    if (number < 0 or number < self.balance):
      return False
    self.balance -= self.overdraft_penalty
    return self.balance

  def accumulate_interest(self):
    if (self.balance > 0):
      self.balance += (self.balance * self.interest_rate)
      return self.balance


basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()


childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()


overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
