import random

class Bank:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.init_balance = 1000000
        self.users = {}
        self.loan_enabled = True

    def create_acc(self, name, email, address, acc_type):
        account_num = random.randint(10000, 9999)  # Generate a 4-digit account number
        user = {
            
        }