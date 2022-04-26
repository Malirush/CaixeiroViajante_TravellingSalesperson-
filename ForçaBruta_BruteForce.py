

import random as rd
import math


def scan(tabela):
    matriz = list(open(tabela, 'r'))
    matriz = [s.rstrip() for s in matriz]
    lista = [_str.split(' ') for _str in matriz]
    lista.remove(lista[0])
    x = len(lista)
    scaneadas = {}
    while x >= 0:
        x -= 1
        y = 0
        while y <= 4:
            local_scan = lista[x][y]
            if len(scaneadas) == 5:
                break
            if local_scan != '0':
                index = (y, x)
                scaneadas[local_scan] = index
            y += 1
    return custo(scaneadas)


def custo(scan):
    saida = 'R'
    cidades = ['B', 'C', 'A', 'D']
    distancias = {}
    percurso = []
    individuos = 100
    pm = 0.1
    all_dist = []
    perc_dist = {}
    best_results = []
    j = 0
    best_ways = {}
    format = '"]['
    geracoes = 20

    while j < individuos:
        embaralhamento = rd.sample(cidades, len(cidades))
        for i in range(4):
            try:
                cidade_atual = embaralhamento[i]
                percurso.append(cidade_atual)
                prox_cidade = embaralhamento[i+1]
                valor_saida = scan[saida]
                valor_1 = scan[cidade_atual]
                valor_2 = scan[prox_cidade]
                dist_inicial = abs(
                    valor_saida[1]-valor_1[1])+abs(valor_1[0]-valor_saida[0])

                dist = abs(valor_1[1]-valor_2[1])+abs(valor_2[0]-valor_1[0])

                if len(distancias) < 1:
                    distancias.update(
                        {f'{saida},{cidade_atual}': dist_inicial})

                distancias.update({f'{cidade_atual},{prox_cidade}': dist})
            except:
                pass
        if len(distancias) == 4:
            dist_retorno = abs(valor_saida[1]-valor_2[1]) + \
                abs(valor_2[0]-valor_saida[0])
        dis_total = sum(distancias.values())+dist_retorno

        # print(f'{dis_total}')
        all_dist.append(dis_total)
        perc_dist.update({f'{percurso}': dis_total})
        percurso.clear()
        distancias.clear()
        j += 1
        if j == 100:
            if rd.random() < pm:
                j = 0
                best_results.append(min(all_dist))
                continue

    best_results.append(min(all_dist))
    for chave, valor in perc_dist.items():
        if valor == min(best_results):
            best_ways.update({chave: valor})

    for chave, valor in best_ways.items():
        print(f'{chave} custo: {valor}')

    return


scan(r'C:\python\PSIS\flyfood\tabela.txt')
