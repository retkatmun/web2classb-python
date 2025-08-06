'''
enter_password = int(input("Enter password:  "))
comfirm_password = int(input("comfirm password:  "))

if enter_password == comfirm_password:
    print("successful")
else:
    print("wrong password") 
'''

user_data = ["core","tk","mp"]


enter_data = input("Enter name:  ")

if enter_data in user_data:
    print("exist")
else:
    print("does not exist")
