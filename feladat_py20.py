lista = []
nev = None
while nev != "":
    nev = input("Adj meg egy keresztnevet! ")
    lista.append(nev)
print(*lista, sep="\n")