# Zadanie 1.
#
# Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.


# (liczba, podstawa systemu)
def wyp_podst(n, pod):
    rez = ""
    lit="ABCDEF"
    while n > 0:
        a = n % pod
        if a <= 9:
            a = str(a)
        else:
            a = lit[a-10]
        rez += a
        n //= pod
    for i in rez[::-1]:
        print(i, end='')
    if len(rez) == 0:
        print(0, end='')
    print('')
