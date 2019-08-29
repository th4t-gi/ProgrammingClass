# Judd Brau
# Period 7
# riddle.py
import time

riddles = [
    ["Whats red and greed and goes 100mph?", ["a frog in a blender", "Correct!"], "Close! A frog in a blender"],
    ["Knock knock!", None, "Control Freak", None, "Ok, now your supposed to say \"Control Freak who?\" okay?"],
    ["What do you call cheese that isn't yours?", ["nacho cheese", "Correct!"], "Almost!, its nacho cheese"]
]

def printRiddle(riddles):
    rididx = 0
    print(riddles[0])
    for string, i in enumerate(riddles[rididx]):
        print(i)
        if type(string) == list:
            answer = input()
            if answer == string[0] or (not string[0]):
                print(string[1])
            else:
                print(string[i+1])
        else:
            print(string)
    rididx += 1


try:
    num = input("What riddle do you want to hear, 1, 2, or 3? ")
except:
    print("Please enter in a number next time")
    quit()

printRiddle(riddles)
# if int(num) == 2:
#     print("Knock knock!")
#     input()
#     print("Control Freak.")
#     time.sleep(1.7)
#     print("Okay, now your supposed to say 'Control Freak who?'")
# else:
#     set_up = riddles[num]
#     print(set_up[0])
#     answer = input(": ")
#     if answer.lower() == set_up[1].lower():
#         print("Correct!")
#     else:
#         print("Close!", set_up[1])
