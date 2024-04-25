class Bank:
    def __init__(self, name):
        self.name = name
        self.users = []
    def add_user(self, user):
        self.users.append(user)
    def get_user(self):
        print("Id \t Name\t Email\t    Amount")
        for user in self.users:
            print(user.id,user.name,user.email,user.amount)
    def find_user(self, name ,email):
        for i in self.users:
            if i.name == name and i.email == email:
                return i
            else:
                # print("User not found")
                return None
class User:
    def __init__(self,name,email,amount,id):
        self.name = name
        self.email = email
        self.amount = amount
        self.id = id
        # self.bank=Bank()

    def add_money(self, money):
        self.amount = self.amount + money
    def withdraw_money(self, money):
        self.amount = self.amount - money
    
    def transfer_money(self, bank, money, userId):
        try:
            for i in bank.users:
                print(i.name,i.email,i.amount,i.id)
                if i.id == userId:
                    i.amount +=money 
                    self.withdraw_money(money)
                    return
                else:
                    print("User not found")
                    return
        except Exception as e:
            print(e)
    def show_money(self):
        print(self.name, "Amount : " , self.amount)


class Admin:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        # self.amount = amount
    
    def add_user(self, bank,user):
        bank.add_user(user)
    def get_user(self,bank):
        bank.get_user()


# fst_user=User("Tanvir","Tn@gmail.com",12000, 1)
# fst_user2=User("Tanvir","Tn@gmail.com",12000,2)

# admin=Admin("admin","adn@gmail.com")
# admin.add_user(bank,fst_user)
# admin.add_user(bank,fst_user2)

# # bank.add_user(fst_user)
# # bank.add_user(fst_user2)
# bank.get_user()

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
            print("1. Add user")
            print("2. View users")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter User name: ")
                email = input("Enter User email: ")
                amount = int(input("Enter User amount: "))
                ids=int(input("Enter User id: "))
                usr=User(name, email,amount,ids)
                admin.add_user(bank,usr)
            elif choice == 2:
                admin.get_user(bank)
                # pass
            elif choice == 3:
                break
            else:
                print("Invalid choice")

    elif choice ==2:
        print("User login")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        us=bank.find_user(name, email)
        if us == None:
            print("User not found")
        else:
            # user = User(us.name, us.email,us.amount,us.id)

            while True:
                print("1. Add money")
                print("2. Withdraw money")
                print("3. Transfer money")
                print("4. Show money")
                print("5. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    amount = int(input("Enter amount: "))
                    us.add_money(amount)
                elif choice == 2:
                    amount = int(input("Enter amount: "))
                    us.withdraw_money(amount)
                elif choice == 3:
                    # bank = input("Enter bank name: ")
                    money = int(input("Enter amount: "))
                    userId = int(input("Enter user id: "))
                    us.transfer_money(bank, money, userId)
                elif choice == 4:
                    us.show_money()
                elif choice == 5:
                    break
                else:
                    print("Invalid choice")
    elif choice ==3:
        print("Exiting")
        break
    else:
        print("Invalid choice")