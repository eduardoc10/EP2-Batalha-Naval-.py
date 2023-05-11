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
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    # Verifica
    for posicao in posicoes:
        linha, coluna = posicao
        if linha not in range(10) or coluna not in range(10):
            return False
        for navio in frota.values():
            for parte in navio:
                if posicao in parte:
                    return False
    return True
from random import randint

Tabuleiro_tamanho=10

def posicao_valida2(tabuleiro, posicoes):
    for pos in posicoes:
        linha, coluna = pos
        if (linha < 0 or linha > 9) or (coluna < 0 or coluna > 9) or (tabuleiro[linha][coluna] != "-"):
            return False
    return True

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 1:
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes

def preenche_frota(tabuleiro, frota, nome, tamanho):
    while True:
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if nome != "submarino":
            orientacao = int(input("[1] Vertical [2] Horizontal >"))
        else:
            orientacao = 2
        posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
        if posicao_valida(tabuleiro, posicoes):
            for pos in posicoes:
                linha, coluna = pos
                tabuleiro[linha][coluna] = nome[0].upper()
            frota[nome].append(posicoes)
            break
        else:
            print("Esta posição não está válida!")

tabuleiro = []
for i in range(10):
    linha = ["-" for i in range(10)]
    tabuleiro.append(linha)

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

embarcacoes = [("porta-aviões", 4), ("navio-tanque", 3), ("navio-tanque", 3), ("contratorpedeiro", 2), ("contratorpedeiro", 2), ("contratorpedeiro", 2), ("submarino", 1), ("submarino", 1), ("submarino", 1), ("submarino", 1)]

for embarcacao in embarcacoes:
    nome, tamanho = embarcacao
    preenche_frota(tabuleiro, frota, nome, tamanho)

print(frota)
