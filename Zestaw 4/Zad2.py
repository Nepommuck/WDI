# Zestaw 4.
# Zadanie 2.
#
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
# z nieparzystych cyfr.


import random


def show(tab):
    for line in tab:
        print(line)


def zad(tab):
    n = len(tab)
    for y in range(n):
        wyst = False
        for x in range(n):
            if niepar(tab[y][x]):
                wyst = True
                break
        if not wyst:
            print(x, y)
            return False
    return True


def niepar(n):
    if n == 0:
        return False
    while n > 0:
        if n % 2 == 0:
            return False
        n //= 10
    return True


if __name__ == '__main__':
    n = 10
    mx = 10_000
    t = [[random.randint(0, mx) for _ in range(n)] for _ in range(n)]
    show(t)
    print(zad(t))
