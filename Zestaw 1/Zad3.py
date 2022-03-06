# Zadanie 3.
#
# Proszę napisać program sprawdzający czy istnieje spójny podciąg
# ciągu Fibonacciego o zadanej sumie.


if __name__ == '__main__':
    spr = int(input("Podaj sumę do sprawdzenia: "))

    a, na = 0, 1
    b, nb = 0, 1
    suma = 0

    znal = False
    while a <= b <= suma:
        if suma < spr:
            suma += nb
            b, nb = nb, b+nb
        elif suma > spr:
            suma -= a
            a, na = na, a+na
        else:
            znal = True
            break
    
    if znal:
        print("Istnieje spójny podciąg o zadanej sumie")
    else:
        print("Nie istnieje spójny podciąg o zadanej sumie")
