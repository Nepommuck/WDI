# Zadanie 8.
#
# Napisać program sprawdzający czy zadana liczba jest pierwsza.

import math


# przydatna funkcja na WDI
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(6, int(math.sqrt(n)+2), 6):
        if n % (i-1) == 0 or n % (i+1) == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input("n = "))

    if is_prime(n):
        print(f'{n} jest liczbą pierwszą')
    else:
        print(f'{n} nie jest liczbą pierwszą')
