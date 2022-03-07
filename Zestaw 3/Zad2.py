# Zestaw 3.
# Zadanie 2.
#
# Napisać program wczytujący dwie liczby naturalne i odpowiadający na pytanie czy
# są one zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.


def dlug(n):
    d = 0
    while n > 0:
        d += 1
        n //= 10
    return d


def spr(a, b):
    if dlug(a) != dlug(b):
        return False

    cyf = [0 for _ in range(10)]
    while a > 0:
        cyf[a % 10] += 1
        a //= 10
    while b > 0:
        cyf[b % 10] -= 1
        if cyf[b % 10] < 0:
            return False
        b //= 10

    for i in range(10):
        if cyf[i] != 0:
            return False
    return True


if __name__ == '__main__':
    x = int(input("Podaj 1. liczbę: "))
    y = int(input("Podaj 2. liczbę: "))

    if spr(x, y):
        print("Liczby są zbudowane z tych samych cyfr")
    else:
        print("Liczby są zbudowane z różnych cyfr")
