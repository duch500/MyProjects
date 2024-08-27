import os
def WypiszEnc(encrypted):
    for y in encrypted:
        print(y, end=" ")
    print('')


def containsNumber(wisielec):
    for character in wisielec:
        if character.isdigit():
            print('PODAJ POPRAWNE HASLO, BEZ LICZB\n')
            return True
    return False


while True:
    wisielec = input('Podaj haslo do wisielca: ').lower()

    check = containsNumber(wisielec)

    if check == True:
        continue
    else:
        break

os.system('cls')
print('ZGADUJ!')
wisielecPelne = wisielec
wisielec = list(wisielec)

encrypted = []

for x in range(len(wisielec)):
    encrypted.append('_')

WypiszEnc(encrypted)
import os

h = 10

while True:
    litera = input("Podaj litere: ").lower()

    if wisielec == encrypted or litera == wisielecPelne:
        print('Wygrales!')
        break

    elif litera in wisielec:
        for x in range(len(wisielec)):

            if litera == wisielec[x]:
                encrypted[x] = wisielec[x]

        WypiszEnc(encrypted)
        if wisielec == encrypted or litera == wisielecPelne:
            print('Wygrales!')
            break
        

    
    else:
        h -= 1
        print(f'Nic sie nie zmienilo, pozostalo Ci {h} ruchow')

    if h == 0:
        print('\n Zostałaś powieszona\y')
        break