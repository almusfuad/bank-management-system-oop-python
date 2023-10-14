import random
from datetime import date

class Bank:
    def __init__(bank, name, address, balance) -> None:
        bank.name = name
        bank.address = address
        bank.__init_balance = balance
        bank.users = {}
        bank.loan_enabled = True

    def create_acc(bank, user):
        account_num = f'{date.today()}-{random.randint(1000, 9999)}'  # Generate a 4-digit account number
        user.account_number = account_num
        user.balance = 0
        user.transaction_history = []
        user.load_count = 0
        bank.users[account_num] = user
        print(f'Account number: {account_num} is created successfully')
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
        total_balance = bank.__init_balance
        for user in bank.users.values():
            total_balance += user.balance
        return total_balance

    def total_loan_amount(bank):
        total_loans = 0
        for user in bank.users.values():
            total_loans += user.loan_balance
            bank.total_balance -= total_loans
        return total_loans
        

    def enable_loan_feature(bank):
        bank.loan_enabled = True
        if bank.loan_enabled:
            print('Loan features is ON')

    def disable_loan_feature(bank):
        bank.loan_enabled = False
        if bank.loan_enabled == False:
            print('Loan features is OFF')


# This class is for banking operation like deposit, withdraw, loaning, transferring
class BankOperation:
    def __init__(bank_op, bank) -> None:
        bank_op.bank = bank

    def deposit(bank_op, account_num, amount):
        if account_num in bank_op.bank.users:
            user = bank_op.bank.users[account_num]
            if amount > 100:
                user.balance += amount
                user.transaction_history.append(f'Deposit: {amount}')
                print(f'Deposited {amount} into account {account_num}')
            else:
                print("Invalid deposit amount")
        else:
            print('Account does not exist.')

    def withdraw(bank_op, account_num, amount):
        if account_num in bank_op.bank.users:
            user = bank_op.bank.users[account_num]
            if amount > 100 and user.balance >= amount:
                user.balance -= amount
                user.transaction_history.append(f'Withdraw: -{amount}')
                print(f'withdrawn {amount} from account {account_num}')
            elif amount > 100 and user.balance < amount:
                print('Withdrawal amount exceeded.')
            else:
                print('Minimum withdrawal amount is 100')
        else:
            print('Account does not exist.')

    def take_loan(bank_op, account_num, amount):
        if account_num in bank_op.bank.users:
            user = bank_op.bank.users[account_num]
            if user.loan_count < 3 and bank_op.bank.loan_enabled:
                if amount > 100:
                    user.balance += amount
                    user.transaction_history.append(f'Loan: +{amount}')
                    user.loan_count += 1
                    print(f'Loan of {amount} credited to account {account_num}.')
                else:
                    print('Minimum Loan amount is 100')
            else:
                print('Loan feature is disabled or maximum loan limit exceeded.')
        else:
            print('Account does not exist.')

    def transfer_amount(bank_op, sender_acc_num, receiver_acc_num, amount):
        if sender_acc_num in bank_op.bank.users and receiver_acc_num in bank_op.bank.users:
            sender = bank_op.bank.users[sender_acc_num]
            receiver = bank_op.bank.users[receiver_acc_num]
            if amount > 100 and sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                sender.transaction_history.append(f'Transfer: -{amount} to {receiver_acc_num}')
                receiver.transaction_history.append(f'Transfer: +{amount} from {sender_acc_num}')
                print(f'Transferred {amount} from account {sender_acc_num} to account {receiver_acc_num}')
            elif amount > 100 and sender.balance < amount:
                print('Insufficient balance for the transfer')
            else:
                print('Minimum amount for transfer is 100')
        else:
            print('One or both accounts do not exist.')

    def check_available_balance(bank_op, account_num):
        if account_num in bank_op.bank.users:
            user = bank_op.bank.users[account_num]
            print(f'{user.balance}')
        else:
            return 'Account does not exist'

    def check_transaction_history(bank_op, account_num):
        if account_num in bank_op.bank.users:
            user = bank_op.bank.users[account_num]
            for _ in user.transaction_history:
                print(f'{_}')
        else:
            print('Account does not exist')