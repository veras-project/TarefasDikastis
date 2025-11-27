alfabeto_codificado = ['k', 'q', 'f', 'm', 'x', 'e', 't', 'z', 'r', 'h', 'v', 'n', 'd', 'l', 'j', 'a', 's', 'u', 'y', 'b', 'g', 'w', 'p', 'o', 'i', 'c']
alfabeto_normal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

teen_team = ['rex splode', 'duplikate', 'atom eve', 'robot']

N = int(input())
equipes = []
i = 0
while i < N:
    equipes.append([])
    i += 1

fim_recebido = False
while not fim_recebido:
    acao = input().strip()
    if acao == 'FIM':
        fim_recebido = True

    elif acao == 'adicionar':
        print("Quem será o próximo integrante do time?")

        linha = input()
        pos_hifen = 0
        encontrou = False
        while pos_hifen < len(linha) and not encontrou:
            if linha[pos_hifen] == '-':
                encontrou = True
            else:
                pos_hifen += 1

        if encontrou:
            nome_cod = ''
            idx = 0
            while idx < pos_hifen:
                nome_cod += linha[idx]
                idx += 1
            nome_cod = nome_cod.strip()

            poder_str = ''
            idx = pos_hifen + 1
            while idx < len(linha):
                poder_str += linha[idx]
                idx += 1
            poder_str = poder_str.strip()

            poder = 0
            j = 0
            while j < len(poder_str):
                poder = poder * 10 + (ord(poder_str[j]) - ord('0'))
                j += 1
        else:
            nome_cod = linha.strip()
            poder = 0

        time_idx = int(input())

        nome_dec = ''
        pos = 0
        while pos < len(nome_cod):
            c = nome_cod[pos]
            if c == ' ':
                nome_dec += ' '
            else:
                k = 0
                achou = False
                while k < len(alfabeto_codificado) and not achou:
                    if alfabeto_codificado[k] == c:
                        nome_dec += alfabeto_normal[k]
                        achou = True
                    k += 1
                if not achou:
                    nome_dec += c
            pos += 1

        equipes[time_idx].append([nome_dec, poder])

        idx_tt = 0
        while idx_tt < len(teen_team):
            if teen_team[idx_tt] == nome_dec:
                if idx_tt == 0:
                    print("Eu vou te detonar!")
                elif idx_tt == 1:
                    print("Quantas de mim você acha que consegue lidar?")
                elif idx_tt == 2:
                    print("Eu reescrevo a matéria... incluindo a SUA.")
                elif idx_tt == 3:
                    print("Minha lógica diz que você vai perder.")
            idx_tt += 1

    elif acao == 'metamorfo':
        print("Atenção!!! Metamorfo encontrado, quem deverá ser removido do time?")
        nome_remover = input().strip()
        print("Quem você gostaria de colocar no lugar?")
        linha = input()

        time_idx = int(input())

        idx_heroi = 0
        achou_heroi = False
        while idx_heroi < len(equipes[time_idx]) and not achou_heroi:
            nome_atual = equipes[time_idx][idx_heroi][0]
            if nome_atual == nome_remover:
                equipes[time_idx].pop(idx_heroi)
                achou_heroi = True
            else:
                idx_heroi += 1

        pos_hifen = 0
        encontrou = False
        while pos_hifen < len(linha) and not encontrou:
            if linha[pos_hifen] == '-':
                encontrou = True
            else:
                pos_hifen += 1

        if encontrou:
            nome_cod = ''
            idx = 0
            while idx < pos_hifen:
                nome_cod += linha[idx]
                idx += 1
            nome_cod = nome_cod.strip()

            poder_str = ''
            idx = pos_hifen + 1
            while idx < len(linha):
                poder_str += linha[idx]
                idx += 1
            poder_str = poder_str.strip()

            poder = 0
            j = 0
            while j < len(poder_str):
                poder = poder * 10 + (ord(poder_str[j]) - ord('0'))
                j += 1
        else:
            nome_cod = linha.strip()
            poder = 0

        nome_dec = ''
        pos = 0
        while pos < len(nome_cod):
            c = nome_cod[pos]
            if c == ' ':
                nome_dec += ' '
            else:
                k = 0
                achou = False
                while k < len(alfabeto_codificado) and not achou:
                    if alfabeto_codificado[k] == c:
                        nome_dec += alfabeto_normal[k]
                        achou = True
                    k += 1
                if not achou:
                    nome_dec += c
            pos += 1

        equipes[time_idx].append([nome_dec, poder])

        idx_tt = 0
        while idx_tt < len(teen_team):
            if teen_team[idx_tt] == nome_dec:
                if idx_tt == 0:
                    print("Eu vou te detonar!")
                elif idx_tt == 1:
                    print("Quantas de mim você acha que consegue lidar?")
                elif idx_tt == 2:
                    print("Eu reescrevo a matéria... incluindo a SUA.")
                elif idx_tt == 3:
                    print("Minha lógica diz que você vai perder.")
            idx_tt += 1

