'''
number = 15

if number > 20:
    print("number is greater ")
elif number > 10:
    print("number is greater than 10")
elif number > 5:
    print("5 is less than number")
elif number > 14:
    print("14 is less than number")
else:
    print("inavalid")


if number > 20:
    print("number is greter")
if number > 10:
    print("number is greater 10")
if number > 5:
    print("5 less than number")
if number > 14:
    print("14 less than number")
'''

'''
names = ["Tom","Jerry","Mimi","Val"]

user_name = input("user name\n>>." )
flag = False
for name in names:	
	if user_name == name:
		flag = True
		break
if  flag == True:		
    print("Vip")
else:
    print("Regular")

'''

numbers = [12,75,150,180,145,525,50]

'''
for number in numbers:
	if number > 500:
		break
	elif number > 150:
		continue
	elif number % 5 ==0:
		print(number)
		
'''
'''
count = len(numbers) -1
for inumber in range(len(numbers)):
    print(numbers[count])
    count = count -1
'''

largest = numbers[0]
for number in numbers:
	if number > largest:
		largest = number
print(largest)		
