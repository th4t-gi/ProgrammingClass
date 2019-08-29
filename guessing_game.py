# Judd Brau
# Period 7
# guessing_game.py

from random import randint, randrange

a = 0
b = int(input("What number do you want to guess up to?"))
num = randint(a, b)

print("Guess a number between {0} and {1}!".format(a, b))
try:
    answer = 0
    count = 0
    while answer != num:
        answer = int(input())
        if (answer > b) or (answer < a):
            print("That's not in the range silly!")
        elif answer > num:
            print("Lower")
        else:
            print("Higher")
        count+=1
    print("Correct!!!!! you guessed that in {} guesses".format(count))
    print("Y"+ "A"*100+ "Y")
except ValueError:
    print("Please enter in only numbers!")
