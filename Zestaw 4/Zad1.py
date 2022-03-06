def spirala(tab):
    n = len(tab)
    for i in range(n):
        tab[0][i] = i
    licz = n
    x = n-1
    y = 0
    dl = n-1
    k = 1
    zm = False
    while dl > 0:
        for _ in range(dl):
            if k == 0:
                x += 1
            elif k == 1:
                y += 1
            elif k == 2:
                x -= 1
            else:
                y -= 1
            tab[y][x] = licz
            licz += 1

        if zm:
            dl -= 1
            zm = False
        else:
            zm = True
        k = (k+1) % 4
