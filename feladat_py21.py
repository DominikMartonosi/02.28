lista = []
count = 0
nev = None
while nev != "":
    nev = input("Adj meg egy keresztnevet! ")
    count += 1
    lista.append(nev)
    if count == 3:
        print("Elérted a max nevet!")
        break
print(*lista, sep="\n")
