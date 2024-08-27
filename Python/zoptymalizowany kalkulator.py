import math
import time
import os
import matplotlib.pyplot as plt
import numpy as np




def dodawanie():

    print("Twoim wynikiem jest ", variable_a + variable_b, ".")


def odejmowanie():
    print("Twoim wynikiem jest ", variable_a - variable_b, ".")


def mnożenie():
    if variable_a == 0 or variable_b == 0:
        print("Jedna z podanych zmiennych jest równa 0.")
    else:
        print("Twoim wynikiem jest ", variable_a * variable_b, ".")


def dzielenie():

    if variable_a == 0 or variable_b == 0:
        print("Jedna z podanych zmiennych jest równa 0.")
    else:
        print("Twoim wynikiem jest ", variable_a / variable_b, ".")


def potęgowanie():
    print("Twoim wynikiem jest ", variable_a1**variable_b1, ".")


def pierwiastkowanie():
    print("Twoim wynikiem jest ", (variable_a2**(1 / variable_b2)), ".")


def pole_kwadrat():
    if kwad_a <= 0:
        print("BŁĄD! BOK NIE MOŻE BYĆ RÓWNY 0 LUB WYNOSIĆ MNIEJ NIŻ 1!")
    else:
        if answer_second_question == 1:
            print("Pole twojego kwadratu wynosi ", (kwad_a**2), ".")
        elif answer_second_question == 2:
            print("Obwód twojego kwadratu wynosi ", (kwad_a * 4), ".")


def pole_prost():
    if pros_b <= 0 or pros_a <= 0:
        print("BŁĄD! BOK NIE MOŻE BYĆ RÓWNY 0 LUB WYNOSIĆ MNIEJ NIŻ 1!")
    else:
        if answer_second_question == 1:
            print("Pole twojego prostokąta wynosi ", (pros_a * pros_b), ".")
        elif answer_second_question == 2:
            print("Obwód twojego prostokąta wynosi ",
                  ((pros_a * 2) + (2 * pros_b)), ".")


def pole_rown():

    if answer_second_question == 1:

        rown_a = float(input("Podaj bok A: "))

        rown_h = float(input("Podaj wysokość: "))

        if rown_a <= 0 or rown_h <= 0:

            print(
                "BŁĄD! BOK LUB WYSOKOŚĆ NIE MOŻE BYĆ RÓWNY/A 0 LUB WYNOSIĆ MNIEJ NIŻ 1!"
            )

        else:

            print("Pole twojego równoległoboku wynosi ", (rown_a * rown_h),
                  ".")

    elif answer_second_question == 2:

        rown_a1 = float(input("Podaj bok A:"))

        rown_b = float(input("Podaj bok B:"))

        if rown_a1 <= 0 or rown_b <= 0:

            print(
                "BŁĄD! BOK LUB WYSOKOŚĆ NIE MOŻE BYĆ RÓWNY/A 0 LUB WYNOSIĆ MNIEJ NIŻ 1!"
            )

        else:

            print("Obwód twojego równoległoboku wynosi ",
                  2 * (rown_a1 + rown_b), ".")


def pole_trap():
    if answer_second_question == 1:

        trap_a = float(input("Podaj bok A: "))
        trap_b = float(input("Podaj bok B: "))
        trap_h = float(input("Podaj wysokość: "))

        if trap_a <= 0 or trap_b <= 0 or trap_h <= 0:
            print(
                "BŁĄD! BOKI LUB WYSOKOŚĆ NIE MOŻE BYĆ RÓWNY/A 0 LUB WYNOSIĆ MNIEJ NIŻ 1!"
            )
        else:
            print("Pole twojego trapeza wynosi ", ((trap_a + trap_b) / trap_h),
                  ".")

    elif answer_second_question == 2:

        trap_a = float(input("Podaj bok A: "))
        trap_b = float(input("Podaj bok B: "))
        trap_c = float(input("Podaj bok C: "))
        trap_d = float(input("Podaj bok D: "))

        if trap_a <= 0 or trap_b <= 0 or trap_c <= 0 or trap_d <= 0:
            print("BŁĄD! BOKI NIE MOGĄ BYĆ RÓWNE 0 LUB WYNOSIĆ MNIEJ NIŻ 1!")
        else:
            print("Obwód twojego trapeza wynosi ",
                  (trap_c + trap_b + trap_d + trap_a), ".")


