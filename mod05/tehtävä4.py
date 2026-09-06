import random

oikea = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku: "))

    if arvaus > oikea:
        print("Liian suuri arvaus")
    elif arvaus < oikea:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break