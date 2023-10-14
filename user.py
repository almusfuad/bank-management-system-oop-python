class User:
    def __init__(user, name, email, address, acc_type) -> None:
        user.name = name
        user.email = email
        user.address = address
        user.acc_type = acc_type
        user.acc_num = None
        user.balance = 0
        user.transaction_history = []
        user.loan_count = 0
        user.loan_balance = 0

