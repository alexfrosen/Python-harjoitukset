import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("Rekisteri | Huippunopeus | Nopeus | Kuljettu matka")
        print("-" * 60)

        for auto in self.autot:
            print(auto.rekisteritunnus,"|",auto.huippunopeus,"km/h",auto.nopeus,"km/h",auto.kuljettu_matka,"km")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True

        return False


autot = []

for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)


tunti = 0

while not kilpailu.kilpailu_ohi():

    kilpailu.tunti_kuluu()

    tunti += 1

    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()


print("\nKILPAILU PÄÄTTYI!")
kilpailu.tulosta_tilanne()