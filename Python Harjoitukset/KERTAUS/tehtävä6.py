lista = []

while True:
    arvo = int(input("anna arvo"))
    if arvo == 0:
        break
    
    lista.append(arvo)
    print("lisäysjärjestyksessä", lista)
    print("pienimmästä suurimpaan", sorted(lista))
