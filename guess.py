import random
print("number guessing game")
number= random.randint(1,9)
print(number)
chances=0
print("guess a number between 1 and 9")
while chances<5:
    guess= int(input("enter yuor guess"))
    if guess == number: 
        print ("conragulation you won")
    elif guess < number:
        print ("your guess was to low")
    else:
        print ("your guess was to high")
    chances = chances+1
if  chances >= 5:
    print("you lose, the number is ",number)
