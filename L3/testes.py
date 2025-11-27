#Começando a parte basic

# vv,vh,sv são (vitoriavilão,vitoriaheroi,semvitoria)

qntdonda=int(input())
resultodisput=[]
difbattle=[]
# CORREÇÃO: Adicionada uma lista para guardar as ondas originais para o print final
ondas_originais = [] 
posbiggest=0
# CORREÇÃO: A maior diferença precisa começar com um valor que possa ser superado.
# -1 garante que a primeira diferença (que é sempre >= 0) seja registrada.
biigestdif=-1 
tvondavenceddora=False


#Preenchendo As 3 Listas Com informações
for _ in range (qntdonda):
    heroes=[]
    villain=[]
    
    bruteinput=input()
    ondas_originais.append(bruteinput) # Guarda a string da onda original
    
    listaprimaria=bruteinput.split(', ')
    # A sua lógica para pegar a sublista da disputa está perfeita.
    characterlist=listaprimaria[1:len(listaprimaria)-1]

    for j in characterlist:
        if 'H-' in j:
            heroes.append(j)
        else:
            villain.append(j)
    
    dif= len(heroes) - len(villain)
    # abs() já calcula o valor absoluto, não precisa converter para int.
    difbattle.append(abs(dif))
    
    if dif < 0: 
        resultodisput.append('vv')
    elif dif > 0:
        resultodisput.append('vh')
    else:
        resultodisput.append('sv')

#Analisando a Lista (Sua lógica aqui já estava ótima)
for k in range(len(difbattle)):
    # A regra de desempate (menor índice) é garantida pelo ">"
    if difbattle[k] > biigestdif:
        biigestdif = difbattle[k]
        posbiggest = k

if biigestdif == 0:
    print('🌀Nenhuma onda foi selecionada como a menos acirrada e a mais favorável para nenhum do dois lados!')
elif resultodisput[posbiggest]=='vh':
    print(f'🌀Onda {posbiggest + 1} foi a menos acirrada e a mais favorável para os heróis!')
    tvondavenceddora=True
elif resultodisput[posbiggest]=='vv':
    print(f'🌀Onda {posbiggest + 1} foi a menos acirrada e a mais favorável para os vilões!')
    tvondavenceddora=True

# --- INÍCIO DA PARTE FINALIZADA ---

# Imprime os participantes da onda com maior diferença, se houver
if tvondavenceddora:
    # Acessamos a lista de ondas originais com a posição que encontramos
    print(f'Participantes analisados: {ondas_originais[posbiggest]}')

# Imprime o placar geral
print('Agora vamos ao resultado geral das ondas...')

# Contamos as vitórias usando sua lista resultodisput
vitorias_herois = resultodisput.count('vh')
vitorias_viloes = resultodisput.count('vv')

print(f'Heróis: {vitorias_herois} | Vilões: {vitorias_viloes}')

# Imprime o veredito final
if vitorias_herois > vitorias_viloes:
    print('Ufa, os heróis dominaram! Central City está seguro outra vez')
elif vitorias_viloes > vitorias_herois:
    print('Ah, não. Os vilões vão dominar Central City e mandar todos os heróis embora!')
else:
    print('Ninguém é mais forte que ninguém. Heróis e vilões vão ter que entrar em consenso para viverem no mesmo espaço')