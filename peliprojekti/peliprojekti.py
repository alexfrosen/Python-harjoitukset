nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))

print("Hei!", nimi, ikä)

if ikä < 12:
    print("Olet alaikäinen.")
    print("Sammuu...")
else:
    print("Tervetuloa", nimi, "!")


esineet = []


def aloita_peli():
    print("Peli alkaa!")
    
    while True:
        esine = input("Anna esine, jonka haluat ottaa mukaan (tyhjä lopettaa): ")

        if esine == "":
            break

        esineet.append(esine)

    print("Esineet lisätty!")


def ohjeet():
    print("PELIN OHJEET")
    print("1. Aloita peli.")
    print("2. Kerää esineitä.")
    print("3. Voit tarkistaa keräämäsi esineet.")
    print("4. Lopeta peli valitsemalla 3.")


def lopeta():
    print("Peli lopetetaan.")
    print("Kiitos pelaamisesta!")


while True:
    print()
    print("PÄÄVALIKKO")
    print("1. Aloita peli")
    print("2. Ohjeet")
    print("3. Lopeta")

    xx = input("Anna komento: ")

    if xx == "1":
        aloita_peli()

    elif xx == "2":
        ohjeet()

    elif xx == "3":
        lopeta()
        break

    else:
        print("Tuntematon komento.")