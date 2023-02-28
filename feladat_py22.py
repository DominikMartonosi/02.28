print("Adj meg egy 'a' betűvel kezdődő szót! Ha nem 'a' betűvel kezdődik, akkor nem kerül a listára.")

szavak = []

while True:
    szó = input("Add meg az 'a' betűvel kezdődő szót: ")
    if szó == "":
        break
    elif szó[0] == "a":
        szavak.append(szó)
for szó in szavak:
    print(szó)