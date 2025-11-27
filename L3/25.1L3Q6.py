#Começando a parte basic

# vv,vh,sv são (vitoriavilão,vitoriaheroi,semvitoria)

qntdonda=int(input())
resultodisput=[]
difbattle=[]
heroes=[]
villain=[]
posbiggest=0
biigestdif=-1
tvondavenceddora=False
secondanaliselist=[]
Hexcl=[]
Vexcl=[]
geralchegou = []


#Preenchendo As 3 Listas Com informações

for _ in range (qntdonda):
    heroes.clear()
    villain.clear()
    bruteinput=input()

    geralchegou.append(bruteinput)

    listaprimaria=bruteinput.split(', ')
    characterlist=listaprimaria[1:len(listaprimaria)-1]





    for j in characterlist:

        if 'H-' in j:
            j=j[2:]
            heroes.append(j)
        else:
            j=j[2:]
            villain.append(j)
    
    
    dif= len(heroes)- len(villain)
    difbattle.append(abs(int(dif)))
    

    if dif < 0: 

        resultodisput.append('vv')
    
    elif dif > 0:

        resultodisput.append('vh')

    else:

        resultodisput.append('sv')

#Analisando a Lista

for k in range(0,len(difbattle)):

    if difbattle[k]>biigestdif:
        biigestdif=difbattle[k]
        posbiggest=k

if biigestdif == 0:
    print('🌀Nenhuma onda foi selecionada como a menos acirrada e a mais favorável para nenhum do dois lados!')
elif resultodisput[posbiggest]=='vh':
    print(f'🌀Onda {posbiggest + 1} foi a menos acirrada e a mais favorável para os heróis!')
    tvondavenceddora=True
elif resultodisput[posbiggest]=='vv':
    print(f'🌀Onda {posbiggest + 1} foi a menos acirrada e a mais favorável para os vilões!')
    tvondavenceddora=True

#Segunda Análise

if tvondavenceddora:
    print(f'Participantes analisados: {geralchegou[posbiggest]}')

    print('Agora vamos ao resultado geral das ondas...')

winheroe = resultodisput.count('vh')
winvillain = resultodisput.count('vv')

print(f'Heróis: {winheroe} | Vilões: {winvillain}')

# Agora, quem ganha?

if winheroe > winvillain:
    print('Ufa, os heróis dominaram! Central City está seguro outra vez')
elif winvillain > winheroe:
    print('Ah, não. Os vilões vão dominar Central City e mandar todos os heróis embora!')
else:
    print('Ninguém é mais forte que ninguém. Heróis e vilões vão ter que entrar em consenso para viverem no mesmo espaço')



        
    
    






