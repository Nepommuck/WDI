# Zestaw 6.
# Zadanie 2.
#
# Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.


import math
import random


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(6, int(math.sqrt(n)+2), 6):
        if n % (i-1) == 0 or n % (i+1) == 0:
            return False
    return True


def waga(n):
    if n <= 1:
        return 0
    w = 0
    if n % 2 == 0:
        w = 1
        while n % 2 == 0:
            n //= 2
    i = 3
    while n > 1 and not is_prime(n):
        if n % i == 0:
            w += 1
            while n % i == 0:
                n //= i
        i += 2
    if n > 1:
        w += 1
    return w


# Rozwiązanie 1 - bez użycia dodatkowej pamięci, bardzo wolne
def zad1(t, i=0, a=0, b=0, c=0):
    if i == len(t):
        if a == b == c:
            return True
        return False
    return zad1(t, i+1, a+waga(t[i]), b, c) or zad1(t, i+1, a, b+waga(t[i]), c) or zad1(t, i+1, a, b, c+waga(t[i]))


# Rozwiązanie 2 - Minimalna ilość dodatkowej pamięci, dużo szybsze
def zad2(t):
    wagi = [None for _ in range(len(t))]
    for i in range(len(t)):
        wagi[i] = waga(t[i])
    return rekur(wagi)


def rekur(t, i=0, a=0, b=0, c=0):
    if i == len(t):
        if a == b == c:
            return True
        return False
    return rekur(t, i+1, a+t[i], b, c) or rekur(t, i+1, a, b+t[i], c) or rekur(t, i+1, a, b, c+t[i])


if __name__ == '__main__':
    n = 12
    mx = 1000
    t = [random.randint(0, mx) for _ in range(n)]

    print(t)
    print(zad2(t))
    print(zad1(t))
