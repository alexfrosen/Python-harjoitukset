luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print("Ei ole alkuluku")
else:
    alkuluku = True

    for i in range(2, luku):
        if luku % i == 0:
            alkuluku = False
            break

    if alkuluku:
        print("On alkuluku")
    else:
        print("Ei ole alkuluku")