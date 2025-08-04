'''
response = ("good",4)
print(type(response),response)

response = (True,"welcome",["email","username"])

(succes,message,data) = response
print(succes)
print(message)
print(data)

my_response = list(response)
my_response[0] = (False)
my_response = tuple(my_response)

print(type(my_response))

print(f'{response[1]} {response[2]}')

a = (1,2,3)
b = (4,5,6)
print(a + b)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

'''
b = [1,"2",3]
print(b[0] + 2)
