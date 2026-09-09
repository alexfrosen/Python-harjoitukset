import random

määrä = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for i in range(määrä):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

print("Silmälukujen summa:", summa)