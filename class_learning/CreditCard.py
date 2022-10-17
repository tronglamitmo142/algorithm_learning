class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instanceank
        customer: the name of customer
        bank: the name of bank
        acnt: the account identifier
        limit: credit limit (measured in dollars) """

        self._customer = customer
        self._bank = bank
        self._account = acnt 
        self._limit = limit
        self._balance = 0 
    
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True 
    
    def make_payment(self, amount):
        self._balance -= amount

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '2022 2102 1111 1111', 3500))
    wallet.append(CreditCard('Lam', 'California Federal', '2321 21321 1233 1111', 3500))
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)

