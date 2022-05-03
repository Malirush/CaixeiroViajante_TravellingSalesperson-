

# tentar implementar uma funcao para cada coisa
# posso usar uma biblioteca para retornar os cromos e as distancias





import random as rd


def scan(tabela):
    matriz = list(open(tabela, 'r'))
    matriz = [s.rstrip() for s in matriz]
    lista = [_str.split(' ') for _str in matriz]
    lista.remove(lista[0])
    x = len(lista)
    global scaneadas
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
    global keys
    keys = list(scaner.keys())
    global cromos
    try:
        qtdF = len(cromos)

    except NameError:
        cromos = []
    mtz = 'R'
    global all_dists
    all_dists = []
    global TopResultscromo
    try:
        qtdTop = len(TopResultscromo)

    except NameError:
        TopResultscromo = []

    global TopResultsdist
    try:
        qtdTopdist = len(TopResultsdist)

    except NameError:
        TopResultsdist = []

    tp = 8
    grdr = 0
    vfs = []
    vfsTotal = []
    keys.remove(mtz)
    cromo_dist = {}
    global Mutcount
    try:
        Mutcount += 0
    except:
        Mutcount = 0
    gras = 2
    gerascount = 0
    all_gras = []
    j = 0
    while gerascount < gras:
        gerascount += 1
        while grdr < tp:
            grdr += 1
            if Mutcount > 0:
                if j < qtdF:
                    rkeys = cromos[j]
                    Mutcount -= 1
                    j += 1

            else:
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

            if cromossv not in cromos:
                cromos.append(cromossv)
            dTotal = sum(dists)+dr
            all_dists.append(dTotal)
            vfs.append(1/dTotal)
            cromo_dist.update({str(cromossv): dTotal})
        if len(cromo_dist) != 8 or len(cromos) != 8:
            cromos.clear()
            try:
                cromos.append(filho1)
                cromos.append(filho2)
                grdr += 2
            except:
                pass
            cromo_dist.clear()
            all_dists.clear()
            grdr = 0
            gerascount = 0
            continue

        bestindex = (all_dists.index(min(all_dists)))
        TopResultsdist.append(min(all_dists))
        TopResultscromo.append(cromos[bestindex])
        if len(TopResultscromo) == 10:
            bestindex = TopResultsdist.index(min(TopResultsdist))
            distfinal = TopResultsdist[bestindex]
            final = TopResultscromo[bestindex]
            final = ','.join(final)
            return print(f'Melhor caminho:{final} Distancia: {distfinal}')

    return genetico(cromos, all_dists)


def genetico(cromos, dists):
    tp = len(cromos)
    vfs = [1/x for x in dists]
    vfsTotal = []
    pc = 0.95  # prbabilidade de cruzamento
    pm = 0.01  # prbabilidade de mutacao
    global tc
    tc = 4  # tamanho do cromossomo
    # criacao da roleta
    for i in range(tp):
        if i == 0:
            vfsTotal.append(vfs[i])
        else:
            vfsTotal.append(vfs[i]+vfsTotal[i-1])

    selecao = True
    while selecao:
        roleta1 = rd.random()
        i = 0
        while roleta1 > vfsTotal[i]:
            i += 1
            if i == (len(vfsTotal)):
                roleta1 = rd.random()
                i = 0
                continue

        pai1 = i

        roleta2 = rd.random()
        i = 0
        while roleta2 > vfsTotal[i]:
            i += 1
            if i == (len(vfsTotal)):
                roleta2 = rd.random()
                i = 0
                continue
        pai2 = i
        while pai2 == pai1:
            roleta2 = rd.random()
            i = 0
            while(roleta2 > vfsTotal[i]):
                i = i+1
                if i == (len(vfsTotal)):
                    roleta2 = rd.random()
                    i = 0
                    continue
            pai2 = i
        # cruzamento
        crz = 20
        while crz > 0:
            if pc > rd.random():
                c = rd.randint(0, 3)
                cromos[pai1][c], cromos[pai2][c] = cromos[pai2][c], cromos[pai1][c]
                if len(set(cromos[pai1])) < tc or len(set(cromos[pai2])) < tc:
                    cromos[pai1][c], cromos[pai2][c] = cromos[pai2][c], cromos[pai1][c]
                    crz -= 1
                    continue
                else:
                    global filho1
                    filho1 = cromos[pai1]
                    global filho2
                    filho2 = cromos[pai2]
                    selecao = False
                    break
        try:
            len(filho1)
            break
        except:
            continue
    if pm > rd.random():

        return mutacao(filho1, filho2)

    else:
        cromos.clear()
        cromos.append(filho1), cromos.append(filho2)
        global Mutcount
        Mutcount += 2
        curso(scaneadas)


def mutacao(filho1, filho2):
    mut = True
    while mut:
        idx = rd.randint(0, 3)
        if idx < 3:
            idx2 = idx+1
        elif idx > 0:
            idx2 = idx-1
        filho1[idx], filho2[idx] = filho2[idx], filho1[idx]
        filho1[idx2], filho2[idx2] = filho2[idx2], filho1[idx2]
        filho1test = set(filho1)
        filho2test = set(filho2)
        if len(filho1test) < tc or len(filho2test) < tc:
            filho1[idx], filho2[idx] = filho2[idx], filho1[idx]
            continue
        else:
            break
    cromos.clear()
    cromos.append(filho1), cromos.append(filho2)
    global Mutcount
    Mutcount += 2

    curso(scaneadas)


print(scan(r'C:\python\PSIS\flyfood\tabela.txt'))
