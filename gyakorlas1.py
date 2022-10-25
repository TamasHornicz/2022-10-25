import math

x1 = float(input("Adja meg az első pontot az x tengelyen: ")) 
y1 = float(input("Adja meg az első pontot az y tengelyen: ")) 
x2 = float(input("Adja meg a második pontot az x tengelyen: ")) 
y2 = float(input("Adja meg a második pontot az y tengelyen: ")) 

xnegyzet = math.pow(x2 - x1,2)
ynegyzet = math.pow(y2 - y1,2)
osszeg = xnegyzet + ynegyzet
vegeredmeny = math.sqrt(osszeg)

print(vegeredmeny)