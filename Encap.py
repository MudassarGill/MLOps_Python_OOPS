# Here we cover encapsulation 
# Encapuslation use for data hiding,and secure our data
class Bank:
    def __init__(self,name,balance):
        self.__name = name
        self.__balance = balance
obj=Bank("Mudassar", 1000)
try:
    print(obj.__name)
    print('You can access the data')
except Exception as e:
    print(e)
    print('You can not access the data')
    print('\n')
print(obj._Bank__balance)
print('You can access the data')


# now we make an ATM machine and also we use Encapsulation here
class ATM_Machine:
    def __init__(self,name,balance,withdraw,deposit):
        self.name = name
        self.__balance = balance
        self.withdraw = withdraw
        self.__deposit = deposit
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")
    def deposit(self):
        self.__balance += self.__deposit
        print("Deposit successful")
    def get_balance(self):
        return self.__balance
    def get_name(self):
        return self.name
    def get_withdraw(self):
        return self.withdraw
    def get_deposit(self):
        return self.deposit

obj = ATM_Machine("Mudassar", 10000)
print(obj.get_balance())
print(obj.get_name())
obj.set_balance(2000)
obj.set_name("Mudassar Ali")
print(obj.get_balance())
print(obj.get_name())