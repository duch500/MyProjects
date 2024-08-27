# SCHEMAT BERNOUILEGO

def sil(s):
    w = 1
    while s != 0:
        w = w * s
        s= s - 1
    return w


print('Podasz teraz pare wartości:')

while True:

    n = int(input("Podaj ilość prób: "))
    k = int(input('Wymagana ilość sukcesów: '))

    if k > n:
        print('Podaj poprawne wartości')
        continue
    else:
        break

while True:

    p = float(input('Prawdopodobieństwo pozytywne: '))
    q = 1 - p
    if p+q > 1:
        print('Podaj poprawne wartości')
        continue
    else:
        break

wynik = (sil(n)/(sil(k)*sil(n-k))) * (p**k) * (q **(n-k))

print(f'Prawdopodobieństwo tego zdarzenia wynosi {round(wynik, 2)}')
    