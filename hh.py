import json
import os

DATA_FILE = "users.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return[]
    
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data,f,indent=4)
    

def home():
    print("Hello! User")
    while True:
        try:
            user_input=int(input("Press 1 for login and 2 for creating account: "))
            print()
            if(user_input in [1,2]):
                if user_input == 1:
                    name = login()
                    if name:
                        return name
                    else :
                        continue
                 
                else:
                    name = create()
                    return name
            else:
                raise ValueError("Not a valid number\n")
        except ValueError as e:
            print(e)
            
def exit1():
    print("Exiting...")
    exit()
      
            
            
            
def login():
    users=load_data()
    if not users:
        print("No users found. Create an account first.\n")
        return 
    
    try:
        user_id=int((input("Enter your ID: ")))
        pin=input("Enter your pin: ")
        
        for user in users:
            if user["id"] == user_id and user["pin"]==pin:
                print(f"Welcome back, {user["name"]}!\n")
                name = user["name"]
                return name
            else:
                print("Login failed. ID or Pin is inncorrect.\n")
        
    except ValueError:
        print("Invalid input. ID must be a number.\n")
        
    
        
        
def create():
    users = load_data()
    while True:
        try:
            name = input("Enter your name: ")
            if not name.replace(" ", "").isalpha():
                raise TypeError("Enter a valid name (letters and spaces only)")
            name = name.title()
            user_id=input("Enter the id no.: ")
            if not user_id.isdigit():
                raise TypeError ("Enter the number")
            user_id =int(user_id)
            pin=input("Enter 4 digit num pin: ")
            print()
            if not pin.isdigit() or len(pin) != 4:
                raise ValueError("Pin must be a number with 4 digits")
            break

        except Exception as e:
            print("Error!")
            print("Fill the form correct!")
            print("Reason:",e)
            print()
            
        
    print(f"Check your data info:\nName:{name}\nId:{user_id}\nPin:{pin}")
    while True:
        user_input=input("1 for Refill or 'confirm' for correct fill: ")
        print()
        if user_input == "1":
            return create()
        elif user_input.lower() == "confirm":
            break
        else:
            print("Enter the correct value! \n")
            
    new_user={
        "name":name,
        "id":user_id,
        "pin":pin,
        "balance": 0,
    }
    
    users.append(new_user)
    save_data(users)
    print("Account created successfully\n")
    return name
    
def delete(name):
    users = load_data()
    for i, user in enumerate(users):
        if user['name']==name:
            user_input = input(f"Are you aware that you are deleting your account? yes or no?")
            if user_input.lower() == "yes":
                users.pop(i)
                save_data(users)
                print("Account deleted sucessfully.\n")
                main()
                return
            else:
                print("Account deletion cancelled.\n")
    menu(name)

def get_balance(name):
    users = load_data()
    for user in users:
        if user["name"] == name:
            return user["balance"]
    return 0

def user_input():
    while True:
        x=input("Enter the amount: $")
        if x.isdigit():
            x=int(x)
            return x
        else:
            print("Enter the number! ")
            
    

def deposit(name,balance):
    users = load_data()
    for user in users:
        if user["name"] == name:
            print(f"{name}, you have ${user['balance']} in your account.")
            x = user_input()
            user["balance"] += x
            save_data(users)
            print(f"Your new balance is ${user['balance']}")
            break
            
        else:
            print("No user found")
        
    menu(name, user["balance"])
            
            
            
    
def withdraw(name,balance):
    users = load_data()
    for user in users:
        if user["name"]== name:
            print(f"{name}, you have ${user['balance']} in your account.")
            while True:
                x = user_input()
                if 0 < x <= user["balance"]:
                    user['balance']-=x
                    save_data(users)
                    print("Withdrawing..")
                    print(f"You have ${user['balance']} left.\n")
                    break
                    
                else:
                    print(f"You cant withdraw ${x}. You have ${user['balance']}.\n") 
    
    menu(name, user["balance"])


def menu(name,balance):
    while True:
        user_input=input("Enter 0 for exit\nEnter 1 for Deposit\nEnter 2 for Withdraw\nEnter 3 for Deletion of Account\nYour input: ")
        print()
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input in [0,1,2,3]:
                if user_input ==0:
                    exit1()
                elif user_input ==1:
                    deposit(name,balance)
                    break
                elif user_input ==2:
                    withdraw(name,balance)
                    break
                elif user_input ==3:
                    delete(name)
            else:
                print("Enter valid option\n")
        else:
            print("only numbers are allowed!\n")
    
    
                
        
    
            
        
            
            
    
    
       
#code here starts
def main():
    name = home()
    balance = get_balance(name)
    menu(name, balance)

    
main()
        
    
    
