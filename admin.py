class Admin:
    def __init__(admin, bank) -> None:
        admin.bank = bank
        admin.__passkey = '1234'

    def create_acc(admin, user):
        return admin.bank.create_acc(user)

    def delete_acc(admin, account_num):
        admin.bank.delete_acc(account_num)

    def all_users_acc(admin):
        admin.bank.all_users_acc()

    def total_bank_balance(admin):
        print(f'Total bank balance is: {admin.bank.total_bank_balance()}')

    def total_loan_amount(admin):
        print(f'Total loan amount is: {admin.bank.total_loan_amount()}')

    def enable_loan_feature(admin):
        admin.bank.enable_loan_feature()

    def disable_loan_feature(admin):
        admin.bank.disable_loan_feature()

    def check_admin(admin, password):
        if password == admin.__passkey:
            return True
        return False

    def bankrupt(admin):
        print('Bankrupt is enabled.')
        return admin.bank.isBankrupt == True