user_register = {}

user_data = {"core": "pass1", "tk": "pass2", "mp": "pass3"}

print("Login and\nRegistration portal\nSystem\n")

command_line = input("Enter 'login' or 'register':>>> ")

# LOGIN SECTION
if command_line == "login":
    print("Continue login:")
    enter_data = input("Enter name:  ")
    if enter_data in user_data:
        print("User exists")
        enter_password = input("Enter password:  ")
        if enter_password == user_data[enter_data]:
            print("Successful")
            is_verified = False  # By default, not verified
            if is_verified:
                print("Verified")
            else:
                print("Not verified")
        else:
            print("Wrong password")
    else:
        print("User does not exist")

# REGISTRATION SECTION
elif command_line == "register":
    print("Continue registration:")
    new_user = input("Enter new username: ")
    if new_user in user_data:
        print("User already exists")
    else:
        new_password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
        if new_password == confirm_password:
            proceed = input("Do you want to proceed with verification? (yes/no): ").lower()
            if proceed == "yes":
                balance = float(input("Enter your account balance: "))
                if balance >= 1500:
                    print("Verified and successfully registered.")
                    user_register[new_user] = new_password  # Save new user
                else:
                    print("Insufficient balance. Not verified.")
            else:
                print("Not verified.")
        else:
            print("Passwords do not match")
else:
    print("invalid") 	
