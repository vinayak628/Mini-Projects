# RANDOM PASSWORD GENERATOR 
import random               # a python module which generates random choice
import string               # a python library which contains digits,ascii values and characters


#taking the length of the password from the user
length=int(input("Enter the length of the password:"))

#combining all the character,digits and punctuation from the string module
character=string.ascii_letters+string.digits+string.punctuation

#crreating an empty password variable
password=""

# for loop in the range of the length of the password given
for i in range(length):

#adding random choice from the characters in the password 
    password+=random.choice(character)

#dislay the password
print(password)
