# RANDOM PASSWORD GENERATOR 
import random
import string

length=int(input("Enter the length of the password:"))
character=string.ascii_letters+string.digits+string.punctuation

password="".join([random.choice(character) for i in range(length)])

print(password)
