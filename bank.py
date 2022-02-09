class BankAccount: 
    
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self




class User:

    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account = BankAccount(int_rate = 0.02, balance = 0 )
        

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name, self.account.balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw -= amount
        other_user.account.deposit += amount
        return self

Michael = User('Michael Stinko', 'mystink@email.stench')
Anna = User('Anna Banana', 'abanana@fruity.com')
Beef = User('Beef Testosterone', 'btest@meat.net')
Bonk = User('Bonk on the Head', 'bonk@bonk.bonk')



Michael.make_deposit(50).make_withdrawal(10).display_user_balance()