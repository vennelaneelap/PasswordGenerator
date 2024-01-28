import math
import numpy 
import random as rm
print("Hello world")

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
num = int(input("Amount of Passwords you want to generate: "))

length = int(input("how many letters do you need the passwords to me: "))

print("\nYour passwords are: ")
for pwd in range(num):
    passwords = ""
    for c in range(length):
        passwords += rm.choice(char)
    print(passwords)
