

# tentar implementar uma funcao para cada coisa
# posso usar uma biblioteca para retornar os cromos e as distancias


import copy
import random as rd


def scan(tabela):
    matriz = list(open(tabela, 'r'))

    matriz = [s.rstrip() for s in matriz]
    print(matriz)
    print(len(matriz))
    lista = [_str.split(' ') for _str in matriz]

    lista.remove(lista[0])
    print(lista)

    x = len(lista)
    scaneadas = {}
    while x > 0:
        if x != 0:
            x -= 1
        y = 0
        while y <= (len(lista[x])-1):
            local_scan = lista[x][y]
            if local_scan != '0':
                index = (y, x)
                scaneadas[local_scan] = index
            y += 1
    return curso(scaneadas)


def curso(scaner):
    keys = list(scaner.keys())
    cromos = []
    mtz = 'R'
    all_dists = []
    tp = 10
    grdr = 0
    vfs = []
    vfsTotal = []
    keys.remove(mtz)
    while grdr < tp:
        grdr += 1
        rkeys = rd.sample(keys, len(keys))
        cromossv = []
        dists = []
        for i in range(len(keys)-1):
            ca = rkeys[i]
            cp = rkeys[i+1]
            vs = scaner[mtz]
            v1 = scaner[ca]
            v2 = scaner[cp]

            dis_ini = abs(vs[1]-v1[1])+abs(v1[0]-vs[0])
            dist = abs(v1[1]-v2[1])+abs(v2[0]-v1[0])
            if len(dists) == 0:
                dists.append(dis_ini)
            dists.append(dist)
            if ca not in cromossv:
                cromossv.append(ca)
            if cp not in cromossv:
                cromossv.append(cp)
            if len(cromossv) == 4:
                dr = abs(vs[1]-v2[1]) + abs(v2[0]-vs[0])

        dTotal = sum(dists)+dr
        all_dists.append(dTotal)
        cromos.append(cromossv)
        vfs.append(1/dTotal)

    # criacao da roleta
    for i in range(tp):
        if i == 0:
            vfsTotal.append(vfs[i])
        else:
            vfsTotal.append(vfs[i]+vfsTotal[i-1])
    print('ola')


print(scan(r'C:\python\PSIS\flyfood\tabela.txt'))
