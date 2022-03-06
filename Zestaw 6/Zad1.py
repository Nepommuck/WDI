# Zestaw 6.
# Zadanie 1.
#
# Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkieco najmniej
# dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej cyfry.


import math
import random


# funkcja pomocnicza - określa czy liczba jest pierwsza
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(6, int(math.sqrt(n)+2), 6):
        if n % (i-1) == 0 or n % (i+1) == 0:
            return False
    return True


# funkcja pomocnicza - zwraca długość liczby (liczbę cyfr)
def dlug(n):
    d = 0
    while n > 0:
        n //= 10
        d += 1
    return d


# Rozwiązanie 1:
# nierekurencyjne, przy użyciu stringów, sporadycznie wypisuje parokrotnie tę samą liczbę
def iter(licz):
    nap = str(licz)
    n = len(nap)
    for i in range(1, 2**n - 1):
        k = i
        ind = 0
        new = ""
        while k > 0:
            if k % 2 == 1:
                new += nap[ind]
            ind += 1
            k //= 2
        if new[0] != '0':
            g = int(new)
            if g >= 10 and is_prime(g):
                print(g)


# Rozwiązanie 2:
# REKURENCYJNE, bez stringów, wypisuje od groma tych samych liczb
def rekur(licz, usun=-1):
    if usun != -1:
        k = 0
        i = 0
        while licz > 0:
            if i != usun:
                k = 10*k + (licz % 10)
            licz //= 10
            i += 1
        while k > 0:
            licz = 10*licz + (k % 10)
            k //= 10
        if licz >= 10 and is_prime(licz):
            print(licz)
    n = dlug(licz)
    if licz >= 100:
        for i in range(n):
            rekur(licz, i)


# Rozwiązanie 3:
# REKURENCYJNE, kalka z Rozwiązania 2.
# Zapisuje do tablicy znalezione liczby, dzięki czemu każda jest wypisana jedynie raz
def rekur_z_zap(licz):
    odp = []
    rekur2(licz, -1, odp)
    odp.sort()
    for item in odp:
        print(item)


def rekur2(licz, usun, tab):
    if usun != -1:
        k = 0
        i = 0
        while licz > 0:
            if i != usun:
                k = 10*k + (licz % 10)
            licz //= 10
            i += 1
        while k > 0:
            licz = 10*licz + (k % 10)
            k //= 10
        if licz >= 10 and is_prime(licz) and licz not in tab:
            tab.append(licz)    # Jedyna różnica
    n = dlug(licz)
    if licz >= 100:
        for i in range(n):
            rekur2(licz, i, tab)


if __name__ == '__main__':
    for i in range(1):
        n = random.randint(0, 1_000_000)
        print(f'Wylosowano: {n}')
        print('\nRozwiązanie 1:')
        iter(n)
        print('\nRozwiązanie 2:')
        rekur(n)
        print('\nRozwiązanie 3:')
        rekur_z_zap(n)
