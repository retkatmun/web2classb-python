'''
age = int(input("Enter your age: "))

if age >= 60:
    print("You are eligible to buy a ticket.\n you can get a discount ticket ")
elif age >= 18:
    print("You can buy a regular movie ticket.")
elif age >= 12:
    print("You can buy a Teen Ticket")
else:
    print("You can buy a Kid Ticket")
'''


'''
phone_budget = float(input("Enter your budget: "))

if phone_budget >= 500:
   print("go for Iphone: ")
elif phone_budget < 500 and phone_budget >= 1000:
    print("Google pixel 9 pro")
elif phone_budget < 500 and phone_budget >= 200:
    print("you can go for Redmi: ")
else:
    print("save more: ")
'''


student = {
    "name": "legolas",
    "has_registered": True,
    "has_piad": True,
    "has_internet": False

}


if student["has_registered"]:
    if student["has_piad"]:
        if student["has_internet"]:
            print("Allow access to exam")
        else:
            print("Check internet connection")
    else:
        print("Pay your fees")
else:
    print("You have to register first")


