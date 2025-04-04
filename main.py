from random import shuffle

cards = []
for i in range (13):
    cards.append(f"{i + 1} S")
    cards.append(f"{i + 1} H")
    cards.append(f"{i + 1} D")
    cards.append(f"{i + 1} C")

shuffle(cards)

print(cards)