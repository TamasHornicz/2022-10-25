import random

'''
hossz = int(input("Adja meg a hosszát: "))

for i in range(hossz):
    lista = [*range(-100, 100+1)]
    veletlen = random.choice(lista)
    print(veletlen)'''

N = int(input("Írja be hogy mennyi számot szeretne: "))

Lszamok= []

for i in range(N): 
    Lszamok.append(random.randint(-100, 100))

negativdb = 0

for szam in Lszamok:
    if(szam<0):
        negativdb+=1

print("Negatí számok száma:", negativdb)

print(max(Lszamok)-min(Lszamok))

Lszamok.sort()
Lszamok.reverse
print(Lszamok)
