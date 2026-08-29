




leiviskät = int(input("anna leiviskät"))
naulat = int(input("anna naulat"))
luodit = float(input("anna luodit"))


naulamäärä =leiviskät*20+naulat
luotimäärä =naulamäärä*32+luodit
paino =luotimäärä*13.3
kilogrammaa = paino//1000
grammaa = paino % 1000


print (f"massa nykymittojen mukaan: {kilogrammaa:.0f} kilogrammaa ja {grammaa:.2f} grammaa")



