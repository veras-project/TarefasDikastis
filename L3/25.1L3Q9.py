N = int(input())
matriz = []
for _ in range(N):
    linha = input().strip().split()
    matriz.append(linha)

pos_linha = 0
pos_coluna = 0
i = 0
achou = False
while i < N and not achou:
    j = 0
    while j < N and not achou:
        if matriz[i][j] == 'H':
            pos_linha = i
            pos_coluna = j
            achou = True
        j += 1
    i += 1

dias = 0
restaurados = 0
destruidos = 0
dias_sem_restaurar = 0

i = 0
while i < N:
    j = 0
    while j < N:
        if matriz[i][j] == 'X':
            destruidos += 1
        j += 1
    i += 1

jogo_ativo = True
while dias < 7 and jogo_ativo:
    comando = input().strip()
    if comando == 'FIM':
        tem_E = False
        i = 0
        while i < N:
            j = 0
            while j < N:
                if matriz[i][j] == 'E':
                    tem_E = True
                j += 1
            i += 1
        if tem_E:
            print("Ainda existem quarteirões corrompidos! O Miranha não pode ir embora agora!")
        jogo_ativo = False
        continue

    dias += 1
    nova_linha = pos_linha
    nova_coluna = pos_coluna

    if comando == 'Cima':
        nova_linha = pos_linha - 1
    elif comando == 'Baixo':
        nova_linha = pos_linha + 1
    elif comando == 'Esquerda':
        nova_coluna = pos_coluna - 1
    elif comando == 'Direita':
        nova_coluna = pos_coluna + 1

    movimento_valido = True
    if nova_linha < 0 or nova_linha >= N or nova_coluna < 0 or nova_coluna >= N:
        movimento_valido = False
    else:
        if matriz[nova_linha][nova_coluna] == 'X':
            movimento_valido = False

    mensagem_especial = ""
    if not movimento_valido:
        mensagem_especial = "Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!"
        dias_sem_restaurar += 1
    else:
        matriz[pos_linha][pos_coluna] = '.'
        if matriz[nova_linha][nova_coluna] == 'E':
            matriz[nova_linha][nova_coluna] = 'H'
            restaurados += 1
            dias_sem_restaurar = 0
            mensagem_especial = "O Miranha restaurou um quarteirão!"
        else:
            matriz[nova_linha][nova_coluna] = 'H'
            mensagem_especial = "O Electro está ganhando espaço!"
            dias_sem_restaurar += 1

        pos_linha = nova_linha
        pos_coluna = nova_coluna

    if dias_sem_restaurar == 3:
        destruiu_um = False
        i = 0
        while i < N and not destruiu_um:
            j = 0
            while j < N and not destruiu_um:
                if matriz[i][j] == 'E':
                    matriz[i][j] = 'X'
                    destruidos += 1
                    destruiu_um = True
                j += 1
            i += 1
        dias_sem_restaurar = 0

    print("Dia {}".format(dias))
    i = 0
    while i < N:
        linha_imprimir = ""
        j = 0
        while j < N:
            linha_imprimir += matriz[i][j]
            if j != N - 1:
                linha_imprimir += " "
            j += 1
        print(linha_imprimir)
        i += 1

    print("Posição atual do Homem-Aranha: ({}, {})".format(pos_linha, pos_coluna))
    print("Quarteirões restaurados: {} | Quarteirões destruídos: {}".format(restaurados, destruidos))
    print(mensagem_especial)
    print()

    tem_E = False
    i = 0
    while i < N and not tem_E:
        j = 0
        while j < N and not tem_E:
            if matriz[i][j] == 'E':
                tem_E = True
            j += 1
        i += 1
    if not tem_E:
        print("Missão cumprida! Nova York está segura e o Miranha faz tudo novamente!")
        jogo_ativo = False

if dias == 7 and jogo_ativo:
    tem_E = False
    i = 0
    while i < N and not tem_E:
        j = 0
        while j < N and not tem_E:
            if matriz[i][j] == 'E':
                tem_E = True
            j += 1
        i += 1
    if tem_E:
        print("O Miranha não conseguiu restaurar a cidade a tempo, o Electro venceu!")
