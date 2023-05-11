# EP2(1.0):

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


#Esse primeiro codigo não estava rodando 100%, tentei reescrever o mesmo abaixo, mas no fim nenhum rodou até o fim :(

# EP2(2.0):

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

from random import randint

frota_inimiga = {
    "porta-aviões": [[[randint(0, 9), randint(0, 9)] for _ in range(4)]] ,
    "navio-tanque": [[[randint(0, 9), randint(0, 9)] for _ in range(3)] , [[randint(0, 9), randint(0, 9)] for _ in range(3)]],
    "contratorpedeiro": [[[randint(0, 9), randint(0, 9)] for _ in range(2)] , [[randint(0, 9), randint(0, 9)] for _ in range(2)], [[randint(0, 9), randint(0, 9)] for _ in range(2)]],
    "submarino": [[[randint(0, 9), randint(0, 9)]] , [[randint(0, 9), randint(0, 9)]] , [[randint(0, 9), randint(0, 9)]] , [[randint(0, 9), randint(0, 9)]] ]
}

def imprime_tabuleiro(tabuleiro):
    print("   A B C D E F G H I J")
    for i, linha in enumerate(tabuleiro):
        print(f"{i}  {' '.join(str(c) for c in linha)}")

def verifica_jogada(jogada, frota):
    for navio, posicoes in frota.items():
        for i, parte in enumerate(posicoes):
            if jogada in parte:
                frota[navio][i].remove(jogada)
                if not frota[navio][i]:
                    frota[navio].remove(frota[navio][i])
                    if not frota[navio]:
                        print(f"Você afundou o {navio}!")
                return True
    return False


tabuleiro_jogador = [[0] * 10 for _ in range(10)]
jogadas = []
while True:

    imprime_tabuleiro(tabuleiro_jogador)

    while True:
        jogada = input("Informe a sua jogada (ex: A4): ")
        if len(jogada) == 2 and jogada[0] in "ABCDEFGHIJ" and jogada[1] in "0123456789":
            linha = int(jogada[1])
            coluna = "ABCDEFGHIJ".index(jogada[0])
            if [linha, coluna] not in jogadas:
                jogadas.append([linha, coluna])
                break
            else:
                print("Você já jogou nessa posição!")
        else:
            print("Jogada inválida! Informe a jogada no formato A4.")

    if verifica_jogada([linha, coluna], frota_inimiga):
        tabuleiro_jogador[linha][coluna] = "X"
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
def posiciona_frota(tabuleiro, frota):
    while True:
        try:
            linha = int(input("Qual linha deseja jogar? "))
            coluna = int(input("Qual coluna deseja jogar? "))
            if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                raise ValueError
            break
        except ValueError:
            print("Jogada inválida! Tente novamente.")
    
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
        print("Você acertou uma embarcação inimiga!")
        if afundados(frota, tabuleiro) == len(frota):
            print("Você venceu o jogo!")
    else:
        tabuleiro[linha][coluna] = '-'
        print("Você não acertou nenhuma embarcação inimiga.")

from random import randint

frota_inimiga = {
    "porta-aviões": [[[randint(0, 9), randint(0, 9)] for _ in range(4)]] ,
    "navio-tanque": [[[randint(0, 9), randint(0, 9)] for _ in range(3)] , [[randint(0, 9), randint(0, 9)] for _ in range(3)]],
    "contratorpedeiro": [[[randint(0, 9), randint(0, 9)] for _ in range(2)] , [[randint(0, 9), randint(0, 9)] for _ in range(2)], [[randint(0, 9), randint(0, 9)] for _ in range(2)]],
    "submarino": [[[randint(0, 9), randint(0, 9)]] , [[randint(0, 9), randint(0, 9)]] , [[randint(0, 9), randint(0, 9)]] , [[randint(0, 9), randint(0, 9)]] ]
}

def imprime_tabuleiro(tabuleiro):
    print("   A B C D E F G H I J")
    for i, linha in enumerate(tabuleiro):
        print(f"{i}  {' '.join(str(c) for c in linha)}")

def verifica_jogada(jogada, frota):
    for navio, posicoes in frota.items():
        for i, parte in enumerate(posicoes):
            if jogada in parte:
                frota[navio][i].remove(jogada)
                if not frota[navio][i]:
                    frota[navio].remove(frota[navio][i])
                    if not frota[navio]:
                        print(f"Você afundou o {navio}!")
                return True
    return False

tabuleiro_jogador = [[0] * 10 for _ in range(10)]
jogadas = []
while True:

    imprime_tabuleiro(tabuleiro_jogador)
    
    while True:
        jogada = input("Informe a sua jogada (ex: A4): ")
        if len(jogada) == 2 and jogada[0] in "ABCDEFGHIJ" and jogada[1] in "0123456789":
            linha = int(jogada[1])
            coluna = "ABCDEFGHIJ".index(jogada[0])
            if [linha, coluna] not in jogadas:
                jogadas.append([linha, coluna])
                break
            else:
                print("Você já jogou nessa posição!")
        else:
            print("Jogada inválida! Informe a jogada no formato A4.")

    if verifica_jogada([linha, coluna], frota_inimiga):
        tabuleiro_jogador[linha][coluna] = "X"

