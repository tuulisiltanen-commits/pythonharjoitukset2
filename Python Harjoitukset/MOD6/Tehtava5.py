def karsi_parittomat(lista) :
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:          
            uusi_lista.append(luku)
    return uusi_lista
alkuperainen = [4,5,6,58,2,6,7]
karsittu = karsi_parittomat(alkuperainen)
print("Alkuperäinen lista:", alkuperainen)
print("Karsittu lista:    ", karsittu)