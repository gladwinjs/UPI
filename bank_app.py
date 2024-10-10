import os
import pickle

# Class representing a user
class User:
    def __init__(self, name, phone, account, password, balance=0):
        self.name = name
        self.phone = phone
        self.account = account
        self.password = password
        self.balance = balance

# Function to save user data to a file
def save_user(user):
    with open(f"{user.phone}.dat", 'wb') as file:
        pickle.dump(user, file)

# Function to load user data from a file
def load_user(phone):
    if os.path.exists(f"{phone}.dat"):
        with open(f"{phone}.dat", 'rb') as file:
            return pickle.load(file)
    return None

# Function for user registration
def register():
    print("Register a new account")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    account = input("Enter your account number: ")
    password = input("Create a password: ")

    if load_user(phone):
        print("An account with this phone number already exists!")
    else:
        user = User(name, phone, account, password)
        save_user(user)
        print("Account registered successfully!")

# Function for user login
def login():
    print("Login to your account")
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")

    user = load_user(phone)

    if user and user.password == password:
        print(f"Welcome, {user.name}!")
        return user
    else:
        print("Invalid phone number or password!")
        return None

# Function to show the user's balance
def check_balance(user):
    print(f"Your current balance is Rs.{user.balance}")

# Function to deposit money
def deposit(user):
    amount = float(input("Enter the amount to deposit: "))
    user.balance += amount
    save_user(user)
    print(f"Rs.{amount} deposited successfully! Your new balance is Rs.{user.balance}")

# Function to withdraw money
def withdraw(user):
    amount = float(input("Enter the amount to withdraw: "))
    if user.balance >= amount:
        user.balance -= amount
        save_user(user)
        print(f"Rs.{amount} withdrawn successfully! Your new balance is Rs.{user.balance}")
    else:
        print("Insufficient balance!")

# Function to transfer money to another account
def transfer(user):
    phone_to_transfer = input("Enter the recipient's phone number: ")
    amount = float(input("Enter the amount to transfer: "))

    recipient = load_user(phone_to_transfer)
    if recipient:
        if user.balance >= amount:
            user.balance -= amount
            recipient.balance += amount
            save_user(user)
            save_user(recipient)
            print(f"Rs.{amount} transferred to {recipient.name} successfully!")
        else:
            print("Insufficient balance!")
    else:
        print("Recipient account not found!")

# Function to change password
def change_password(user):
    new_password = input("Enter your new password: ")
    user.password = new_password
    save_user(user)
    print("Password changed successfully!")

# Main function to run the banking system
def main():
    print("Welcome to the Simple Banking System!")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Online Transfer")
                    print("5. Change Password")
                    print("6. Logout")
                    
                    action = input("Choose an option: ")

                    if action == '1':
                        check_balance(user)
                    elif action == '2':
                        deposit(user)
                    elif action == '3':
                        withdraw(user)
                    elif action == '4':
                        transfer(user)
                    elif action == '5':
                        change_password(user)
                    elif action == '6':
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid option!")
        elif choice == '3':
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
