import random

answers=[
    "Yes",
    "No",
    "Matbe",
    "Ask Again Later",
    "Definitely",
    "Not Sure"
]

input("Ask a question:")

print("Answer:",random.choice(answers))