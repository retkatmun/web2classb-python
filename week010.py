#foor loop
'''
numbers = [1,2,3,4,5]
names = ["tom","jerry","mimi","val","john"]
'''
#for number in numbers:
#	print(number)
#for _ in numbers:
#	print("scholar")
#for name in names:
#	print(name)

#range 

'''
for i in range(len(names)):
	print(f"name {i}")
	print(names[i])
'''

'''
vip = ["tom","jerry","mimi","val","john"]

name_input = input("Enter name:>>> ").capitalize()

for i in vip:
    if i == name_input:
	    print("vip")
    else:
	    print("regular")

for i in range(1,101):
	total = i * i
	print(f"{i} * {i} = {total}")

'''

for num in range(1, 101):  
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

