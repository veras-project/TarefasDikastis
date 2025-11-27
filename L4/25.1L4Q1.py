#Hora de Aventura

rounds=int(input())

#Minhas Variáveis Globais

obj_name=[]
xpoint=[]
ypoint=[]

for _ in range(rounds):

    obj_name.append(input())
    xpoint.append(int(input()))
    ypoint.append(int(input()))

qntdesferas=obj_name.count('esfera')

#Calculando A Distância da Esfera

def calcdist(alpha, beta):
    D = ((alpha**2)+ (beta**2))**0.5
    return D

#Calculando Esfera Mais Perto

esferas=[]
locx=[]
locy=[]

def amaisperto():
    D1 = 999999999999
    idxdamaisperto = -1
    for i in range(len(obj_name)):
        if obj_name[i] == 'esfera':
            dist = calcdist(xpoint[i], ypoint[i])
            if dist < D1:
                D1 = dist
                idxdamaisperto = i
    return idxdamaisperto

            

#Tratamento de Dados

for i in range(rounds):
        
        if obj_name[i] == 'rocha':
            print("Radar: Rocha detectada! Bulma resmunga: 'Só um pedregulho cósmico... Sem valor para mim!'")
        elif obj_name[i] == 'árvore':
            print("Radar: Árvore à vista! Bulma comenta: 'Interessante, mas não brilha como uma esfera. Próximo alvo!'")
        elif obj_name[i]== 'nave':
            print("Radar: Sinal de nave! Bulma alerta: 'Pode ser Pilaf ou a Patrulha Vermelha! Melhor ficar atenta, mas o foco são as esferas!'")
        elif obj_name[i] != 'esfera':
            print(f'Radar: Detectado um(a) {obj_name[i]}. Não parece ser uma esfera... Continuando a busca.')   

if(qntdesferas==1):
    idx=obj_name.index('esfera')
    print(f'ALVO PRIORITÁRIO: Esfera | Distância: {calcdist(xpoint[idx],ypoint[idx]):.2f}m | Detecção Original: {idx+1}°')

elif(qntdesferas>1):

    idx1=amaisperto()
    distancia=calcdist(xpoint[idx1],ypoint[idx1])

    print(f'ALVO PRIORITÁRIO: Esfera | Distância: {distancia:.2f}m | Detecção Original: {idx1+1}°')

if qntdesferas==0:
    print('Radar varreu a área. Nenhuma esfera do dragão à vista desta vez!')