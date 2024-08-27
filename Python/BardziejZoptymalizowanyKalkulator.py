import sys
import sympy
class Kalkulator():

    def dodawanie(self,a,b):
        return a + b
    
    
    def odejmowanie(self,a,b):
        return a - b

    def mnoz(self,a,b):
        return a * b

    def dziel(self,a,b):
        while True:
            if b < 1:
                print('BLAD!\n')
                b = float(input('Podaj liczbę b: '))
            else:
                return a / b
                
    def pot(self,a,b):
        return a ** b
        
    def pierw(self,a,b):

        return a ** (1/b)

    def zaokr(self,a):
        while True:
            answer_zaokraglanie = input("Czy chcesz dokładnie zaokrąglić liczbę (WPISZ \"JA\"), czy ma to zrobić program (WPISZ \"PROGRAM\") :")


            if answer_zaokraglanie.lower() == 'ja':

                if_przecinek = input("\n Chcesz zaokrąglić liczbę by przecinek miał ZOSTAC czy ma ZNIKNAC: ")

                if if_przecinek.lower() == 'zostac':
            
                    how_many = int(input("\n Ile miejsc po przecinku ma być: "))

                    rounded = round(a, how_many)

                    return rounded

                elif if_przecinek.lower() == 'zniknac':

                    print("\n1. Jedności.")
                    print("2. Dziesiątek.")
                    print("3. Setek")
                    print("4. Tysięcy")
                    print("5. Dziesiątek tysięcy")
                    print("6. Setek tysięcy.")
                    print("7. Miliona.")

                    how_many = int(input("Zaokrąglić do : "))

                    if how_many > 7 or how_many <= 0:
                        print("BŁĄD! PODAJ POPRAWNĄ LICZBĘ")
                    else:
                        
                        rounded = round(a, (-how_many))
                        return rounded
            
            elif answer_zaokraglanie.lower() == 'program':
                

                if (a - int((a)) == 0):
                    rounded = round(a / 10) * 10
                    return rounded
                else:
                    rounded = round(a, 2)
                    return rounded

            else:
                print("BŁĄD! PODAJ POPRAWNĄ LICZBĘ")




kalk = Kalkulator()




print("""Witaj!
To jest mój zaawansowany kalkulator, który jest stale rozwijany!
""")

print("1. Dodawanie.")
print("2. Odejmowanie.")
print("3. Mnożenie.")
print("4. Dzielenie.")
print("5. Potęgowanie")
print("6. Pierwiastkowanie.")
print("7. Zaokrąglanie.")
print('8. Działania niestandardowe.')

while True:
    choice = int(input('Co chcesz zrobić: '))

    if choice < 1 or choice > 8:
        print('BLAD')
    else:
        break

if choice == 1:
    a = float(input('Podaj liczbę a: '))
    b = float(input('Podaj liczbę b: '))
    answer = kalk.dodawanie(a,b)
    print(f'Twoj wynik to: {answer}')

elif choice == 2:
    a = float(input('Podaj liczbę a: '))
    b = float(input('Podaj liczbę b: '))
    answer = kalk.odejmowanie(a,b)
    print(f'Twoj wynik to: {answer}')

elif choice == 3:
    a = float(input('Podaj liczbę a: '))
    b = float(input('Podaj liczbę b: '))
    answer = kalk.mnoz(a,b)
    print(f'Twoj wynik to: {answer}')

elif choice == 4:
    a = float(input('Podaj liczbę a: '))
    b = float(input('Podaj liczbę b: '))
    answer = kalk.dziel(a,b)
    print(f'Twoj wynik to: {answer}')

elif choice == 5:
    a = float(input("Podaj podstawę potęgi: "))
    b = float(input("Podaj wykładnik potęgi: "))
    answer = kalk.pot(a,b)
    print(f'Twoj wynik to: {answer}')

elif choice == 6:
    a = float(input("Podaj liczbę podpierwiastkową: "))
    b = float(input("Podaj stopień pierwiastka: "))
    answer = kalk.pierw(a,b)
    print(f'Twoj wynik to: {answer}')

elif choice == 7:
    a = float(input("Podaj liczbę, którą będziemy zaokrąglać: "))
    rounded = kalk.zaokr(a)
    print(f'Twoja zaokrąglona liczba to: {rounded}')

elif choice == 8:
    
    dzialanie = input('Podaj dzialanie: ')
    print(sympy.sympify(dzialanie))
  




    
    
