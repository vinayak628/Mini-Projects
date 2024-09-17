# Guess the number game

import random
number=random.randint(1,50)
print("Guess a number between 1-50...")

while True:
    x=(input("Guess the number or Quit(Q):"))
    if(x=="Q"):
        print("Thankyou!!")
        break

    x=int(x)

    if (x==number):
        print("Hurrrray....!!!You guessed the correct number...!")
        break
    
    if(x<number):
        print("The number you have guessed is smaller...")
    elif(x>number):
        print("The number you have entered is greater...")
    else:
        print("Invalid Number")


print("---GAME OVER---")