def pole_romb():

    if answer_second_question == 1:

        answer_romb = input(
            "Chcesz obliczyć dzięki przekątnej czy dzięki wysokości: ")

        if answer_romb == 'przekątna' or answer_romb == 'przekątnej' or answer_romb == 'przekatna' or answer_romb == 'przekatnej':

            romb_przk1 = float(input("Podaj pierwszą przekątną: "))
            romb_przek2 = float(input("Podaj drugą przekątną: "))

            if romb_przk1 <= 0 or romb_przek2 <= 0:
                print(
                    "BŁĄD! PRZEKĄTNA NIE MOŻE BYĆ RÓWNA 0 LUB WYNOSIĆ MNIEJ NIŻ 1!"
                )
            else:
                print("Pole twojego rombu wynosi ",
                      (romb_przk1 * romb_przek2) / 2, ".")


## koniec przk ##########################################################################################################################

        elif answer_romb == 'wysokości' or answer_romb == 'wysokosci' or answer_romb == 'wysokość' or answer_romb == 'wysokosc':

            romb_a = float(input("Podaj bok A: "))
            romb_h = float(input("Podaj wysokosć: "))

            if romb_a <= 0 or romb_h <= 0:
                print(
                    "BŁĄD! BOK LUB WYSOKOŚĆ NIE MOŻE BYĆ RÓWNY/A 0 LUB WYNOSIĆ MNIEJ NIŻ 1!"
                )
            else:
                print("Pole twojego rombu wynosi ", (romb_a * romb_h), ".")
        else:
            print("BŁĄD! NIEPOPRAWNE WEJŚCIE")

    elif answer_second_question == 2:

        romb_a1 = float(input("Podaj bok A: "))

        if romb_a1 <= 0:
            print("BŁĄD! BOK NIE MOŻE BYĆ RÓWNY 0 LUB WYNOSIĆ MNIEJ NIŻ 1!")
        else:
            print("Obwód twojego rombu wynosi ", (4 * romb_a1), ".")


def pole_kola():

    radius = float(input("Podaj promień koła: "))

    if answer_second_question == 1:

        if radius <= 0:
            print(
                "BŁĄD! PROMIEŃ NIE MOŻE BYĆ RÓWNY 0 LUB WYNOSIĆ MNIEJ NIŻ 1!")
        else:

            pole_kola_wynik_rounded = round(((math.pi) * 2) * radius / 10) * 10
            pole_kola_wynik_not_rounded = round((((math.pi) * 2) * radius), 2)

            print("Pole twojego koła (w zaokrągleniu) wynosi ",
                  pole_kola_wynik_rounded, ".")
            print("")
            print("Pole twojego koła (dokładnie) wynosi ",
                  pole_kola_wynik_not_rounded, ".")

    elif answer_second_question == 2:
        # 2 * pi * r
        if radius <= 0:
            print(
                "BŁĄD! PROMIEŃ NIE MOŻE BYĆ RÓWNY 0 LUB WYNOSIĆ MNIEJ NIŻ 1!")
        else:

            obwod_kola_wynik_rounded = round(
                ((math.pi) * 2) * (2 * radius) / 10) * 10
            obwod_kola_wynik_not_rounded = round(
                (((math.pi) * 2) * (2 * radius)), 2)

            print("Pole twojego koła (w zaokrągleniu) wynosi ",
                  obwod_kola_wynik_rounded, ".")
            print("")
            print("Pole twojego koła (dokładnie) wynosi ",
                  obwod_kola_wynik_not_rounded, ".")


