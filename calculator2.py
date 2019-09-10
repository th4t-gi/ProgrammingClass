# Judd Brau
# Period 7
# calculator2.py
import re

def convNum(word):
    if word in numbers.keys():
        return numbers[word]
    for k, v in startwith.items():
        if word.startswith(k):
            for kk, vv in endwith.items():
                if word.endswith(kk):
                    return (vv+v)

    return word
def doOp(list):


numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'twenty': 20,
    'thirty': 30
}

startwith = {
    'thir': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'twenty': 20,
    'thirty': 30,
}

endwith = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'teen': 10,
}

operations = [
    'times',
    'subtract',
    'plus',
    'divided',
    'by',
    'from'
]


print("This is a calculator to turn words into numbers!\nEx. Two times nineteen minus three\n")
expr = input("Give me an expression to solve! ")

expr = re.split(' ', expr.lower())
print(expr)
expr = [convNum(i) for i in expr]
expr = [doOp([]) for i, el in enumerate(expr)]
print(expr)
