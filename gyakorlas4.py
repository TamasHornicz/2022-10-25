import random

print("A fej az 1-es, az írás a 2-es")
user = int(input("Írja beb hogy fej vagy írás: "))
gép =random.randint(1, 2)

if gép == user:
    print("Nyert")
else:
    print("Vesztett")

