"""
Task 35. Classes creation
"""
import datetime


class BankAccount:
    """According to the bank's terms, an account is opened for the client, provided that the initial
    deposit to the account is at least 100,000 US dollars"""

    date = datetime.datetime.utcnow()
    inflation_percentage = 7.5

    def __init__(self, name, balance=1000000):
        """Initializes the BankAccount class with the name and balance of the account holder.
        The default balance is 1000000."""
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Adds the amount to the balance of the account holder."""
        self.balance += amount
        return (f'Operation “Replenishment account” of the account owner\n'
                f'Account holder: {self.name}\nBalance: {self.balance}$\nDate of operation: {self.date}')

    def withdraw(self, amount):
        """Subtracts the amount from the balance of the account holder."""
        if amount > self.balance:
            return 'Insufficient funds for transaction!'
        self.balance -= amount
        return (f'Operation "Withdraw money" of the account owner\n'
                f'Account holder: {self.name}\nBalance: {self.balance}$\nDate of operation: {self.date}')

    @staticmethod
    def annual_percentage(balance, percentage: float or int):
        """Calculates the annual percentage of the account holder's balance."""
        return (f'Account balance: {balance}$\nAnnual percentage {percentage}%\n'
                f'Income: {(balance /100) * percentage}$\n'
                f'Balance after annual percentage: {balance + (balance / 100) * percentage}$\n')

    @classmethod
    def inflation(cls, new_inflation_percentage, percentage, balance):
        """Calculates the inflation of the account holder's balance at the end of the year"""
        cls.inflation_percentage = new_inflation_percentage
        if new_inflation_percentage > percentage:
            result_losses = ((percentage - new_inflation_percentage) / 100) * balance
            return (f'At the end of the year your losses: {round(result_losses, 2)}$\nYour start balance: {balance}$\n'
                    f'Balance after inflation: {balance + result_losses}$\n')
        else:
            result_income = ((percentage - new_inflation_percentage) / 100) * balance
            return (f'Your income at the end of the year: {round(result_income, 2)}$\nYour start balance: {balance}$\n'
                    f'Balance after inflation: {balance + result_income}$\n')

    def __str__(self):
        """Returns the account owner's name, balance, and account opening date.
        String representation of an object, focusing on readability"""
        return (f'Account holder: {self.name}\nBalance: {self.balance}$\n'
                f'Account opening date: {self.date}')


class BTCAccount(BankAccount):
    """The BTCAccount class is inherited from the BankAccount class.
    The BTCAccount class is designed"""

    btc_exchange_rate_buy = 69074.44
    btc_exchange_rate_sell = 69089.79

    def __init__(self, name, balance=1000000, btc=0):
        """Initializes the BTCAccount class with the name, balance, and number of bitcoins of the account holder.
        The default balance is 1000000, the default number of bitcoins is 0."""
        super().__init__(name, balance)
        self.btc = btc

    def buy_btc(self, btc_price):
        """The method calculates the cost of buying bitcoins and subtracts the amount from
        the balance of the account holder."""
        cost = self.btc * btc_price
        if cost > self.balance:
            return 'Insufficient funds for transaction!'
        self.balance -= cost
        return (f'Operation “Buy BTC” of the account owner\n'
                f'Account holder: {self.name}\nBalance: {self.balance}$\n'
                f'Number of bitcoins: {self.btc}\nDate of operation: {self.date}')

    def sell_btc(self, btc_price):
        """The method calculates the cost of selling bitcoins and adds the amount to the
        balance of the account holder."""
        cost = self.btc * btc_price
        self.balance += cost
        return (f'Operation “Sell BTC” of the account owner\n'
                f'Account holder: {self.name}\nBalance: {self.balance}$\n'
                f'Number of bitcoins: {self.btc}\nDate of operation: {self.date}')

    @staticmethod
    def btc_delta(volume_of_sales, volume_of_buy, period):
        """Bitcoin cumulative delta indicator for the month"""
        delta = round(volume_of_sales - volume_of_buy / period, 4)
        if delta > 0:
            return (f'Bitcoin cumulative delta indicator for the month: +{delta}\n'
                    f'The market is dominated by buyers')
        else:
            return (f'Bitcoin cumulative delta indicator for the month: {delta}\n'
                    f'The market is dominated by sellers')

    @classmethod
    def btc_change(cls, new_btc_exchange_rate_buy, new_btc_exchange_rate_sell, btc):
        """The method calculates the cost of buying and selling bitcoins and returns the difference
        at the changed bitcoin rate"""
        cls.btc_exchange_rate_buy = new_btc_exchange_rate_buy
        cls.btc_exchange_rate_sell = new_btc_exchange_rate_sell
        cost = btc * new_btc_exchange_rate_buy
        income = btc * new_btc_exchange_rate_sell
        return (f'Cost of buying {btc} bitcoins: {cost}$\nIncome from selling {btc} bitcoins: {income}$\n'
                f'Difference: {income - cost}$')

    def __str__(self):
        """Returns the account owner's name, balance, number of bitcoins, and account opening date.
        String representation of an object, focusing on readability"""
        return (f'Account holder: {self.name}\nBalance: {self.balance}$\n'
                f'Number of bitcoins: {self.btc}\nAccount opening date: {self.date}')


print('-------------------------Results Jane Doe-------------------------')
account = BankAccount('Jane Doe')
print(str(account))
print()
print(str(account.deposit(1000)))
print()
print(str(account.withdraw(500)))
print()
print(str(BankAccount.annual_percentage(100000, 6.5)))
print()
print(f'Old inflation percentage: {str(BankAccount.inflation_percentage)}')
print(str(BankAccount.inflation(13, 6.5, 100000)))
print('-------------------------Results John Doe-------------------------')
account = BankAccount('John Doe', 100000)
print(str(account))
print()
print(str(account.deposit(23000)))
print()
print(str(account.withdraw(1500)))
print()
print(str(BankAccount.annual_percentage(100000, 6.5)))
print()
print(f'Old inflation percentage: {str(BankAccount.inflation_percentage)}')
print(str(BankAccount.inflation(6.3, 8.4, 100000)))
print('-------------------------Results Nik Smith-------------------------')
btc_account = BTCAccount('Nik Smith', 1000000, 5)
print(str(btc_account))
print()
print(str(btc_account.buy_btc(69074.44)))
print()
print(str(btc_account.sell_btc(69089.79)))
print()
print(str(BTCAccount.btc_delta(1300000, 1700060, 30)))
print()
print(str(btc_account.btc_delta(1300000, 1700060, 30)))
print()
print(f'Old BTC exchange rate buy: {str(BTCAccount.btc_exchange_rate_buy)}')
print(f'Old BTC exchange rate sell: {str(BTCAccount.btc_exchange_rate_sell)}')
print(str(BTCAccount.btc_change(69079.45, 69099.45, 5)))
print()
print('-------------------------Results Samanta DuCaine-------------------------')
btc_account = BTCAccount('Samanta DuCaine', 2500000, 8)
print(str(btc_account))
print()
print(str(btc_account.buy_btc(69074.44)))
print()
print(str(btc_account.sell_btc(69089.79)))
print()
print(str(BTCAccount.btc_delta(1234000, 900060, 30)))
print()
print(str(btc_account.btc_delta(1234000, 900060, 30)))
print()
print(f'Old BTC exchange rate buy: {str(BTCAccount.btc_exchange_rate_buy)}')
print(f'Old BTC exchange rate sell: {str(BTCAccount.btc_exchange_rate_sell)}')
print(str(BTCAccount.btc_change(69079.45, 69099.45, 5)))
print()




