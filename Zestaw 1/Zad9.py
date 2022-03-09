# Zestaw 1.
# Zadanie 9.
#
# Napisać program wypisujący podzielniki liczby.


import math


def print_aliquot(n):
    for i in range(1, int(math.sqrt(n))+ 1):
        if n % i == 0:
            print(i)
            if n // i != i:
                print(n // i)


# To samo tylko wypisuje po kolei dzięki użyciu tablicy
def print_ordered(n):
    dziel = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(i)
            dziel.append(n // i)
    if len(dziel) == 0:
        return
    if n // dziel[-1] == dziel[-1]:
        dziel.pop()
    for item in dziel[::-1]:
        print(item)


if __name__ == '__main__':
    a = int(input("Podaj liczbę: "))
    print("Jej podzielniki to:")
    
    print_aliquot(a)
