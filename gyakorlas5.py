import random


hossz = int(input("Adja meg a hosszát: "))

for i in range(hossz):
    lista = [*range(-100, 100+1)]
    veletlen = random.choice(lista)
    print(veletlen)