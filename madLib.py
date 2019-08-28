# Judd Brau
# Period 7
# madLib.py

input("Hi!, your playing madlib! Ready? ")

words = [input("Give me an animal: "),
    input("Give me a place: "),
    input("Give me an occupation: "),
    input("Give me another occupation: "),
    input("Give me another place: "),
    input("Give me a mode of transportation: "),
    input("Give me a date: "),
    input("Finally, give me a hobbie: ")
]

input("Hi!, are you ready to see your story? ")

print(
    "Once upon a time there was a {0}, the {0} loved living at {1},but they didn't like {2} everyday to stay there. One day, the {0} decided to pursue {3} in {4} and left {1} for a new life. They took the {5} to {4}. But sadly, on {6}, the {1} died while doing {7}".format(*words)
)
