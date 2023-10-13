from bank import Bank, BankOperation
from admin import Admin
from user import User

def main():
    # creating bank
    fokira = Bank("Fokira Bank", 'Fokirpul, Bangladesh')
    bank_operations = BankOperation(fokira)

    # Creating admin
    admin = Admin(fokira)
    
    # creating users
    user1 = User('King Khan', 'Kingkhan@gmail.com', 'coxsbazar, Bangladesh', 'Savings')
    acc_num1 = fokira.create_acc(user1)
    user2 = User('Sakip Khan', 'sakip@gmail.com', 'Kuakata, Bangladesh', 'Current')
    acc_num2 = fokira.create_acc(user2)

if __name__ == "__main__":
    main()