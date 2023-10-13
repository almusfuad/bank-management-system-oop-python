import random

class Bank:
    def __init__(bank, name, address) -> None:
        bank.name = name
        bank.address = address
        bank.init_balance = 1000000
        bank.users = {}
        bank.loan_enabled = True

    def create_acc(bank, user):
        account_num = random.randint(10000, 9999)  # Generate a 4-digit account number
        user.account_number = account_num
        user.balance = 0
        user.transaction_history = []
        user.load_count = 0
        bank.users[account_num] = user
        return account_num

    def delete_acc(bank, account_num):
        if account_num in bank.users:
            del bank.users[account_num]
            print(f'Account {account_num} has been deleted.')
        else:
            print('Account does not exist.')

    def all_users_acc(bank):
        for acc_num, user in bank.users.items():
            print(f'Account number: {acc_num}')

    def total_bank_balance(bank):
        return bank.init_balance

    def total_loan_amount(bank):
        total_loans = sum(user.balance for user in bank.users.values() if user.balance < 0)
        return abs(total_loans)

    def enable_loan_feature(bank):
        bank.loan_enabled = True

    def disable_loan_feature(bank):
        bank.loan_enabled = False