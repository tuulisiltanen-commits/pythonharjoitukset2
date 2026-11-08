import random
def heita_noppaa(tahkojen_maara):
    return random.randint(1,tahkojen_maara)
maksimi = int(input("anna tahkojen maara"))
while True:
    silmaluku = heita_noppaa(maksimi)
    print(silmaluku)
    if silmaluku == maksimi:
        break