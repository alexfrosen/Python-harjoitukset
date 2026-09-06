luvut = []

while True:
    luku1 = input("Anna joku luku: ")

    if luku1 ==" ":
        break

    luvut.append(int(luku1))

print("Pienin luku:", min(luvut))
print("Suurin luku:", max(luvut))