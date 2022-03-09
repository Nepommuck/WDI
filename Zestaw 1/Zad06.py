# Zestaw 1.
# Zadanie 6. 
# 
# Proszę napisać program rozwiązujący równanie xx = 2020 metodą bisekcji.


def x_to_x(eps=0.000_000_1, eq=2020):
    x = 0
    while x**x < eq:
        x += 1
    if x**x == eq:
        return x
    l = x-1
    r = x
    while abs(l - r) > eps:
        x = (l+r) / 2
        if x**x > eq:
            r = x
        else:
            l = x
    return (l+r) / 2


if __name__ == '__main__':
    print(x_to_x())