def pole_trojkat():

    if answer_second_question == 1:
        trojk_a = float(input("Podaj bok A: "))
        trojk_h = float(input("Podaj wysokość: "))
        if trojk_a <= 0 or trojk_h <= 0:
            print(
                "BŁĄD! BOKI LUB WYSOKOŚĆ NIE MOŻE BYĆ RÓWNY/A 0 LUB WYNOSIĆ MNIEJ NIŻ 1!"
            )
        else:
            print("Pole twojego trójkąta wynosi ", ((trojk_a * trojk_h) / 2),
                  ".")
    elif answer_second_question == 2:

        trap_a = float(input("Podaj bok A: "))
        trap_b = float(input("Podaj bok B: "))
        trap_c = float(input("Podaj bok C: "))

        if trap_a <= 0 or trap_b <= 0 or trap_c <= 0:
            print("BŁĄD! BOKI NIE MOGĄ BYĆ RÓWNE 0 LUB WYNOSIĆ MNIEJ NIŻ 1!")
        else:
            print("Obwód twojego trapeza wynosi ", (trap_c + trap_b + trap_a),
                  ".")


def delta():

    print("Wybrałeś Obliczanie delty!")

    delt_a = int(input("Podaj A: "))
    delt_b = int(input("Podaj B: "))
    delt_c = int(input("Podaj C: "))

    delta_bez_pier = (delt_b**2) - (4 * delt_a * delt_c)
    delta_bez_pier = float(delta_bez_pier)

    if delta_bez_pier < 0:
        print(f'Twoja delta jest ujemna i wynosi: {delta_bez_pier}')
    elif delta_bez_pier == 0:
        print(f'Twoja delta jest równa 0.')
    else:

        delta_pier = math.sqrt(delta_bez_pier)
        delta_pier = float(delta_pier)



        print("Twoja delta wynosi: ", delta_bez_pier, ".")
        print("")
        print("Twoja delta pod pierwiastkiem wynosi: ",
                round(delta_pier, 2), ".")

def miejscaZerowe():
    print("Wybrałeś obliczanie miejsc zerowych, ale najpierw daj delte!")

    delt_a = int(input("Podaj A: "))
    delt_b = int(input("Podaj B: "))
    delt_c = int(input("Podaj C: "))

    delta_bez_pier = (delt_b**2) - (4 * delt_a * delt_c)
    delta_bez_pier = float(delta_bez_pier)

    if delta_bez_pier < 0:
        print(f'Twoja delta jest ujemna i wynosi: {delta_bez_pier}. Nie ma miejsc zerowych!')
    elif delta_bez_pier == 0:

        zerowe0 = -(delt_b) / 2 * delt_a

        print(f'Twoja delta jest równa 0 - ma jedno miejsce zerowe, które jest równe: {zerowe0}')

    else:

        delta_pier = math.sqrt(delta_bez_pier)
        delta_pier = float(delta_pier)



        print("Twoja delta wynosi: ", delta_bez_pier, ".")
        print("")
        print("Twoja delta pod pierwiastkiem wynosi: ",
                round(delta_pier, 2), ".")
            
        print('\n Teraz obliczymy miejsca zerowe!')
        
        zerowe1 = (-delt_b) - delta_pier / ( 2 * delt_a) ## Obliczanie miejsc zerowych
        zerowe2 = (-delt_b) + delta_pier / ( 2 * delt_a)

        print(f'Miejsce zerowe x1 = {zerowe1}.')
        print(f'Miejsce zerowe x2 = {zerowe2}.')
    




###################################################################################

print("Hej! Jestem zaawansowanym kalkulatorem stworzonym przez Macieja.")
print("Wybierz sekcję by przejść dalej:")

print("1. Podstawowe działania.")
print("2. Wzory.")
print("3. W budowie")

answer_first = int(input("Podaj cyfrę sekcji: "))
print("\n")
if answer_first > 3 or answer_first <= 0:
    print("BŁĄD! NIE MOŻESZ PODAĆ CYFRY WIĘKSZEJ LUB MNIEJSZEJ NIŻ PODANE.")
