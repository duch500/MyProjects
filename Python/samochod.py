


class ErrorTest(Exception):
    pass

class samochod:

    
    def __init__(self, silnik, bieg, predkosc):


        self.silnik = silnik
        self.bieg = bieg
        self.predkosc = predkosc
        

    def wlaczSilnik(self):
        
        if self.silnik == True:
            print('Silnik jest już włączony!')
        elif self.silnik == False:
            print('Silnik został włączony')
            self.silnik = True

        else:
            print('Wystąpił dziwny błąd!')
        
        

    def biegUp(self):

        if self.silnik != True:
            print('Silnik nie jest włączony. Włącz silnik.')
        elif self.silnik == True:

            if self.bieg == 6:
                print(f'Osięgnięto bieg maksymalny z prędkością {self.predkosc}km/h!')
            else:
                self.bieg = self.bieg + 1
                self.predkosc += 30
                print(f'Jedziesz na biegu {self.bieg} z zawrotną prędkością {self.predkosc} km/h')

    def biegDown(self):

        if self.silnik != True:
            print('Silnik nie jest włączony. Włącz silnik.')
        elif self.silnik == True:

            if self.bieg == 0:
                print(f'Zatrzymałeś się!')
            elif self.bieg <= 0:
                print('Nie da się niżej zejść!')
            else:
                self.bieg = self.bieg - 1
                self.predkosc -= 30
                print(f'Jedziesz na biegu {self.bieg} z zawrotną prędkością {self.predkosc} km/h')

    def wylaczSilnik(self):

        if self.silnik == False:
            print('Silnik jest już wyłączony!')
        elif self.silnik == True:
            print('Silnik został wyłączony')
            self.silnik = False

        else:
            print('Wystąpił dziwny błąd')
            

ferrari = samochod(False, 0, 0)

'''
Wybor komend:

ferrari.wlaczSilnik()
ferrari.wylaczSilnik()

ferrari.biegUp()
ferrari.biegDown()
    
'''
petla = True
print('1. Wlacz silnik.')
print('2. Wylacz silnik')
print('3. Zwieksz predkosc - bieg')
print('4. Zmniejsz predkosc - bieg')
print('5. KONIEC PROGRAMU')
print('\n')
while petla:
    choice = int(input('>>>'))

    if choice < 1 or choice > 5:
        print('BŁĄD! Podaj poprawną liczbę!')
    elif choice == 1:
        ferrari.wlaczSilnik()
    elif choice == 2:
        ferrari.wylaczSilnik()
    elif choice == 3:
        ferrari.biegUp()
    elif choice == 4:
        ferrari.biegDown()
    elif choice == 5:
        print('\n Koniec programu')
        petla = False



        







