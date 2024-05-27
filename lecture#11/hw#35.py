"""
Task 35. Classes creation
"""
import datetime
from typing import Union


class BankAccount:
    """According to the bank's terms, an account is opened for the client, provided that the initial
    deposit to the account is at least 100,000 US dollars"""

    date = datetime.datetime.utcnow()
    inflation_percentage = 7.5

    def __init__(self, name, balance=1000):
        """Initializes the BankAccount class with the name and balance of the account holder.
        The default balance is 1000000."""
        self.name = name
        self.balance = balance

    def add_money_on_account(self, amount):
        """Adds the amount to the balance of the account holder."""
        self.balance += amount

    def add_money_account_info(self, amouth):
        """Returns information about the account holder's balance after adding money to the account."""
        self.add_money_on_account(amouth)
        return f'Operation "Add money on account" of the account owner\n' \
               f'Account holder: {self.name}\nBalance: {self.balance}$\nDate of operation: {self.date}\n'

    def withdraw_money_from_account(self, amount):
        """Subtracts the amount from the balance of the account holder."""
        self.balance -= amount

    def withdraw_money_account_info(self, amount):
        """Returns information about the account holder's balance after withdrawing money from the account."""
        self.withdraw_money_from_account(amount)
        if self.balance < 0:
            return 'Insufficient funds for transaction!\n'
        return f'Operation "Withdraw money from account" of the account owner\n' \
               f'Account holder: {self.name}\nBalance: {self.balance}$\nDate of operation: {self.date}\n'

    @staticmethod
    def annual_percentage(balance, percentage: Union[int, float]):
        """Calculates the annual percentage of the account holder's balance."""
        return f'Account balance: {balance}$\nAnnual percentage {percentage}%\n' \
               f'Income: {(balance /100) * percentage}$\n' \
               f'Balance after annual percentage: {balance + (balance / 100) * percentage}$\n'

    @classmethod
    def inflation(cls, new_inflation_percentage: Union[int, float], percentage: Union[int, float], balance):
        """Calculates the inflation of the account holder's balance at the end of the year"""
        cls.inflation_percentage = new_inflation_percentage
        if new_inflation_percentage > percentage:
            result_losses = ((percentage - new_inflation_percentage) / 100) * balance
            return f'Inflation rate has increased during the current year since your deposit, result be:\n' \
                   f'At the end of the year your losses: {round(result_losses, 2)}$\nYour start balance: {balance}$\n'\
                   f'Balance after inflation: {balance + result_losses}$\n'
        else:
            result_income = ((percentage - new_inflation_percentage) / 100) * balance
            return f'Inflation rate at the time of expiration of 365 days from the date\n' \
                   f'of your deposit is lower than the inflation rate at the time you opened a \n' \
                   f'deposit account with our bank, result be:\n' \
                   f'Your income at the end of the year: {round(result_income, 2)}$\nYour start balance: {balance}$\n' \
                   f'Balance after inflation: {balance + result_income}$\n'

    def __str__(self):
        """Returns the account owner's name, balance, and account opening date.
        String representation of an object, focusing on readability"""
        return f'Account holder: {self.name}\nBalance: {self.balance}$\n' \
               f'Account opening date: {self.date}\n'


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

    def buy_btc(self, btc_price: Union[int, float]):
        """The method calculates the cost of buying bitcoins and subtracts the amount from
        the balance of the account holder."""
        cost = self.btc * btc_price
        self.balance -= cost

    def buy_btc_info(self, btc_price: Union[int, float]):
        """Returns information about the account holder's balance after buying bitcoins."""
        self.buy_btc(btc_price)
        if self.balance < 0:
            return 'Insufficient funds for transaction!\n'
        return f'Operation “Buy BTC” of the account owner\n' \
               f'Account holder: {self.name}\nNumber of bitcoins purchased: {self.btc}\n' \
               f'Price of one BTC: {btc_price}$\nYour balance after purchase BTC: {self.balance}$\n' \
               f'Date of operation: {self.date}\n'

    def sell_btc(self, btc_price: Union[int, float]):
        """The method calculates the cost of selling bitcoins and adds the amount to the
        balance of the account holder."""
        cost = self.btc * btc_price
        self.balance += cost

    def sell_btc_info(self, btc_price: Union[int, float]):
        """Returns information about the account holder's balance after selling bitcoins."""
        self.sell_btc(btc_price)
        return f'Operation “Sell BTC” of the account owner\n' \
               f'Account holder: {self.name}\nNumber of bitcoins for sale: {self.btc}\n' \
               f'Price of one BTC: {btc_price}$\nYour balance after sale BTC: {self.balance}$\n' \
               f'Date of operation: {self.date}\n'

    @staticmethod
    def btc_delta(bid, ask):
        """Bitcoin cumulative delta indicator for the one day"""
        cum_delta = bid - ask
        if cum_delta > 0:
            return f'Bitcoin cumulative delta indicator for the month V: +{round(cum_delta, 4)}\n' \
                   f'The market is dominated by buyers\n'
        else:
            return f'Bitcoin cumulative delta indicator for the month: {round(cum_delta, 4)}\n' \
                   f'The market is dominated by sellers\n'

    @classmethod
    def btc_change(cls, new_btc_exchange_rate_buy: Union[int, float],
                   new_btc_exchange_rate_sell: Union[int, float], total_btc: int):
        """The method calculates the cost of buying and selling bitcoins and returns the difference
        at the changed bitcoin rate"""
        print(f'Old price BTC buy: {cls.btc_exchange_rate_buy}$ - New price BTC: {new_btc_exchange_rate_buy}$')
        print(f'Old price BTC sell: {cls.btc_exchange_rate_sell}$ - New price BTC: {new_btc_exchange_rate_sell}$')
        cls.number_btc = total_btc
        cls.btc_exchange_rate_buy = new_btc_exchange_rate_buy
        cls.btc_exchange_rate_sell = new_btc_exchange_rate_sell
        cost = total_btc * new_btc_exchange_rate_buy
        income = total_btc * new_btc_exchange_rate_sell
        return f'Cost of buying {total_btc} bitcoins at the new price: {round(cost, 4)}$\n' \
               f'Income from selling {total_btc} bitcoins at the new price: {round(income, 4)}$\n'

    def __str__(self):
        """Returns the account owner's name, balance, number of bitcoins, and account opening date.
        String representation of an object, focusing on readability"""
        return f'Account holder: {self.name}\nBalance: {self.balance}$\n' \
               f'Number of bitcoins: {self.btc}\nAccount opening date: {self.date}\n'


print('-------------------------Results BankAccount-------------------------')
user_bank = BankAccount('Jane Doe')
print(user_bank)
print(user_bank.add_money_account_info(500))
print(user_bank.withdraw_money_account_info(100))
print(user_bank.annual_percentage(1000, 7.5))
print(BankAccount.inflation(6.5, 7.5,
                            1000))
print('-------------------------Results BTCAccount-------------------------')
user = BTCAccount(21, 'John Doe')
print(user)
print(user.buy_btc_info(69074.44))
print(user.sell_btc_info(69089.79))
print(user.btc_delta(10734, 17564))
print(BTCAccount.btc_change(69075.44,
                            69090.79, 5))


