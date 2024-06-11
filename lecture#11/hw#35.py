"""Task 35."""

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
        return f'Operation “Replenishment account” of the account owner\n' \
               f'Account holder: {self.name}\nBalance: {self.balance}$\nDate of operation: {self.date}'

    def withdraw(self, amount):
        """Subtracts the amount from the balance of the account holder."""
        if amount > self.balance:
            return 'Insufficient funds for transaction!'
        self.balance -= amount
        return f'Operation "Withdraw money" of the account owner\n' \
               f'Account holder: {self.name}\nBalance: {self.balance}$\nDate of operation: {self.date}'

    @staticmethod
    def annual_percentage(balance, percentage):
        """Calculates the annual percentage of the account holder's balance."""
        return f'Account balance: {balance}$\nAnnual percentage {percentage}%\n' \
               f'Income: {(balance /100) * percentage}$\n' \
               f'Balance after annual percentage: {balance + (balance / 100) * percentage}$\n'

    @classmethod
    def inflation(cls, new_inflation_percentage, percentage, balance):
        """Calculates the inflation of the account holder's balance at the end of the year"""
        cls.inflation_percentage = new_inflation_percentage
        if new_inflation_percentage > percentage:
            result_losses = ((percentage - new_inflation_percentage) / 100) * balance
            return f'If the inflation rate has increased during the current year since your deposit, then:\n' \
                   f'At the end of the year your losses: {round(result_losses, 2)}$\nYour start balance: {balance}$\n'\
                   f'Balance after inflation: {balance + result_losses}$\n'
        else:
            result_income = ((percentage - new_inflation_percentage) / 100) * balance
            return f'If the inflation rate at the time of expiration of 365 days from the date\n' \
                   f'of your deposit is lower than the inflation rate at the time you opened a \n' \
                   f'deposit account with our bank, then:\n' \
                   f'Your income at the end of the year: {round(result_income, 2)}$\nYour start balance: {balance}$\n' \
                   f'Balance after inflation: {balance + result_income}$\n'

    def __str__(self):
        """Returns the account owner's name, balance, and account opening date.
        String representation of an object, focusing on readability"""
        return f'Account holder: {self.name}\nBalance: {self.balance}$\n' \
               f'Account opening date: {self.date}'


class BTCAccount(BankAccount):
    """The BTCAccount class is inherited from the BankAccount class.
    The BTCAccount class is designed"""

    number_btc = 1
    btc_exchange_rate_buy = 69074.44
    btc_exchange_rate_sell = 69089.79

    def __init__(self, btc, name, balance=1000000):
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
        return f'Operation “Buy BTC” of the account owner\n' \
               f'Account holder: {self.name}\nNumber of bitcoins purchased: {self.btc}\n' \
               f'Price of one BTC: {btc_price}\nYour balance after purchase BTC: {self.balance}$\n' \
               f'Date of operation: {self.date}'

    def sell_btc(self, btc_price):
        """The method calculates the cost of selling bitcoins and adds the amount to the
        balance of the account holder."""
        cost = self.btc * btc_price
        self.balance += cost
        return f'Operation “Sell BTC” of the account owner\n' \
               f'Account holder: {self.name}\nNumber of bitcoins for sale: {self.btc}\n' \
               f'Price of one BTC: {btc_price}\nYour balance after sale BTC: {self.balance}$\n' \
               f'Date of operation: {self.date}'

    @staticmethod
    def btc_delta(bid, ask):
        """Bitcoin cumulative delta indicator for the one day"""
        cum_delta = bid - ask
        if cum_delta > 0:
            return f'Bitcoin cumulative delta indicator for the month V: +{cum_delta}\n' \
                   f'The market is dominated by buyers'
        else:
            return f'Bitcoin cumulative delta indicator for the month: {cum_delta}\n' \
                   f'The market is dominated by sellers'

    @classmethod
    def btc_change(cls, new_btc_exchange_rate_buy, new_btc_exchange_rate_sell, total_btc):
        """The method calculates the cost of buying and selling bitcoins and returns the difference
        at the changed bitcoin rate"""
        cls.number_btc = total_btc
        cls.btc_exchange_rate_buy = new_btc_exchange_rate_buy
        cls.btc_exchange_rate_sell = new_btc_exchange_rate_sell
        cost = total_btc * new_btc_exchange_rate_buy
        income = total_btc * new_btc_exchange_rate_sell
        return f'Cost of buying {total_btc} bitcoins: {cost}$\nIncome from selling {total_btc} bitcoins: {income}$\n' \
               f'Difference: {income - cost}$'

    def __str__(self):
        """Returns the account owner's name, balance, number of bitcoins, and account opening date.
        String representation of an object, focusing on readability"""
        return f'Account holder: {self.name}\nBalance: {self.balance}$\n' \
               f'Number of bitcoins: {self.btc}\nAccount opening date: {self.date}'


print('-------------------------Results Jane Doe-------------------------')
account = BankAccount('Jane Doe')
print(str(account))
print()
print(str(account.deposit(1000)))
print()
print(str(account.withdraw(500)))
print()
print(str(BankAccount.annual_percentage(100000, 6.5)))
print(str(account.annual_percentage(100000, 6.5)))
print()
print(str(BankAccount.inflation(13, 6.5, 100000)))
print('-------------------------Results Nik Smith-------------------------')
btc_account = BTCAccount(5, 'Nik Smith', 1000000)
print(str(btc_account))
print()
print(str(btc_account.buy_btc(69074.44)))
print()
print(str(btc_account.sell_btc(69089.79)))
print()
print(str(BTCAccount.btc_delta(1300000, 1700060)))
print(str(btc_account.btc_delta(1300000, 1700060)))
print()
print(f'Old BTC exchange rate buy: {str(BTCAccount.btc_exchange_rate_buy)}')
print(f'Old BTC exchange rate sell: {str(BTCAccount.btc_exchange_rate_sell)}')
print(str(BTCAccount.btc_change(69079.45, 69099.45, 5)))
print()




