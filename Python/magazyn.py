## Magazyn produktów

class magazyn:

    def __init__(self, listaProduktow):
        
        self.listaProdktow = listaProduktow

        
                



    def sprawdzListe(self):
        print('Twoje produkty w magazynie: ')
        for produkt in self.listaProdktow:
            print(f'{produkt}')

        if len(self.listaProdktow) == 0:
            print('\nBrak produktów w magazynie!')

    def dodajProdukt(self):

        
        self.nowyProd = input("Podaj produkt, który chcesz dodać >>>> ")

        if self.nowyProd not in self.listaProdktow:
            self.listaProdktow.append(self.nowyProd)
            print(f'Produkt {self.nowyProd} został dodany do magazynu!')

        else:
            print("Wystąpił błąd lub produkt jest już w magazynie")


    def usunProdukt(self):

        self.usuwanieProd = input("Jaki produkt chciał*byś usunąć >>>> ")

        if self.usuwanieProd in self.listaProdktow:
            self.listaProdktow.remove(self.usuwanieProd)
            print(f'Produkt {self.usuwanieProd} został usunięty z magazynu!')
        else:
            print('Nie ma takiego produktu w magazynie!')

    
    def zapiszDoPliku(self):

        print('Zapisywanie do pliku, zaczekaj')

        with open('lista zakupow.txt', 'a') as plik:
            plik.write('Twoj stan magazynu: \n')
            for produkt in self.listaProdktow:
                plik.write(f'{produkt} \n')

        print('\n Plik został zapisany')

stwierdzenie = True
magazyn1 = magazyn([])
print('*'*10)
while stwierdzenie == True:
            
    
    print('')
    print('Wybierz NUMER co chcesz zrobić w magazynie!')
    print('1. Sprawdzić stan magazynu.')
    print('2. Dodać produkt do magazynu.')
    print('3. Usunąć produkt z magazynu.')
    print('4 Przenieść magazyn do pliku tesktowego.')
    print('5. Zakończyć program.')

    wyborUzytkownika = int(input('Wybierz co chcesz zrobić: '))

    if wyborUzytkownika < 1 or wyborUzytkownika > 5:
        print('Błąd, wpisz poprawną liczbę')
    elif wyborUzytkownika == 1:
        magazyn1.sprawdzListe()
    elif wyborUzytkownika == 2:
        magazyn1.dodajProdukt()
    elif wyborUzytkownika == 3:
        magazyn1.usunProdukt()
    elif wyborUzytkownika == 4:
        magazyn1.zapiszDoPliku()
    elif wyborUzytkownika == 5:
        print('\nProgram zakończony')
        break

                


    
