# Zestaw 1.
# Zadanie 10. 
# 
# Napisać program wyszukujący liczby doskonałe mniejsze od miliona.


import math


# Rozwiązanie intuicyjne - za wolne dla miliona
def is_perfect(n):
    sum = 1
    i = 2
    s = math.sqrt(n)
    while i < s:
        if sum > n:
            return False
        if n % i == 0:
            sum += i
            sum += n // i
        i += 1

    if i == s:
        sum += s

    if sum == n:
        return True
    return False


# Liczby doskonałe mają postać: q*(q+1)/2
# gdzie q to liczba pierwsza postaci: q = 2^i-1
# a i jest liczbą naturalną
def print_perfects(mx=1_000_000):
    rez = 1
    i = 1
    while rez < mx:
        q = 2 ** i - 1
        rez = q * (q + 1) // 2
        if is_prime(q):
            print(rez)
        i += 1


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(6, int(math.sqrt(n) + 2), 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
    return True


if __name__ == '__main__':
    #   for i in range(1_000_000):
    #       if is_perfect(i):
    #           print(i)

    print_perfects(1_000_000)

    # Polecam potestować jak bardzo oba rozwiązania różnią się szybkością
    # print_perfects(1_000_000_000_000_000_000)
