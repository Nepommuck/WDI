# Zadanie 4.
#
# Proszę napisać program obliczający pierwiastek całkowitoliczbowy
# z liczby naturalnej korzystając z zależności 1 + 3 + 5 + ... = n^2.

# n to liczba składników sumy /Pawel


if __name__ == '__main__':
    kw = int(input("Podaj sumę do sprawdzenia: "))    
    sum = 0
    n = 0
    el = 1
    
    while sum <= kw:
        n += 1
        sum += el
        el += 2
        
    n -= 1
    print(n)
