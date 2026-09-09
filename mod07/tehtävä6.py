import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2 / 100
    pinta_ala = math.pi * sade ** 2
    return hinta / pinta_ala


halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija cm: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija cm: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

hinta_m2_1 = yksikkohinta(halkaisija1, hinta1)
hinta_m2_2 = yksikkohinta(halkaisija2, hinta2)

if hinta_m2_1 < hinta_m2_2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif hinta_m2_2 < hinta_m2_1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä edullisia.")