# Zadanie 5.
#
# Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.

# Zaczynamy od prostokąta: 1 x kw i tak zmieniamy długości boków, aby otrzymać kwadrat.
# Boki oznaczamy: a i b. W każdej iteracji jeden bok zostaje średnią artmetyczną boków
# poprzedniego porstokąta: a = (a+b)/2, a drugi tak aby pole prostokąta wynosiło ciągle
# kw, czyli b = kw/a    /Paweł


if __name__ == '__main__':
    kw = float(input("x^2 = "))

    # Dokladnosc uzyskanego wyniku - im wyższa, tym więcej iteracji
    eps = 0.000_000_1
    a = 1
    b = kw
    while abs(a - b) > eps:
        a = (a+b) / 2
        b = kw / a
        
    print(f'x = {a}')
