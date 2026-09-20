class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylos()

        while self.kerros > kohde:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print("Hissi on kerroksessa", self.kerros)


class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissien_maara):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("PALOHÄLYTYS!")

        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)


# Tehtävä 1
hissi = Hissi(1, 10)

hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)


# Tehtävä 2
talo = Talo(1, 10, 3)

talo.aja_hissia(1, 8)
talo.aja_hissia(2, 5)
talo.aja_hissia(3, 3)


# Tehtävä 3
talo.palohalytys()