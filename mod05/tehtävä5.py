tunus = "python"
salasana = "radmin"
yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana_input = input("Anna salasana: ")
    yritykset += 1

    if tunnus == tunus and salasana_input == salasana:
        print("Tervetuloa")
        break
    elif yritykset == 5:
        print("Pääsy evätty")