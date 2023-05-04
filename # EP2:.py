# EP2:


def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'horizontal':
            posicoes.append([linha, coluna+i])
        else:
            posicoes.append([linha+i, coluna])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    return frota
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for _ in range(10)]

    for navio, posicoes in frota.items():
        for coordenadas in posicoes:
            for linha, coluna in coordenadas:
                tabuleiro[linha][coluna] = 1

    return tabuleiro
def afundados(frota, tabuleiro):
    afundados = 0



     for navio, posicoes in frota.items():
        for posicao in posicoes:
            afundado = True
            for coordenada in posicao:
                x, y = coordenada
                if tabuleiro[x][y] != "X":
                    afundado = False
                    break
            if afundado:
                afundados += 1
    return afundados
