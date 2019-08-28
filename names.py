# Judd Brau
# Period 7
# names.py

from time import sleep

def quit_program():
    exit = input("Press enter to exit this program: ")
    if exit == '':
        quit()
    else:
        quit_program()

x = input('what is your name? ')
sleep(1)
print("nice to meet you", x)
sleep(1)
num = input("How many times do you want to see your name? ")
print("HI {} ".format(x)*int(num))
quit_program()