idx_time = 0
achou_teen_time = False
while idx_time < len(equipes):
    count_teen = 0
    pos_tt = 0
    while pos_tt < len(teen_team):
        pos_heroi = 0
        achou_heroi = False
        while pos_heroi < len(equipes[idx_time]):
            if equipes[idx_time][pos_heroi][0] == teen_team[pos_tt]:
                achou_heroi = True
            pos_heroi += 1
        if achou_heroi:
            count_teen += 1
        pos_tt += 1
    if count_teen == 4:
        achou_teen_time = True
        pos_heroi = 0
        while pos_heroi < len(equipes[idx_time]):
            poder_antigo = equipes[idx_time][pos_heroi][1]
            poder_novo = int(poder_antigo * 1.1)
            equipes[idx_time][pos_heroi][1] = poder_novo
            pos_heroi += 1
    idx_time += 1

if achou_teen_time:
    print("O teen team esta completo, Cecil esta muito contente!")

idx_time = 0
melhor_poder = -1
melhor_time = -1
while idx_time < len(equipes):
    soma_poder = 0
    pos_heroi = 0
    while pos_heroi < len(equipes[idx_time]):
        soma_poder += equipes[idx_time][pos_heroi][1]
        pos_heroi += 1
    if soma_poder > melhor_poder:
        melhor_poder = soma_poder
        melhor_time = idx_time
    idx_time += 1

time_sel = equipes[melhor_time]

i = 0
while i < len(time_sel) - 1:
    j = 0
    while j < len(time_sel) - 1 - i:
        if time_sel[j][1] < time_sel[j+1][1]:
            aux = time_sel[j]
            time_sel[j] = time_sel[j+1]
            time_sel[j+1] = aux
        j += 1
    i += 1

top = 3
if len(time_sel) < 3:
    top = len(time_sel)

nomes_top = ''
i = 0
while i < top:
    nomes_top += time_sel[i][0]
    if i != top - 1:
        nomes_top += ', '
    i += 1

print(f"Aqui está o poderoso time da terra: {nomes_top}")

viltrumitas = [['general kregg',110],['conquista',100], ['anissa', 90]]

rodada = 1
vitorias_herois = 0
vitorias_viltrumita = 0
i = 0
while i < top:
    heroi_nome = time_sel[i][0]
    heroi_poder = time_sel[i][1]
    vil_nome = viltrumitas[i][0]
    vil_poder = viltrumitas[i][1]

    print(f"{rodada} Duelo: {heroi_nome} X {vil_nome}")
    if heroi_poder > vil_poder:
        vitorias_herois += 1
    else:
        vitorias_viltrumita += 1

    rodada += 1
    i += 1

if vitorias_herois > vitorias_viltrumita:
    print("A terra venceu!")
else:
    print("Infelizmente o imperio viltrumita conquistou a terra!")