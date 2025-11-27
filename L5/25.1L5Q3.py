#Fun?NeverEverAgain.Ções
def forja(obj_melhorar, acao_ordem):
    powup = ['S', 'D', 'I', 'F', 'A']
    upgrade=acao_ordem.pop(0)
    if isinstance(upgrade, list):
        obj_melhorar[2], obj_melhorar[3] = sublistas(upgrade, obj_melhorar,True,[])
    elif upgrade == '+' or upgrade == '-':
        if obj_melhorar[1] == 'normal' and upgrade == '+':
            obj_melhorar[2] += 3
        elif obj_melhorar[1] == 'especial' and upgrade == '-':
            obj_melhorar[2] += 5
    elif upgrade in powup:
        #Vendo Característcas 
        if upgrade == 'S' and 'força' in obj_melhorar:
            obj_melhorar[2] += 1
        elif upgrade == 'D' and 'destreza' in obj_melhorar:
            obj_melhorar[2] += 1
        elif upgrade == 'I' and 'inteligência' in obj_melhorar:
            obj_melhorar[2] += 1
        elif upgrade == 'F' and 'fé' in obj_melhorar:
            obj_melhorar[2] += 1
        elif upgrade == 'A' and 'arcano' in obj_melhorar:
            obj_melhorar[2] += 1    
        #Vendo Atributos
        if upgrade == 'S' and 'fogo' in obj_melhorar:
            obj_melhorar[2] += 1
        elif upgrade == 'D' and 'físico' in obj_melhorar:
            obj_melhorar[2] += 1
        elif upgrade == 'I' and 'mágico' in obj_melhorar:
            obj_melhorar[2] += 1
        elif upgrade == 'F' and 'dourado' in obj_melhorar:
            obj_melhorar[2] += 1
        elif upgrade == 'A' and 'oculto' in obj_melhorar:
            obj_melhorar[2] += 1 
    if len(acao_ordem)==0:
        return obj_melhorar[2], obj_melhorar[3]
    else:
        obj_melhorar[2],obj_melhorar[3]=forja(obj_melhorar,acao_ordem)
        return obj_melhorar[2], obj_melhorar[3]

def sublistas(sublista, obj_melhorar,primeiro,obj_melhorar_reserva):
    if primeiro:
        obj_melhorar_reserva = list(obj_melhorar)
        primeiro=False

        if obj_melhorar[3] == 'físico':
            obj_melhorar[3] = 'mágico'
        elif obj_melhorar[3] == 'mágico':
            obj_melhorar[3] = 'fogo'
        elif obj_melhorar[3] == 'fogo':
            obj_melhorar[3] = 'dourado'
        elif obj_melhorar[3] == 'dourado':
            obj_melhorar[3] = 'oculto'
        else:
            obj_melhorar[3] = 'físico'  
    powup = ['S', 'D', 'I', 'F', 'A']

    miniupgrade=sublista.pop(0)

    if isinstance(miniupgrade, list):
        obj_melhorar[2], obj_melhorar[3] = sublistas(miniupgrade, obj_melhorar,True,obj_melhorar_reserva)
    elif miniupgrade == 'R':
        print('Hmm, não acho que isso vai funcionar...')
        print(f'{obj_melhorar[0]}: {obj_melhorar[2]} -> {obj_melhorar_reserva[2]}')
        print(f'Afinidade revertida para {obj_melhorar_reserva[3]}')

        obj_melhorar[2],obj_melhorar[3]=obj_melhorar_reserva[2], obj_melhorar_reserva[3]
    elif miniupgrade == '+' or miniupgrade == '-':
        if obj_melhorar[1] == 'normal' and miniupgrade == '+':
            obj_melhorar[2] += 3
        elif obj_melhorar[1] == 'especial' and miniupgrade == '-':
            obj_melhorar[2] += 5
    elif miniupgrade in powup:
        if miniupgrade == 'S' and 'força' in obj_melhorar:
            obj_melhorar[2] += 1
        elif miniupgrade == 'D' and 'destreza' in obj_melhorar:
            obj_melhorar[2] += 1
        elif miniupgrade == 'I' and 'inteligência' in obj_melhorar:
            obj_melhorar[2] += 1
        elif miniupgrade == 'F' and 'fé' in obj_melhorar:
            obj_melhorar[2] += 1
        elif miniupgrade == 'A' and 'arcano' in obj_melhorar:
            obj_melhorar[2] += 1

        if miniupgrade == 'S' and 'fogo' in obj_melhorar:
            obj_melhorar[2] += 1
        elif miniupgrade == 'D' and 'físico' in obj_melhorar:
            obj_melhorar[2] += 1
        elif miniupgrade == 'I' and 'mágico' in obj_melhorar:
            obj_melhorar[2] += 1
        elif miniupgrade == 'F' and 'dourado' in obj_melhorar:
            obj_melhorar[2] += 1
        elif miniupgrade == 'A' and 'oculto' in obj_melhorar:
            obj_melhorar[2] += 1
    if len(sublista)==0:
        return obj_melhorar[2], obj_melhorar[3]
    else:
        obj_melhorar[2],obj_melhorar[3]=sublistas(sublista,obj_melhorar,primeiro, obj_melhorar_reserva)
        return obj_melhorar[2], obj_melhorar[3]

#Feijão Com Arroz
objetos_melhoraveis=[]
serie_alteracoes=[]
lista_armas=[]
specs_armas=[]
qntd_armas_fogo=0
qntd_armas_douradas=0
qntd_armas_genericas=0

print('Não aguento mais morrer para a Malenia, Blade of Miquella...')
print('Vou refazer minha build!\n')
dados_brutos_objetos_melhoraveis=input()
#Escolhendo o Arsenal
while dados_brutos_objetos_melhoraveis!='finalizar':
    objetos_melhoraveis=dados_brutos_objetos_melhoraveis.split(' - ')#criei lista
    for i in range(len(objetos_melhoraveis)):
        if objetos_melhoraveis[i].isnumeric():
            objetos_melhoraveis[i]=int(objetos_melhoraveis[i])
        
    lista_armas.append(objetos_melhoraveis)

    dados_brutos_objetos_melhoraveis=input()

#Fazendo a melhoria
for j in range(len(lista_armas)):
    serie_alteracoes=input()
    serie_alteracoes=eval(serie_alteracoes)
    pow_final,afin_final=forja(lista_armas[j],serie_alteracoes)
    print(f'{lista_armas[j][0]} aprimorado!')
    specs_armas.append([pow_final,afin_final])

#Fim
print('Inventário:')
for k in range(len(lista_armas)):
    print(f'- {lista_armas[k][0]}: {specs_armas[k][0]}')
    print(f'- afinidade: {specs_armas[k][1]}')
    if specs_armas[k][1]=='fogo':
        print('Fogo... é uma das fraquezas da Malenia!!!')
        qntd_armas_fogo+=1
    elif specs_armas[k][1]=='dourado':
        print('É, não acho que uma arma de fé vá me ajudar muito...')
        qntd_armas_douradas+=1
    else:
        qntd_armas_genericas+=1
print('')

if(qntd_armas_fogo>0 and qntd_armas_fogo>qntd_armas_genericas and qntd_armas_fogo>qntd_armas_douradas):
    print('Muitas armas de fogo, ela não vai ter chance!')
elif(qntd_armas_douradas>0 and qntd_armas_douradas>qntd_armas_genericas and qntd_armas_douradas>qntd_armas_fogo):
    print('Acho que vou ter que refazer meus aprimoramentos...')
else:
    print('Analisando meu inventário agora, acho que consigo vencer, pode vir, Malenia, Blade of Miquella!!')
