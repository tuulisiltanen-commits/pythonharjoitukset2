from math import sqrt
while True:
    luku = int(input("anna kokonaisluku"))
    if luku < 0:
        print("virheellinen luku")
    elif luku == 0:
        break
    else:
        print(sqrt(luku))