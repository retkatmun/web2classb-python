'''
You try to withdraw money from a Nigerian ATM.
  The ATM has only ₦1000 notes and you have ₦10,000 in your account.
   The machine allows withdrawal only if the amount requested is less than or equa    l to your balance.
  The user enters the amount.
   
   Your  program  should decide:
   Whether to allow the transaction?
   Or deny it with a message: 
   “Insufficient funds or invalid amount”?
'''
'''
my_balance = 10000

amount = float(input("Enter the amount to withdraw: "))

if amount > 0:
    if amount <= my_balance:
        if amount % 1000 == 0:
            print("Transaction successful")
        
        else:
            print("Invalid amount.")
    
    else:
        print("Insufficient funds")

else:
    print("Invalid amount")
'''
'''
name = "Bankat"
name2 = name + "helo"

print(hex(id(name)))
print(hex(id(name2)))


name = -3%2
print(name)

name = 1 // 2
print(name)


name = {
}

name = "{}"
print(type(name))
'''
''
'''
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

all_keys = my_dict.values()
print(list(all_keys))
'''

#1
password = input("Enter your password: ")
confirmed_password = input("confirmed password: ")

if password == confirmed_password:
	print("password matched")
else:
    print("password mismatch")

'''
match confirmed_password:
    case _ if confirmed_password == password:
        print("Password matched")
    case _:
        print("Password mismatch")
'''
#2
num1 = int(input("Enter number integer"))
num2 = int(input("Enter second number"))

result = num1 + num2
print(result)

#3
score = [result]
print(score)

#4
# Create a dictionary with one student record
students = {
    "student1": {
        "name": "John Doe",
        "level": "100",
        "score": 70
    }
}
students["student1"]["score"] += 10
print(students)

#5
score = int(input("Enter the student's score (0-100): "))

if 70 <= score <= 100:
    print("A")
elif 60 <= score <= 69:
    print("B")
elif 50 <= score <= 59:
    print("C")
elif 45 <= score <= 49:
    print("D")
elif 40 <= score <= 44:
    print("E")
elif 0 <= score <= 39:
    print("F")
else:
    print("Invalid score")

