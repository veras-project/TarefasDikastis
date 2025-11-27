def deslocamento_wolf(mapa, passos, linha_atual, coluna_atual, linha_cesar, coluna_cesar, visitados_linhas, visitados_colunas):
    n = len(mapa)
    if n > 0:
           m = len(mapa[0]) 
    else:
        m=0
    
    # Verifica se chegou ao César
    if linha_atual == linha_cesar and coluna_atual == coluna_cesar:
        return passos
    
    # Verifica se está fora dos limites ou em barreira (0)
    if linha_atual < 0 or linha_atual >= n or coluna_atual < 0 or coluna_atual >= m or mapa[linha_atual][coluna_atual] == 0:
        return 9999  # Valor alto indica caminho inválido
    
    # Verifica se já visitou esta posição
    for i in range(len(visitados_linhas)):
        if visitados_linhas[i] == linha_atual and visitados_colunas[i] == coluna_atual:
            return 9999
    
    # Adiciona a posição atual aos visitados
    visitados_linhas.append(linha_atual)
    visitados_colunas.append(coluna_atual)
    
    # Custo do movimento
    custo = 1
    if mapa[linha_atual][coluna_atual] == 3:
        custo = 3
    
    # Movimentos básicos
    movimentos_linhas = [linha_atual - 1, linha_atual + 1, linha_atual, linha_atual]
    movimentos_colunas = [coluna_atual, coluna_atual, coluna_atual - 1, coluna_atual + 1]
    
    # Adiciona saltos se for célula tipo 2
    if mapa[linha_atual][coluna_atual] == 2:
        movimentos_linhas.extend([linha_atual - 2, linha_atual + 2, linha_atual, linha_atual])
        movimentos_colunas.extend([coluna_atual, coluna_atual, coluna_atual - 2, coluna_atual + 2])
    
    menor_passos = 9999
    for i in range(len(movimentos_linhas)):
        nova_linha = movimentos_linhas[i]
        nova_coluna = movimentos_colunas[i]
        
        # Verifica limites
        if nova_linha < 0 or nova_linha >= n or nova_coluna < 0 or nova_coluna >= m:
            continue
        
        # Cria cópias dos visitados
        novos_visitados_linhas = []
        novos_visitados_colunas = []
        for j in range(len(visitados_linhas)):
            novos_visitados_linhas.append(visitados_linhas[j])
            novos_visitados_colunas.append(visitados_colunas[j])
        
        # Chamada recursiva
        passos_atual = deslocamento_wolf(mapa, passos + custo, nova_linha, nova_coluna, 
                                        linha_cesar, coluna_cesar, 
                                        novos_visitados_linhas, novos_visitados_colunas)
        if passos_atual < menor_passos:
            menor_passos = passos_atual
    
    return menor_passos

# Leitura da entrada
n = int(input())
m = int(input())
matriz = []
for _ in range(n):
    aux2=[]
    aux=input()
    for i in aux:
        if i.isnumeric():
            aux2.append(int(i))
    matriz.append(aux2)

# Saída inicial
print('=== SEKIRO: O RESGATE DE CESAR ===')
print('Wolf deve resgatar CESAR!')

# Chamada da função recursiva
visitados_linhas = []
visitados_colunas = []
passos = deslocamento_wolf(matriz, 0, 0, 0, n-1, m-1, visitados_linhas, visitados_colunas)

# Saída final
if passos == 9999:
    print('MORTE! Wolf não conseguiu resgatar Cesar... ele nunca saberá quem venceu Satoru Gojo ou Sukuna!')
else:
    print(f'SUCESSO! Wolf resgatou o Cesar em {passos} movimentos!')
    if passos <= 4:
        print('PERFEITO! Verdadeiro Shinobi! Cesar está ORGULHOSO!!')
    elif passos <= 8:
        print('BOM! Caminho eficiente! Mas você quase decepcionou Cesar')
    else:
        print('Wolf chegou, mas pode melhorar... Cesar está decepcionado, quase morreu de tédio!')