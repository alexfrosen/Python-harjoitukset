import random

def heitä():
    return random.randint(1, 6)

while True:
    silmaluku = heitä()
    print(silmaluku)

    if silmaluku == 6:
        break