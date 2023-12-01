class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return 'Insufficient funds'

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def execute_transaction(self):
        if self.sender.balance >= self.amount:
            self.sender.withdraw(self.amount)
            self.receiver.deposit(self.amount)
            return True
        else:
            return False

def create_account(name, initial_deposit):
    return Account(name, initial_deposit)

def transfer_funds(sender, receiver, amount):
    transaction = Transaction(sender, receiver, amount)
    return transaction.execute_transaction()

def check_balance(account):
    return account.balance

def update_owner(account, new_owner):
    account.owner = new_owner
    return account.owner

def log_transaction(transaction, log_file='transaction_log.txt'):
    with open(log_file, 'a') as file:
        file.write(f'Transaction: {transaction.sender.owner} to {transaction.receiver.owner}, Amount: {transaction.amount}\\n')

# TODO: Implement the 'freeze_account' function
def freeze_account(account):
    # This function should take an Account object as input and change its status to frozen, preventing any withdrawals or deposits.
    # It should return True if the account was successfully frozen, or False if the account was already frozen.
    # Expected Input: account (Account object)
    # Expected Output: True (if successfully frozen) or False (if already frozen)
    pass