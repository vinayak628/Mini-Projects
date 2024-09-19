# Guess the number game

import random
number=random.randint(1,5)              #it generates random numbers within the given range
print("Guess a number between 1-5...")
attempt=0
Q=False

while True:
    x=(input("Guess the number or Quit(Q):"))
    if(x=="Q"):
        attempt+=1               #incrementing attempt if a number is guessed
        print("Thankyou!!")
        Q=True
        break

    x=int(x)      #converting into integer

    if (x==number):
        print("Hurrrray....!!!You guessed the correct number...!")
        attempt+=1               #incrementing attempt for the correct guess
        break
    
    if(x<number):
        print("The number you have guessed is smaller...")
        attempt+=1               #incrementing for a guess

    elif(x>number):
        print("The number you have entered is greater...")
        attempt+=1              ##incrementing for a guess

    else:
        print("Invalid Number")

if Q==False:       #if player does not choose to exit this loop runs!!
    print("You have completed the game in",attempt,"attempts!!")

print("---GAME OVER---")               