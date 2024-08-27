'''
def wypiszTablice(tablica):

    for row in tablica:
        print("".join(row))



dlugISzerPlanszy = int(input('Podaj dlugosc planszy: '))
liczbaPrzekasek = int(input('Ile chcesz przekasek: '))
liczbaPolecen =int(input('Podaj ile chcesz polecen: '))


tablica = []
newtab = []

for x in range(1,dlugISzerPlanszy):
    newtab = []
    for y in range(1,dlugISzerPlanszy):
        newtab.append(".")
    tablica.append(newtab)


waz = [(0,0)]
tablica[0][0] = '0'



y = 0
while y != liczbaPrzekasek:

    w = input('Podaj wiersz: ')
    k =  input('Podaj kolumne: ')
    kolor = input('Podaj kolor: ')
    print('\n')

    


    tablica[int(w)-1][int(k)-1] = kolor
    y+=1




HelpLiczenieLiczbaPol = 0
while HelpLiczenieLiczbaPol != liczbaPolecen:
    wypiszTablice(tablica)

    polecenie = input('Podaj polecenie: ').upper()
    


    if 'Z' in polecenie:

        polecenie = polecenie.split()
        if tablica[int(polecenie[1])-1][int(polecenie[2])-1] == '.':
            print(-1)
        
            
        else:
            print(int(tablica[int(polecenie[1])-1][int(polecenie[2])-1]))
        polecenie = ' '.join([str(elem) for elem in polecenie])

        polecenie = str(polecenie)
        
    elif "G" in polecenie or "P" in polecenie or "D" in polecenie or "L" in polecenie:
        i = "GPDL".index(polecenie)
        dWiersz, dKolumna = ((-1,0), (0, 1), (1,0), (0,-1))[i]
        nextWiersz = waz[0][0] + dWiersz
        nextKol = waz[0][1] + dKolumna
        # if not (0 <= nextWiersz < len(tablica)) or not (0 <= nextKol < len(tablica[0])):
        #     print('Zle wejscie')
            
        #     continue
        waz.insert(0, (nextWiersz, nextKol))

        if tablica[nextWiersz][nextKol] == '.':

            for (nextWiersz, nextKol), (preWiersz, preKol) in zip(waz, waz[1:]):
                tablica[nextWiersz][nextKol] = tablica[preWiersz][preKol]
            
            delWiersz, delKol = waz.pop()
            tablica[delWiersz][delKol] ='.'

    HelpLiczenieLiczbaPol+=1
    

        
    
'''
#JAKO LISTA
def wypiszTablice(tablica):

    for row in tablica:
        print("".join(row))



pierwszeTrzy = input('Podaj dlugosc planszy: ').split()

dlugISzerPlanszy = int(pierwszeTrzy[0])
liczbaPrzekasek = int(pierwszeTrzy[1])
liczbaPolecen = int(pierwszeTrzy[2])


tablica = []
newtab = []

for x in range(1,dlugISzerPlanszy+1):
    newtab = []
    for y in range(1,dlugISzerPlanszy+1):
        newtab.append(".")
    tablica.append(newtab)


waz = [(0,0)]
tablica[0][0] = '0'



y = 0

while y != liczbaPrzekasek:

    
    wszystko = input('Podaj koordynaty: ').split()

    w = wszystko[0]
    k = wszystko[1]
    kolor = wszystko[2]

    # print(w)
    # print(k)
    # print(kolor)
    # print(y)
   # wypiszTablice(tablica)
    tablica[int(w)-1][int(k)-1] = kolor
    y+=1



odpowiedzi = []
HelpLiczenieLiczbaPol = 0

while HelpLiczenieLiczbaPol != liczbaPolecen:
    wypiszTablice(tablica)

    polecenie = input('Podaj polecenie: ').upper()
    


    if 'Z' in polecenie:

        polecenie = polecenie.split()
        if tablica[int(polecenie[1])-1][int(polecenie[2])-1] == '.':
       
            #print(-1)  
            odpowiedzi.append(-1)
        
            
        else:
            #print(int(tablica[int(polecenie[1])-1][int(polecenie[2])-1]))
            odpowiedzi.append(int(tablica[int(polecenie[1])-1][int(polecenie[2])-1]))
            
        polecenie = ' '.join([str(elem) for elem in polecenie])

        polecenie = str(polecenie)
        
    elif "G" in polecenie or "P" in polecenie or "D" in polecenie or "L" in polecenie:
        i = "GPDL".index(polecenie)
        dWiersz, dKolumna = ((-1,0), (0, 1), (1,0), (0,-1))[i]
        nextWiersz = waz[0][0] + dWiersz
        nextKol = waz[0][1] + dKolumna

        waz.insert(0, (nextWiersz, nextKol))

        if tablica[nextWiersz][nextKol] == '.':

            for (nextWiersz, nextKol), (preWiersz, preKol) in zip(waz, waz[1:]):
                tablica[nextWiersz][nextKol] = tablica[preWiersz][preKol]
            
            delWiersz, delKol = waz.pop()
            tablica[delWiersz][delKol] ='.'

    HelpLiczenieLiczbaPol+=1
    
for num in odpowiedzi:
    print(num)
