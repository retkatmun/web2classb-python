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

my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

all_keys = my_dict.values()
print(list(all_keys)) 
