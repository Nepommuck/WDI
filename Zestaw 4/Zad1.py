# Zestaw 4.
# Zadanie 1.
#
# Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami naturalnymi po spirali.


def show(tab):
    for line in tab:
        print(line)


def spirala(tab):
    n = len(tab)
    licz = 0
    x = -1
    y = 0
    dl = n
    k = 0
    zm = True

    while dl > 0:
        for _ in range(dl):
            if k == 0:
                x += 1
            elif k == 1:
                y += 1
            elif k == 2:
                x -= 1
            else:
                y -= 1
            tab[y][x] = licz
            licz += 1

        if zm:
            dl -= 1
            zm = False
        else:
            zm = True
        k = (k+1) % 4


if __name__ == '__main__':
    n = 10
    t = [[0 for _ in range(n)] for _ in range(n)]
    spirala(t)
    show(t)
