# RANDOM PASSWORD GENERATOR 
import random               # a python module which generates random choice
import string               # a python library which contains digits,ascii values and characters

length=int(input("Enter the length of the password:"))         # input from the user


#using string module to call digits,characters and ascii values
character=string.ascii_letters+string.digits+string.punctuation        


#creating a list and joining it using ".join" 

#random.choice(character)= display a random character from the string module

password="".join([random.choice(character) for i in range(length)])      


#printing the password
print(password)
