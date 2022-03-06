# Zadanie 1.
# 
# Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.


if __name__ == '__main__':

    a = 0
    b = 1

    while a < 1_000_000:
        print(a)
        a, b = b, a+b
