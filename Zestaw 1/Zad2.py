# Zadanie 2.
#
# Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu
# analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.


rok = 2022

if __name__ == '__main__':

    # para liczb: (1, rok-1) zawsze bedzie rozwiazaniem
    odp = [1, rok-1]
    suma = rok

    a = 1
    b = 2
    while a+b < suma:
        while a+b < suma:
            i = a
            k = b
            while i+k < rok:
                i, k = k, i+k
                if i + k == rok:
                    odp = [a, b]
                    suma = a+b

            b += 1

        a += 1
        b = a + 1

    print(odp[0], odp[1])
