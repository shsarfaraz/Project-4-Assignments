import random

print("Welcome to your Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'
number = int(input("How many characters would you like in your password? "))
amount = int(input("How many passwords would you like? "))
print("\nHere's are your passwords: \n")

for x in range(amount):
    password = ''
    for x in range(number):
        password += random.choice(chars)
    print(password)

