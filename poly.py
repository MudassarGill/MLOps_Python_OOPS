# Here we cover all the topic about polymorphism
class payment:
    def __init__(self,amount):
        self.amount = amount
    def pay(self):
        print("Payment successful")
class CreditCard(payment):
    def __init__(self,amount,credit_card_number):
        super().__init__(amount)
        self.credit_card_number = credit_card_number
    def pay(self):
        print("Payment successful")
class DebitCard(payment):
    def __init__(self,amount,debit_card_number):
        super().__init__(amount)
        self.debit_card_number = debit_card_number
    def pay(self):
        print("Payment successful")
obj = CreditCard(1000, "1234567890123456")
obj.pay()
obj = DebitCard(1000, "1234567890123456")
obj.pay()