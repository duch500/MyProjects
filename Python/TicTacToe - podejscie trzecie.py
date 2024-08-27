import random
tablicaKolkoKrzyzyk = ['-','-','-',
                       '-','-','-',
                       '-','-','-']




def WypisanieListy(tablicaKolkoKrzyzyk):
    print('  ' +tablicaKolkoKrzyzyk[0] + ' | ' + tablicaKolkoKrzyzyk[1] + ' | ' + tablicaKolkoKrzyzyk[2])
    print('--------------')
    print('  ' +tablicaKolkoKrzyzyk[3] + ' | ' + tablicaKolkoKrzyzyk[4] + ' | ' + tablicaKolkoKrzyzyk[5])
    print('--------------')
    print('  ' +tablicaKolkoKrzyzyk[6] + ' | ' + tablicaKolkoKrzyzyk[7] + ' | ' + tablicaKolkoKrzyzyk[8])


def WyborGracza(tablicaKolkoKrzyzyk):

    playerInp = int(input('Podaj liczbę od 1-9: '))

    if tablicaKolkoKrzyzyk[playerInp-1] =='-':
        tablicaKolkoKrzyzyk[playerInp-1] = aktualnyGracz 
    else:
        print("To miejsce jest zajęte! Spadaj!")   


def wygranaPoziom(tablicaKolkoKrzyzyk):
    global wygrany
    if tablicaKolkoKrzyzyk[0] == tablicaKolkoKrzyzyk[1] == tablicaKolkoKrzyzyk[2] and tablicaKolkoKrzyzyk[0] != '-':
        wygrany = tablicaKolkoKrzyzyk[1]
        return True
    elif tablicaKolkoKrzyzyk[3] == tablicaKolkoKrzyzyk[4] == tablicaKolkoKrzyzyk[5] and tablicaKolkoKrzyzyk[3] != '-':
        wygrany = tablicaKolkoKrzyzyk[3]
        return True
    elif tablicaKolkoKrzyzyk[6] == tablicaKolkoKrzyzyk[7] == tablicaKolkoKrzyzyk[8] and tablicaKolkoKrzyzyk[6] != '-':
        wygrany = tablicaKolkoKrzyzyk[6]
        return True


def wygranaPion(tablicaKolkoKrzyzyk):
    global wygrany
    if tablicaKolkoKrzyzyk[0] == tablicaKolkoKrzyzyk[3] == tablicaKolkoKrzyzyk[6] and tablicaKolkoKrzyzyk[0] != '-':
        wygrany = tablicaKolkoKrzyzyk[0]
        return True
    elif tablicaKolkoKrzyzyk[1] == tablicaKolkoKrzyzyk[4] == tablicaKolkoKrzyzyk[7] and tablicaKolkoKrzyzyk[1] != '-':
        wygrany = tablicaKolkoKrzyzyk[1]
        return True
    elif tablicaKolkoKrzyzyk[2] == tablicaKolkoKrzyzyk[5] == tablicaKolkoKrzyzyk[8] and tablicaKolkoKrzyzyk[2] != '-':
        wygrany = tablicaKolkoKrzyzyk[2]
        return True


def wygranaKos(tablicaKolkoKrzyzyk):
    global wygrany
    if tablicaKolkoKrzyzyk[0] == tablicaKolkoKrzyzyk[4] == tablicaKolkoKrzyzyk[8] and tablicaKolkoKrzyzyk[0] != '-':
        wygrany = tablicaKolkoKrzyzyk[0]
        return True
    elif tablicaKolkoKrzyzyk[2] == tablicaKolkoKrzyzyk[4] == tablicaKolkoKrzyzyk[6] and tablicaKolkoKrzyzyk[2] != '-':
        wygrany = tablicaKolkoKrzyzyk[2]
        return True
    

def RemisCzy(tablicaKolkoKrzyzyk):
    global checiDoGrania
    if '-' not in tablicaKolkoKrzyzyk:
        WypisanieListy(tablicaKolkoKrzyzyk)
        print('Remis!')
        checiDoGrania = False


def CzyWygrana(tablicaKolkoKrzyzyk):
    global checiDoGrania
    if wygranaPoziom(tablicaKolkoKrzyzyk):
        WypisanieListy(tablicaKolkoKrzyzyk)
        print(f"Wygranym jest {wygrany}!")
        checiDoGrania = False


    elif wygranaPion(tablicaKolkoKrzyzyk):
        WypisanieListy(tablicaKolkoKrzyzyk)
        print(f"Wygranym jest {wygrany}!")
        checiDoGrania = False


    elif wygranaKos(tablicaKolkoKrzyzyk):
        WypisanieListy(tablicaKolkoKrzyzyk)
        print(f"Wygranym jest {wygrany}!")
        checiDoGrania = False


def zmianaGracza():
    global aktualnyGracz
    if aktualnyGracz == 'X':
        aktualnyGracz = 'O'
    else:
        aktualnyGracz = 'X'


def Wygrana():
    global checiDoGrania
    if wygranaPoziom or wygranaPion or wygranaKos:
        print('Wygranym jest {wygrany}!')
        print('Koniec gry!')
        checiDoGrania = False

# def komputer(tablicaKolkoKrzyzyk):
#     global aktualnyGracz
#     randomChoice = random.randint(1,9)

#     if tablicaKolkoKrzyzyk[randomChoice-1] != '-':
#         tablicaKolkoKrzyzyk[randomChoice-1] = aktualnyGracz
#     else:
#         komputer(tablicaKolkoKrzyzyk)
    

########################################################

checiDoGrania = True
aktualnyGracz = 'X'
wygrany = None


while checiDoGrania:
    WypisanieListy(tablicaKolkoKrzyzyk)
    WyborGracza(tablicaKolkoKrzyzyk)
    CzyWygrana(tablicaKolkoKrzyzyk)
    RemisCzy(tablicaKolkoKrzyzyk)
    zmianaGracza()
    # komputer(tablicaKolkoKrzyzyk)
    # CzyWygrana(tablicaKolkoKrzyzyk)
    # RemisCzy(tablicaKolkoKrzyzyk)
    # zmianaGracza()


