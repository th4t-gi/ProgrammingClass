# Judd Brau
# Period 7
# names2.py

names = {
    "phil swift": "Awesome, I love Flex Tape",
    "mr. gryboski": "Hey, your that nerdy programming teacher!",
    "judd brau": "Hey!... your me!",
    "woof": "Woof woof woof woof!",
    "tony stark": "Can I get your autograph?!!!"
}

name = input("What is your name? ").lower()

if name in names.keys():
    print(names[name])
else:
    print("It's nice to meet you {}!".format(name))
