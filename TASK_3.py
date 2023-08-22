# Task 3 - Password Generator

# import modules
import string
import random

len = int(input("Enter Length of Password:"))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbols = string.punctuation

str=lower+upper+digit+symbols

password = random.sample(str, len)

password = "".join(password)

print(password)