else:

    if answer_first == 1:
        print("Super!")
        print("")
        print("1. Dodawanie.")
        print("2. Odejmowanie.")
        print("3. Mnożenie.")
        print("4. Dzielenie.")
        print("5. Potęgowanie")
        print("6. Pierwiastkowanie.")
        print("7. Zaokrąglanie.")
        print("")

        answer_equation = input("Wybierz działanie: ")
        print("\n")
        if answer_equation == '1' or answer_equation == '2' or answer_equation == '3' or answer_equation == '4':
            variable_a = float(input("Podaj pierwszą liczbę: "))
            variable_b = float(input("Podaj druga liczbę: "))

            if answer_equation == '1':
                dodawanie()
            elif answer_equation == '2':
                odejmowanie()
            elif answer_equation == '3':
                mnożenie()
            elif answer_equation == '4':
                dzielenie()

        if answer_equation == '5':
            variable_a1 = float(input("Podaj podstawę potęgi: "))
            variable_b1 = float(input("Podaj wykładnik potęgi: "))
            print("\n" * 10)
            potęgowanie()

        elif answer_equation == '6':
            variable_a2 = float(input("Podaj liczbę podpierwiastkową: "))
            variable_b2 = float(input("Podaj stopień pierwiastka: "))
            print("\n")
            pierwiastkowanie()

        elif answer_equation == '7':

            answer_zaokraglanie = input(
                "Czy chcesz dokładnie zaokrąglić liczbę (WPISZ \"JA\"), czy ma to zrobić program (WPISZ \"PROGRAM\") :"
            )

            if answer_zaokraglanie == 'Ja' or answer_zaokraglanie == 'JA' or answer_zaokraglanie == 'ja':
                print("\n " * 2)
                variable_one = float(
                    input("Podaj liczbę całkowitą, którą chcesz zaokrąglić: "))
                print("")
                if_przecinek = input(
                    "Chcesz zaokrąglić liczbę by przecinek miał zostać czy ma zniknąć: "
                )

                if if_przecinek == 'zostac' or if_przecinek == 'Zostać' or if_przecinek == 'zostać' or if_przecinek == 'Zostac':
                    print("")
                    how_many = int(input("Ile miejsc po przecinku ma być?"))
                    print("")
                    print("Twoja zaokrąglona liczba to: ",
                          round(variable_one, how_many), ".")

                elif if_przecinek == 'zniknac' or if_przecinek == 'Zniknac' or if_przecinek == 'zniknąć' or if_przecinek == 'Zniknąć':
                    print("")
                    print("1. Jedności.")
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

                        print("")
                        print("Twoja zaokrąglona liczba to: ",
                              round(variable_one, (-how_many)), ".")

            elif answer_zaokraglanie == 'program' or answer_zaokraglanie == 'PROGRAM' or answer_zaokraglanie == 'Program':
                variable_one = float(
                    input("Podaj liczbę całkowitą, którą chcesz zaokrąglić: "))

                if (variable_one - int((variable_one)) == 0):
                    rounded = round(variable_one / 10) * 10
                    print("Liczba jest całkowita, a jej zaokrąglenie to: ",
                          rounded, ".")
                else:
                    print("Twoja zaokrąglona liczba to: ",
                          round(variable_one, 2), ".")

            else:
                print("BŁĄD! PODAJ POPRAWNĄ LICZBĘ")



#####################################################

    elif answer_first == 2:
        print("Super!")
        print("1. Pola figur.")
        print("2. Obwód figur.")
        print("3. Pitagoras.")
        print("4. Delta.")
        print("5. Miejsca zerowe.")
        print('6. Wykresy')
