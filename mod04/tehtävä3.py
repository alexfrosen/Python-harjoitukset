sp=input ("Kerro biologinen sukupuoli (M/N): ")
hgb=int (input ("Kerro myös Hemoglobiiniarvosi g/l: "))

if sp=="N":
    if hgb < 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hgb <= 175:
        print("Hemoglobiinitaso on normaali")
    else: print ("hemoglobiiniarvo on korkea")
elif sp=="M":
    if hgb < 134: 
        print("Hemoglobiiniarvo on alhainen")
    elif hgb <= 195:
        print("Hemoglobiinitaso on normaali")
    else: print("Hemoglobiiniarvo on korkea")
