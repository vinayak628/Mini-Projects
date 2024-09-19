# Guess the number game

import random
number=random.randint(1,5)
print("Guess a number between 1-5...")
attempt=0
Q=False

while True:
    x=(input("Guess the number or Quit(Q):"))
    if(x=="Q"):
        attempt+=1
        print("Thankyou!!")
        Q=True
        break

    x=int(x)

    if (x==number):
        print("Hurrrray....!!!You guessed the correct number...!")
        attempt+=1
        break
    
    if(x<number):
        print("The number you have guessed is smaller...")
        attempt+=1

    elif(x>number):
        print("The number you have entered is greater...")
        attempt+=1

    else:
        print("Invalid Number")

if Q==False:
    print("You have completed the game in",attempt,"attempts!!")
print("---GAME OVER---")