class Admin:
    def __init__(admin, bank) -> None:
        admin.bank = bank

    def create_acc(admin, user):
        return admin.bank.create_acc(user)

    def delete_acc(admin, account_num):
        admin.bank.delete_acc(account_num)

    def all_users_acc(admin):
        admin.bank.all_users_acc()

    def total_bank_balance(admin):
        return admin.total_bank_balance()

    def total_loan_amount(admin):
        return admin.bank.total_loan_amount()

    def enable_loan_feature(admin):
        admin.bank.enable_loan_feature()

    def disable_loan_feature(admin):
        admin.bank.disable_loan_feature()