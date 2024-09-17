# RANDOM PASSWORD GENERATOR 
import random
import string

length=int(input("Enter the length of the password:"))
character=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(length):
    password+=random.choice(character)


print(password)

