
from abc import ABC
class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Employess(User):
    def __init__(self,name,email,phone,address,salary,job):
        super().__init__(name,email,phone,address)
        self.salary = salary
        self.job = job


class Customer(User):
    def __init__(self,name,email,phone,address):
        super().__init__(name,email,phone,address)
        self.cart= Order()
    def add_to_cart(self,resturent,item,quantity):
        itm=resturent.menu.find_item(item)
        # print(itm)
        if itm:
            if quantity > itm.quantity:
                print("Item quantity exceeded!!")
            else:
                itm.quantity = quantity
            # print(itm)
                self.cart.add_to_cart(itm)
                print("item added")
           
        else:
            print(f"{itm} is not available in {resturent.name}")
    def show_cart(self):
        print("<---------------view cart-------------------->")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price} $\t{item.quantity}")
        print("total price: ",self.cart.total_price)


    def viwe_menu(self,resturent):
        resturent.menu.show_menu()
    def pay_bill(self):
        self.cart.clear()
        


class Order:
    def __init__(self):
        self.items = {}
        # self.total_price = 0
    def add_to_cart(self,item):
        if item in self.items:
            self.items[item] +=item.quantity
        else:
            self.items[item] = item.quantity
    
    
    def remove_item(self,item):
        if item in self.items:
           del self.items[item]
        else:
            print(f"{item.name} is not available in cart")
    @property
    def total_price(self):
        total_price = 0
        for item,quantity in self.items.items():
            total_price += item.price * quantity
        return total_price
    
    def clear(self):
        self.items = {}

class Admin(User):
    def __init__(self,name,email,phone,address):
        super().__init__(name,email,phone,address)


    def add_employess(self,resturent,employee):
        resturent.add_employess(employee)
        print(f"{employee.name} added!!")


    def display_employess(self,resturent):
        resturent.display_employess()
    

    def show_menu(self,resturent):
        resturent.menu.show_menu()


    def add_item(self,resturent,item):
        resturent.menu.add_item(item)
    def remove_item(self,resturent,item_name):
        resturent.menu.remove_item(item_name)


class Resturent:
    def __init__(self,name) :
        self.name = name
        self.employess=[]
        self.menu = Menu()
    def add_employess(self,employee):
        self.employess.append(employee)
        
    def display_employess(self):
        print("<---------------Employess list---------------->")
        for employee in self.employess:
            print(employee.name,employee.email,employee.phone,employee.address,employee.salary,employee.job)


class Menu:
    def __init__(self):
        self.items=[]
    def add_item(self,item):
        self.items.append(item)
    def find_item(self,item_name):
        # print(item_name)
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    def remove_item(self,item_name):
        itm=self.find_item(item_name)
        if itm!= None:
            self.items.remove(itm)
            print(f"{itm.name} removed!!")
        else:
            print(f"{item_name} not found!!")
    def show_menu(self):
        print("<---------------Menu---------------->")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price} $\t{item.quantity}")

class FootItem:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# mamar_restaurant =Resturent("Mamar Restaurant")

# mn=Menu()
# itm=FootItem("Barger",120,40)
# itm2=FootItem("Pizza",120,20)
# admin=Admin("Fuad","tan@gmail.com",129304,"Dhaka")

# admin.add_item(mamar_restaurant,itm)
# admin.add_item(mamar_restaurant,itm2)
# # mn.show_menu()

# customer1=Customer("Tanvir","tan@gmail.com",129304,"Dhaka")
# customer1.add_to_cart(mamar_restaurant,"Pizza",12)
# # customer1.add_to_cart(mamar_restaurant,"Pizza",10)
# # customer1.viwe_menu(mamar_restaurant)

# customer1.show_cart()
# # mamar_restaurant.menu.show_menu()



# --------------------main--------------------

# if __name__ == "main":
resturent = Resturent("Mamar Restaurant")
def coustomer_menu():
    name=input("Enter Your name")
    email=input("Enter your email address")
    phone=input("Enter your phone number")
    address=input("Enter your address")
    customer = Customer(name,email,phone,address)
    while True:
        print("<---------------Customer menu-------------------->")
        print("1. Add to cart")
        print("2. View cart")
        print("3. Show menu")
        print("4. Pay Bill")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            customer.add_to_cart(resturent,item_name,quantity)
        elif choice == 2:
            customer.show_cart()
        elif choice == 3:
            customer.viwe_menu(resturent)
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
def admin_menu():
    name=input("Enter Your name")
    email=input("Enter your email address")
    phone=input("Enter your phone number")
    address=input("Enter your address")
    admin = Admin(name,email,phone,address)
    while True:
        print("<---------------Admin menu-------------------->")
        print("1. Add new item")
        print("2. Add new Employee")
        print("3. Display Employess")
        print("4. Show items")
        print("5. Delete items")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            item=FootItem(item_name,item_price,quantity)
            admin.add_item(resturent,item)
        elif choice == 2:
            name=input("Enter Your name")
            email=input("Enter your email address")
            phone=input("Enter your phone number")
            address=input("Enter your address")
            salary=input("Enter your salary")
            job=input("Enter your job")
            employee = Employess(name,email,phone,address,salary,job)
            admin.add_employess(resturent,employee)
        elif choice == 3:
            admin.display_employess(resturent)
        elif choice == 4:
            admin.show_menu(resturent)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(resturent,item_name)
        elif choice == 6:
            break
        else:
            print("Invalid choice")


while True :
    print("1. Login Admin")
    print("2. Login Customer")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        admin_menu()
    elif choice == 2:
        coustomer_menu()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice")









