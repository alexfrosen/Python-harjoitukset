def summa(lista):
    tulos = 0

    for luku in lista:
        tulos += luku

    return tulos


luvut = [2, 5, 8, 10]

summaus = summa(luvut)

print("Lukujen summa:", summaus)