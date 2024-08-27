
print("Jaki rodzaj ciagow cie interesuje:")

print('1. Arytmetyczny')
print('2. Geometryczny')
wybor_pass = True
while wybor_pass:
    first_Wybor = int(input("Co wybierasz (1-2): "))


    if first_Wybor > 2 or first_Wybor < 1:
        print('Błąd, jeszcze raz')
    else:
        break
        



if first_Wybor == 1:

    print('\nCo chcesz zrobić?')
    print("1. Podasz po przecinku liczby i znajde r, jesli ciag jest arytmetyczny.")
    print('2. Podasz wzor ogolny i znajde dany wyraz ciagu, ktory chcesz')
    print('3. Z podanych liczb po przecinku podam wzor ogolny i r')
    print('4. Zrobie wszystko na raz co powyzej')
    wybor_pass = True
    while wybor_pass:
        answer_ar = int(input("Co wybierasz (1-4): "))


        if answer_ar > 4 or answer_ar < 1:
            print('Błąd, jeszcze raz')
        else:
            break
    
    if answer_ar == 1:

        ciag_liczb = input('Podaj ciag liczb po przecinku (x,y,z):')
        ciag_liczb = ciag_liczb.split(',')
        r = (float(ciag_liczb[1]))-(float(ciag_liczb[0]))

        if len(ciag_liczb) < 2:
            print('Podano za mało liczb!')
        else:
            r = (float(ciag_liczb[1])) - (float(ciag_liczb[0]))
            for x in range(len(ciag_liczb)-1):
                if (float(ciag_liczb[x+1])) - (float(ciag_liczb[x])) == r:
                    continue
                else:
                    print('Ciąg nie jest arytmetyczny!')
                    break
            else:
                print('Ciąg jest arytmetyczny!')
                print(f'r jest równe {r}')

    elif answer_ar == 2:

        wzor_ogolny = input('Podaj wzor ogolny (3*n+2): ')

        wyraz_ciagu = int(input('Podaj ktory wyraz ciagu obliczyc:'))

        wynik = eval(wzor_ogolny, {'n': wyraz_ciagu})
        print(f'Na {wyraz_ciagu} miejscu znajduje się liczba {wynik}')

    elif answer_ar == 3:

        ciag_liczb3 = input('Podaj ciag liczb po przecinku (x,y,z):')
        ciag_liczb3 = ciag_liczb3.split(',')

        roznica = (float(ciag_liczb3[1]))-(float(ciag_liczb3[0]))
        
        print(f'Wzor ogolny jest rowny: Un = {float(ciag_liczb3[0])} * (n-1) * {roznica}')
        print(f'Roznica jest rowna: {roznica}')
        

