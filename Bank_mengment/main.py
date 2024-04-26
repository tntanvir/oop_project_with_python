
from random import randint
from datetime import datetime

class Bank:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.total_balance = 0
        self.total_loan = 0
        self.bool_loan = False
    def add_user(self, user):
        self.users.append(user)
    def get_user(self):
        print("Name\t Email\t    AmountNO \t Account-Type")
        for user in self.users:
            print(f"{user.name}\t  {user.email}\t {user.account_number} \t{user.account_type}")
    def find_user(self, name,email):
        for user in self.users:
            if user.name == name and user.email == email:
                # print(user.id, user.name, user.email, user.amount)
                return user
        print("User not found")
        return None
    def delete_user(self, name, email):
        # self.find_user()
        for user in self.users:
            if user.name == name and user.email == email:
                self.users.remove(user)
                print(f"{user.name} deleted  !! ")
                return 
        print("User not found")
        # return None
class User:
    def __init__(self,name,email,account_type):
        self.name = name
        self.email = email
        self.amount = 0
        self.account_number = f"{name}{randint(1,1000)}{email}"
        self.account_type = account_type
        self.history=[]
        self.loan_time=0
    def show_history(self):
        for i in self.history:
            print(i)
    def add_money(self,bank, money):
        self.amount = self.amount + money
        self.history.append(f"Add Money {money} time: {datetime.now()}")
        bank.total_balance+=self.amount
    def withdraw_money(self,bank, money):
        if money>self.amount:
            print("Withdrawal amount exceeded")
        elif bank.bool_loan==True:
            print("Loan future is off")

        else:
            self.amount = self.amount - money
            self.history.append(f"Withdraw Money {money} time: {datetime.now()}")

    
    def transfer_money(self, bank, money, name):
        if money<self.amount:
            # try:
                for i in bank.users:
                    # print(i.name,i.email,i.amount,i.id)
                    if i.name == name :
                        i.amount +=money 
                        self.amount-=money

                        i.history.append(f"Money recived {money} from {self.name} time: {datetime.now()}")
                        self.history.append(f"Transfer Money {money} time: {datetime.now()}")
                        
                        # self.withdraw_money(money)
                        return
                print("Account does not exist")
                return
            # except Exception as e:
            #     print(e)
        else:
            print("You have no money")
    def show_money(self):
        print(self.name, "Amount : " , self.amount)
    
    def get_loan(self,bank,money):
        if self.loan_time<2 and bank.bool_loan==False and bank.total_balance>=money:
            self.amount+=money
            self.history.append(f"Loan Money {money} time: {datetime.now()}")
            self.loan_time+=1
            bank.total_loan+=money
            bank.total_balance-=money
        else:
            print("Bank is empty !!")
        

class Admin:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        # self.amount = amount
    
    def add_user(self, bank,user):
        bank.add_user(user)
    def delete_user(self, bank,name,email):
        bank.delete_user(name,email)
    def get_user(self,bank):
        bank.get_user()
    def available_balance(self,bank):
        print(bank.total_balance)
    def loan_balance(self,bank):
        print(bank.total_loan)
    def fucure(self,bank,types):
        bank.bool_loan=types



bank = Bank("Dhaka Bank")
while True:
    print("welcome")
    print("1. Admin login")
    print("2. User login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Admin login")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        admin = Admin(name, email)
        while True:
            print("1. create an account ")
            print("2. Delete any user account  ")
            print("3. see all user accounts list   ")
            print("4. check the total available balance of the bank   ")
            print("5. check the total loan amount")
            print("6. on or off the loan feature of the bank")
            print("7. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter User name: ")
                email = input("Enter User email: ")
                print("User account Type 1. Saving  2. Current")
                s = None
                while s is None:
                    choice = input("Enter your choice (1 or 2): ")

                    if choice == "1":
                        s = "Saving"
                    elif choice == "2":
                        s = "Current"
                    else:
                        print("Invalid choice. Please enter 1 or 2.")
                usr=User(name, email,s)
                admin.add_user(bank,usr)
            elif choice == 2:
                name = input("Enter User name: ")
                email = input("Enter User email: ")
                admin.delete_user(bank,name,email)
            elif choice == 3:
                admin.get_user(bank)
            elif choice == 4:
                admin.available_balance(bank)
            elif choice == 5:
                admin.loan_balance(bank)
            elif choice == 6:
                print("Please enter 1. ON or 2. Off")
                # c=int(input("Enter enter Number: "))
                s = None
                while s is None:
                    choice = input("Enter your choice (1 or 2): ")

                    if choice == "1":
                        s = True
                    elif choice == "2":
                        s = False
                    else:
                        print("Invalid choice. Please enter 1 or 2.")

                admin.fucure(bank,s)
                # pass
            elif choice == 7:
                break
            else:
                print("Invalid choice")

    elif choice ==2:
        print("User login")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        # id = int(input("Enter your user id: "))
        us=bank.find_user(name,email)
        if us == None:
            print("User not found")
        else:
            # user = User(us.name, us.email,us.amount,us.id)

            while True:
                print("1. Add money")
                print("2. Withdraw money")
                print("3. Transfer money")
                print("4. Show money")
                print("5. show History")
                print("6. Get Loan")
                print("7. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    amount = int(input("Enter amount: "))
                    us.add_money(bank,amount)
                elif choice == 2:
                    amount = int(input("Enter amount: "))
                    us.withdraw_money(bank,amount)
                elif choice == 3:
                    money = int(input("Enter amount: "))
                    name = input("Enter user name: ")
                    # email = input("Enter user email: ")
                    # us.amount-=money
                    us.transfer_money(bank, money,  name)
                elif choice == 4:
                    us.show_money()
                elif choice == 5:
                    us.show_history()
                    # bank.
                elif choice == 6:
                    money = int(input("Enter amount: "))
                    us.get_loan(bank,money)
                elif choice == 7:
                    break
                else:
                    print("Invalid choice")
    elif choice ==3:
        print("Exiting.....")
        break
    else:
        print("Invalid choice")