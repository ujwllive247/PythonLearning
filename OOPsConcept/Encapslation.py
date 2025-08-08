


# Wrapping data into a single unit.....


class Bankdetails:
    def __init__(self,balance, AccountNo):
        self.balance= balance
        self.AccountNo = AccountNo


        # debit method...
    def debit(self,amount):
            self.balance -=amount
            print("Rs.",amount, "was Debited")
            print("total balance =",self.get_balance())




    def credit(self,amount):
            self.balance +=amount
            print("Rs.",amount, "was credited")
            print("total balance =", self.get_balance())

    def get_balance(self):
            return self.balance

            print("total balance =", self.get_balance())



Account1 = Bankdetails(100000,123466)

Withdrawal =Account1.debit(5200)

print(Withdrawal)



# class Bankdetails:
#     def __init__(self, balance, AccountNo):
#         self.balance = balance
#         self.AccountNo = AccountNo
#
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("Total balance =", self.get_balance())
#
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("Total balance =", self.get_balance())
#
#     def get_balance(self):
#         return self.balance
#
# Account1 = Bankdetails(10000, 123466)
#
# Account1.debit(1000)
