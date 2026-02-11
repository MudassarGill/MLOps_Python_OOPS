#Here we make a bank mangment system where we cover all the topic that we cover in oop in python 
class Account:
    #class attribute
    bank_name='HBL'
    def __init__(self,name,balance):
        self.name = name   #instance attribute
        self.__balance = balance   #private attribute
    #instance method  show info
    def show():
        print(f'Name: {self.name}')
        print(f'Balance: {self.__balance}')
        print(f'Bank Name: {self.bank_name}')
    #getter method
    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")
    #setter method
    def set_balance(self,balance):
        self.__balance = balance
    def set_name(self,name):
        self.name = name
    #class method
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    #static method
    @staticmethod
    def get_bank_address():
        return "123 Main St, Karachi"


# Here we use polymorphism and inheritance
class Account:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")
    def deposit(self,amount):
        self.__balance += amount
        print("Deposit successful")
    def get_balance(self):
        return self.__balance
    def get_name(self):
        return self.name
    def set_balance(self,balance):
        self.__balance = balance
    def set_name(self,name):
        self.name = name
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    @staticmethod
    def get_bank_address():
        return "123 Main St, Karachi"
class SavingAccount(Account):
    def __init__(self,name,balance,interest_rate):
        super().__init__(name,balance)
        self.interest_rate = interest_rate
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")
    def deposit(self,amount):
        self.__balance += amount
        print("Deposit successful")
    def get_balance(self):
        return self.__balance
    def get_name(self):
        return self.name
    def set_balance(self,balance):
        self.__balance = balance
    def set_name(self,name):
        self.name = name
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    @staticmethod
    def get_bank_address():
        return "123 Main St, Karachi"
        
   #creating account
account = Account("Mudassar", 1000)
account.withdraw(100)
account.deposit(100)
account.get_balance()
account.get_name()
account.set_balance(100)
account.set_name("Mudassar")
account.get_bank_name()
account.get_bank_address()

   #creating saving account
saving_account = SavingAccount("Mudassar", 1000, 0.05)
saving_account.withdraw(100)
saving_account.deposit(100)
saving_account.get_balance()
saving_account.get_name()
saving_account.set_balance(100)
saving_account.set_name("Mudassar")
saving_account.get_bank_name()
saving_account.get_bank_address()