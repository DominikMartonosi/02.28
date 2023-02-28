print("Adj meg egy 'a' betűvel kezdődő szót! Ha nem 'a' illetve 'A' betűvel kezdődik, akkor kimarad a listából.")

szavak = []

while True:
    szo = input("Add meg egyA 'a' betűvel kezdődő szót: ")
    if szo == "":
        break
    elif szo[0] == "a":
        szavak.append(szo)
    elif szo[0] == "A":
        szavak.append(szo)
for szo in szavak:
    print(szo)