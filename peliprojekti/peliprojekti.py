nimi=str (input ("Anna Nimesi: "))
ikä = int(input("Anna ikäsi: "))
print ("Hei!",nimi, ikä)

if ikä < 12:
    print("Olet alaikäinen.")
    print("Sammuu...")
else:
    print("Tervetuloa", nimi, "!")

    while True:
        print("PÄÄVALIKKO")
        print("1. Aloita peli")
        print("2. Ohjeet")
        print("3. Lopeta")

        xx = input("Anna komento: ")

        if xx == "lopeta":
            break
        elif xx == "1":
            print("Peli alkaa!")
        elif xx == "2":
            print("Pelin ohjeet...")
        else:
            print("Tuntematon komento.")