# Judd Brau
# Period 7
# riddle.py
import time

riddles = {
    "1": ["Whats red and greed and goes 100mph?", "a frog in a blender"],
    "Knock knock!": "Control Freak who?",
    "3": ["What do you call cheese that isn't yours?", "nacho cheese"]

}

try:
    num = input("What riddle do you want to hear, 1, 2, or 3? ")
except:
    print("Please enter in a number next time")
    quit()

if int(num) == 2:
    print("Knock knock!")
    input()
    print("Control Freak.")
    time.sleep(1.7)
    print("Okay, now your supposed to say 'Control Freak who?'")
else:
    set_up = riddles[num]
    print(set_up[0])
    answer = input(": ")
    if answer.lower() == set_up[1].lower():
        print("Correct!")
    else:
        print("Close!", set_up[1])