######################################################
        answer_second_question = int(input("Co wybierasz : "))
        print("\n")
        if answer_second_question > 6 or answer_second_question <= 0:
            print("Wybierz poprawną opcję!")
        else:

            if answer_second_question == 1:
                print("Wybrałeś pola figur!")
                print("")
                print("1. Kwadrat.")
                print("2. Prostokąt")
                print("3. Równoległobok.")
                print("4. Trapez")
                print("5. Romb.")
                print("6. Koło.")
                print("7. Trójkąt.")
                print("")
                answer_pola_figura = int(
                    input("Pole której figury chcesz obliczyć: "))
                print("\n")

                if answer_pola_figura > 7 or answer_pola_figura <= 0:
                    print("Wybierz poprawną opcję!")

                elif answer_pola_figura == 1:
                    kwad_a = float(input("Podaj bok kwadratu: "))
                    pole_kwadrat()

                elif answer_pola_figura == 2:
                    pros_a = float(input("Podaj bok A: "))
                    pros_b = float(input("Podaj bok B: "))
                    pole_prost()

                elif answer_pola_figura == 3:
                    pole_rown()

                elif answer_pola_figura == 4:
                    pole_trap()

                elif answer_pola_figura == 5:
                    pole_romb()

                elif answer_pola_figura == 6:

                    pole_kola()

                elif answer_pola_figura == 7:
                    trojk_a = float(input("Podaj bok A: "))
                    trojk_h = float(input("Podaj wysokość: "))
                    pole_trojkat()

##################################

            elif answer_second_question == 2:

                print("Wybrałeś obwód figur!")
                print("")
                print("1. Kwadrat.")
                print("2. Prostokąt")
                print("3. Równoległobok.")
                print("4. Trapez")
                print("5. Romb.")
                print("6. Koło.")
                print("7. Trójkąt.")
                print("")
                answer_obj_figura = int(
                    input("Obwód której figury chcesz obliczyć: "))

                if answer_obj_figura > 7 or answer_obj_figura <= 0:
                    print("Wybierz poprawną opcję!")

                elif answer_obj_figura == 1:
                    kwad_a = float(input("Podaj bok kwadratu: "))
                    pole_kwadrat()

                elif answer_obj_figura == 2:
                    pros_a = float(input("Podaj bok A: "))
                    pros_b = float(input("Podaj bok B: "))
                    pole_prost()

                elif answer_obj_figura == 3:
                    pole_rown()

                elif answer_obj_figura == 4:

                    pole_trap()

                elif answer_obj_figura == 5:
                    pole_romb()

                elif answer_obj_figura == 6:
                    pole_kola()

                elif answer_obj_figura == 7:
                    pole_trojkat()

            elif answer_second_question == 3:
                print("Wybrałeś obliczanie pitagorasa!")
                print("Wzór to a2 + b2 = c2")

                pit_ans = input("Czy znasz wszystkie przyprostokątne: ")

                if pit_ans == 'tak' or pit_ans == 'Tak' or pit_ans == 'TAK':

                    przyp_a = int(input("Podaj przyprostokątną A: "))
                    przyp_b = int(input("Podaj przyprostokątną B: "))
                    print("")
                    przeciw_tak = math.sqrt(przyp_a**2 + przyp_b**2)

                    print("Twoja przeciwprostokątna wynosi: ", przeciw_tak,
                          ".")

                elif pit_ans == 'nie' or pit_ans == 'Nie' or pit_ans == 'NIE':
                    print(
                        "Zakładam, że znasz jedną przypostokątną i przyprostokątną."
                    )

                    przeciw = int(input("Podaj przeciwprostokątną: "))
                    przyp = int(input("Podaj przyprostokątną: "))

                    expr = (przeciw**2 - przyp**2)

                    expr = math.sqrt(expr)

                    print("Twoja przypostokątna wynosi ", expr, ".")

            elif answer_second_question == 4:
                delta()

            elif answer_second_question == 5:
                miejscaZerowe()

            elif answer_second_question == 6:
                x = np.linspace(0, 2 * np.pi, 200)
                y = np.sin(x)

                fig, ax = plt.subplots()
                ax.plot(x, y)
                plt.show()
            



    elif answer_first == 3:
        print('')
################################koniec
