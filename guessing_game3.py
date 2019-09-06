# Judd Brau
# Period 7
# guessing_game.py

from random import randint, randrange
from art import art, faces

def guessing_game(num=None, count=0, start=False):
    if start:
        a = int(input("What number do you want to guess up to? "))
        num = randint(0, a)
        print("Guess a number between 0 and {}! ".format(a))

    answer = int(input())
    if (answer == num):
        winned(count)
    elif answer > num:
        print("Lower than", answer)
    else:
        print("Higher than", answer)
    guessing_game(num, count=count+1)

def ascii_art():
    print("Ok, here's a smiley face for you then!")
    print(faces[randint(0, len(faces)-1)])
    quit()

def winned(count):
    print("Correct!!!!! you guessed that in {} guesses".format(count))
    print(art[3])

    again = bool(input('Would you like to play again?(hit enter if not) '))
    if again:
        guessing_game(start=True)
    else:
        ascii_art()


if __name__ == '__main__':
    play = bool(input("Do you want to play a guessing game?(hit enter if not) "))
    if play:
        guessing_game(start=True)
    else:
        ascii_art()
