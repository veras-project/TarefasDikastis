#Fun?No.Ções
def deslocamento_wolf(mapa, passos, linha_atual, coluna_atual, linha_cesar, coluna_cesar, visitados_linhas, visitados_colunas):
    n = len(mapa)
    if n > 0:
        m=len(mapa[0])
    else:
        m=0
    
    if linha_atual == linha_cesar and coluna_atual == coluna_cesar:
        return passos
    
    if linha_atual < 0 or linha_atual >= n or coluna_atual < 0 or coluna_atual >= m or mapa[linha_atual][coluna_atual] == 0:
        return 9999
    
    javisitou = False
    i = 0
    while i < len(visitados_linhas) and not javisitou:
        if visitados_linhas[i] == linha_atual:
            for _ in range(len(visitados_colunas)):
                if visitados_colunas[i] == coluna_atual:
                    javisitou = True
        i += 1
    if javisitou:
        return 9999
    
    visitados_linhas.append(linha_atual)
    visitados_colunas.append(coluna_atual)
    
    # How Much Man
    custo = 1
    if mapa[linha_atual][coluna_atual] == 3:
        custo = 3
    
    movimentos_linhas = [linha_atual - 1, linha_atual + 1, linha_atual, linha_atual]
    movimentos_colunas = [coluna_atual, coluna_atual, coluna_atual - 1, coluna_atual + 1]
    
    if mapa[linha_atual][coluna_atual] == 2:

        movimentos_linhas.append(linha_atual - 2) 
        movimentos_colunas.append(coluna_atual)   

        movimentos_linhas.append(linha_atual + 2)  
        movimentos_colunas.append(coluna_atual)   


        movimentos_linhas.append(linha_atual)    
        movimentos_colunas.append(coluna_atual - 2) 
        movimentos_linhas.append(linha_atual)      
        movimentos_colunas.append(coluna_atual + 2)  
    
    valemaisapena = 9999
    for i in range(4):
        nova_linha = movimentos_linhas[i]
        nova_coluna = movimentos_colunas[i]
        
        if not (nova_linha < 0 or nova_linha >= n or nova_coluna < 0 or nova_coluna >= m):
            novos_visitados_linhas = []
            novos_visitados_colunas = []
            for j in range(len(visitados_linhas)):
                novos_visitados_linhas.append(visitados_linhas[j])
                novos_visitados_colunas.append(visitados_colunas[j])
            
            passos_atual = deslocamento_wolf(mapa, passos + custo, nova_linha, nova_coluna,linha_cesar, coluna_cesar,novos_visitados_linhas, novos_visitados_colunas)
            if passos_atual < valemaisapena:
                valemaisapena = passos_atual
    
    return valemaisapena

# Leitura da entrada
n = int(input())
m = int(input())
matriz = []
for _ in range(n):
    aux2 = []
    aux = input()
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

# Prints
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