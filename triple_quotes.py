# Judd Brau
# Period 7
# triple_quotes.py
from art import ascii_art
num = int(input("What picture do you want to see? (1, 2, 3)")) - 1

if num == 3:
    print('hiiiiiiii\r')
else:
    print(ascii_art[num])
