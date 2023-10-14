from bank import Bank, BankOperation
from admin import Admin
from user import User

def main():
    # creating bank
    bank = Bank("Fokira Bank", 'Fokirpul, Bangladesh', -5000)
    bank_operations = BankOperation(bank)

    # Creating admin
    admin = Admin(bank)

    account_type = {
        1: 'savings',
        2: 'current',
    }

    print(f'1. User\n2. Admin\nEnter Option: ', end= "")
    choice = int(input())
    resume = True
    if choice == 1:
        while resume:
            print('\n')
            print(f'1. Create account \n2. Deposit Amount \n3. Withdraw amount \n4. Check Available Balance')
            print(f'5. Check transaction history \n6. Take Loan \n7. Transfer amount \n8. EXIT')
            print(f'Choose an option: ', end='')
            userChoice = int(input())
            if userChoice == 1:
                print('Enter your name: ', end= "")
                name = str(input())
                print('Enter your email: ', end= "")
                email = str(input())
                print('Enter your address: ', end= '')
                address = str(input())
                print('1. Savings \n2. Current \nChoose account type: ', end='')
                account_Op = int(input())
                user_num = bank.create_acc(User(name, email, address, account_type[account_Op]))
                print(f'Your account number is: {user_num}')
            elif userChoice == 2:
                print('Enter account number: ', end="")
                acc_num = str(input())
                print('Enter amount to deposit: ', end='')
                amount = int(input())
                bank_operations.deposit(acc_num, amount)
            elif userChoice == 3:
                print('Enter account number: ', end="")
                acc_num = str(input())
                print('Enter amount to withdraw: ', end='')
                amount = int(input())
                bank_operations.withdraw(acc_num, amount)
            elif userChoice == 4:
                print('Enter account number: ', end="")
                acc_num = str(input())
                bank_operations.check_available_balance(acc_num)
            elif userChoice == 5:
                print('Enter account number: ', end="")
                acc_num = str(input())
                bank_operations.check_transaction_history(acc_num)
            elif userChoice == 6:
                print('Enter account number: ', end="")
                acc_num = str(input())
                print('Enter amount for loan: ', end='')
                amount = int(input())
                bank_operations.take_loan(acc_num, amount)
            elif userChoice == 7:
                print('Enter sender account number: ', end="")
                sender_acc_num = str(input())
                print('Enter receiver account number: ', end="")
                receiver_acc_num = str(input())
                print('Enter amount to send: ', end='')
                amount = int(input())
                bank_operations.transfer_amount(sender_acc_num, receiver_acc_num, amount)
            elif userChoice == 8:
                resume = False
    elif choice == 2:
        print('Enter your password: ', end='')
        password = str(input())
        if admin.check_admin(password) == False:
            print('Credential does not match.')
        else:
            while resume:
                print('\n')
                print(f'1. Create an user \n2. Delete an user \n3. All user List \n4. Check bank balance \n5. Check total loan amount \n6. Loan features ON/OFF \n7. EXIT')
                print(f'Choose an option: ', end='')
                adminChoise = int(input())
                if adminChoise == 1:
                    print('Enter user name: ', end= "")
                    name = str(input())
                    print('Enter user email: ', end= "")
                    email = str(input())
                    print('Enter user address: ', end= '')
                    address = str(input())
                    print('1. Savings \n2. Current \nChoose account type: ', end='')
                    account_Op = int(input())
                    bank.create_acc(User(name, email, address, account_type[account_Op]))
                elif adminChoise == 2:
                    print('Enter account number: ', end="")
                    acc_num = str(input())
                    admin.delete_acc(acc_num)
                elif adminChoise == 3:
                    admin.all_users_acc()
                elif adminChoise == 4:
                    admin.total_bank_balance()
                elif adminChoise == 5:
                    admin.total_loan_amount()
                elif adminChoise == 6:
                    print(f'1. Enable bank loan \n2. Disable bank loan')
                    print(f'Choose an option: ', end='')
                    loan_op = int(input())
                    if loan_op == 1:
                        admin.enable_loan_feature()
                    elif loan_op == 2:
                        admin.disable_loan_feature()
                elif adminChoise == 7:
                    resume = False


if __name__ == "__main__":
    main()