import random

print('-' * 40)
print('Welcome to Your Password Generator'.center(40))
print('-' * 40)
chars = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'"!@#$£¢%¬&*()-_=+§´`[]{~}^,.;:/?°|'''

number = int(input("Amount of passwords to generate: "))
length = int(input("Your password(s) lenght(s): "))

print('-' * 35)
print('Here are your password(s)'.center(35))
print('-' * 35)

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print("-" * length)
    print(passwords.center(length))
    print("-" * length)
