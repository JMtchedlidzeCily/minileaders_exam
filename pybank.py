# ACCOUNT CREATION 
name = input("Enter your name: ")
pin = input("Create a four-digit PIN: ")

# Ensuring the pin is valid
while not (pin.isdigit() and len(pin) == 4):
    print("INVALID PIN. Please enter a four-digit PIN.")
    pin = input("Create a four-digit PIN: ")

# List to store accounts
accounts = [
    {"name": name, "pin": pin, "balance": 0}
]

# Function to check PIN
def pincheck(account):
    while True:
        usrpin = input("Enter your PIN: ")
        if usrpin == account["pin"]:
            return True
        else:
            print("Incorrect PIN, try again.")

# Function to find an account by name and PIN
def find_account(name, pin):
    for account in accounts:
        if account["name"] == name and account["pin"] == pin:
            return account
    return None

# BANK SYSTEM
quit = False

while not quit:
    # Main menu
    print("\nMenu:")
    choice = input(f"Hi, {name}! Please pick one of the following actions:\n1. See balance\n2. Withdraw cash\n3. Deposit cash\n4. Create a new account\n5. Log into another account\n6. Quit\n")

    if choice == "1":
        print(f"You have ${accounts[0]['balance']} in your account.")
    elif choice == "2":
        if pincheck(accounts[0]):
            withdraw = int(input("Enter the amount of cash you want to withdraw: "))
            if withdraw > accounts[0]['balance']:
                print("Insufficient balance.")
            else:
                accounts[0]['balance'] -= withdraw
                print(f"Successfully withdrew ${withdraw}. Your new balance is ${accounts[0]['balance']}.")
    elif choice == "3":
        if pincheck(accounts[0]):
            deposit = int(input("Enter the amount of cash you want to deposit: "))
            accounts[0]['balance'] += deposit
            print(f"Successfully deposited ${deposit}. Your new balance is ${accounts[0]['balance']}.")
    elif choice == "4":
        newname = input("Enter your name: ")
        newpin = input("Create a four-digit PIN: ")
        while not (newpin.isdigit() and len(newpin) == 4):
            print("INVALID PIN. Please enter a four-digit PIN.")
            newpin = input("Create a four-digit PIN: ")
        accounts.append({"name": newname, "pin": newpin, "balance": 0})
        print(f"Account created successfully for {newname}!")
    elif choice == "5":
        logname = input("Enter your name: ")
        logpin = input("Enter your PIN: ")
        account = find_account(logname, logpin)
        if account:
            print(f"SUCCESS! You logged into {logname}'s account.")
            accounts[0] = account
            name = logname
        else:
            print("Account not found. Please check your credentials.")
    elif choice == "6":
        quit = True
    else:
        print("Enter a valid choice.")

print("Thanks for using our bank!")
