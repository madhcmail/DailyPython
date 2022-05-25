
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    # withdrawal method subtracts the amount from the balance
    def withdrawl(self, amount):
        self.balance= self.balance - amount  
    
    # deposit method adds the amount to the balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    
    # this method just returns the value of balance
    def getBalance(self):
        return self.balance

class savingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title,balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return(self.interestRate * self.getBalance())/100

acc_1= savingsAccount("Mark", 5000, 5) 
print("Balance= ", acc_1.balance)
print("Interest= ", acc_1.interestRate)
print(acc_1.getBalance())
acc_1.deposit(500)
print(acc_1.getBalance())
acc_1.withdrawl(1000)
print(acc_1.getBalance())
print(acc_1.interestAmount())
