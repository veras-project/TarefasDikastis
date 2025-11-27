#Fun?nope,Ções
def Tribonacci(checkar,n2,n1,n,tentativa):
    if tentativa>=99:
        return False
    else:
        if checkar<=1:
            return True
        else:  
            n3=n2+n1+n
            if checkar==n3:
                return True
            elif checkar< n3:
                return False
            else:
                n=n1
                n1=n2
                n2=n3
                tentativa+=1
                fazparte=Tribonacci(checkar,n2,n1,n,tentativa)
                return fazparte
            
def Fatorial(checkar,mult,aux):
    if aux>=9:
        return False
    else:
        if checkar<=1:
            return True 
        else: 
            aux+=1
            mult=mult*aux
            if checkar==mult:
                return True
            elif checkar< mult:
                return False
            else:
                return Fatorial(checkar,mult,aux)
            
def calc_fatorial(numero,multiplo):
    if numero==1 or numero==0:
        return multiplo
    else:
        multiplo=multiplo* numero
        numero-=1
        return calc_fatorial(numero, multiplo)

def Catalan(n):
    if n <= 1:
        return 1
    
    res = 0
    for i in range(n):
        res += Catalan(i) * Catalan(n - i - 1)
    return res

def trinca_catalonica(check_trinca,ordem_catalao,n,ok):
    triplice_entente=[0,0,0]

    if n==len(check_trinca)-2:
        ok=False
        return ok,triplice_entente[0],triplice_entente[1],triplice_entente[2]
    
    for k in range(len(ordem_catalao)-2):
        if check_trinca[n]==ordem_catalao[k] and check_trinca[n+1]== ordem_catalao[k+1] and check_trinca[n+2]==ordem_catalao[k+2]:
            ok = True
            triplice_entente = [check_trinca[n], check_trinca[n+1], check_trinca[n+2]]
            return ok, triplice_entente[0], triplice_entente[1], triplice_entente[2]

    ok, t0, t1, t2 = trinca_catalonica(check_trinca, ordem_catalao, n + 1, ok)
    return ok, t0, t1, t2
  
  
def aprimoramento_arma(info_arma, sequencia_num, novo_nivel):
    if len(sequencia_num)==0: 
        return info_arma[1], novo_nivel
    else:
        agora = sequencia_num.pop(0)
        if info_arma[2] == 'basica':
            if novo_nivel < 20:
                if Tribonacci(agora, 1, 1, 0, 0):
                    novo_nivel += 1
                    print(f'Pronto, consegui mais um nível agora a/o {info_arma[0]} está no nível {novo_nivel}!')
                    info_arma[1] *= 1.1
        else:
            if novo_nivel < 10:
                if Fatorial(agora, 1, 0):
                    novo_nivel += 1
                    print(f'Pronto, consegui mais um nível agora a/o {info_arma[0]} está no nível {novo_nivel}!')
                    info_arma[1] *= 1.2
        
        info_arma[1], novo_nivel = aprimoramento_arma(info_arma, sequencia_num, novo_nivel)
        return int(info_arma[1]), novo_nivel
    
def ativacao_runa(serie_comandos,serie_catalao,HP,nome_runa):
    foi,n1,n2,n3=trinca_catalonica(serie_comandos,serie_catalao,0,False)
    updano=1
    malena=False
    if foi:
        print('Isso consegui ativar a Grande Runa.')
        print(f'Acabei precisando apenas dos números: {n1} - {n2} - {n3}.')
        if nome_runa=='Grande Runa de Godrick':
            HP[1]=round(HP[1]*1.10)
            updano=1.1
        elif nome_runa=='Grande Runa de Radahn':
            HP[1]=round(HP[1]*1.15)
            updano=1
        elif nome_runa=='Grande Runa de Morgott':
            HP[1]=round(HP[1]*1.25)
            updano=1
        else:
            updano=1
            malena=True
    else:
        print('Caramba não consegui ativar a Grande Runa, infelizmente vou ter que me contentar com as armas que vou levar.')
        updano=1
        malena=False

    return updano, malena, HP[1]

   
#Variáveis Apoio
runamalenaativada=False
updano=1
lista_armamento=[]
nvl=0
lista_catalonica=[]
derrotado=False
morreu=False
num_turno=0
kbouaszarma=False
for j in range(15):
    lista_catalonica.append(Catalan(j))

#Feijão & Arroz
nomeevida=input()
nomeevida=nomeevida.split(' - ')
nomeevida[1]=int(nomeevida[1])

qntd_acoes_pre_luta=int(input())

#Preparação
for _ in range(qntd_acoes_pre_luta):
    acao=input()
    if '-' in acao:
        arma_specs=acao.split(' - ')
        arma_specs[1]=int(arma_specs[1])
        print(f'Vou levar a/o {arma_specs[0]} ela/e vai ser de grande ajuda.')

        tenta=''
        sequencia=[]
        while tenta != 'fim':
            tenta=input()
            if tenta=='fim':
                None
            else:
                tenta=int(tenta)
                sequencia.append(tenta)     
        
        print('Hora de Aprimorar!!!')
        arma_specs[1],nvl=aprimoramento_arma(arma_specs,sequencia,0)
        if nvl>=1:
            print(f'Agora sim! Acho que a/o {arma_specs[0]} está forte o suficiente, consegui colocar ele/a para o nível {nvl}')
        else:
            print(f'Droga não consegui aumentar o nível da/o {arma_specs[0]}')
        lista_armamento.append(arma_specs)
        print()
        
    else:
        runa=acao
        print(f'A batalha vai ser difícil melhor tentar ativar uma runa!\nMe decidi vou tentar ativar a {runa}, ',end='')
        if runa=='Grande Runa de Godrick':
            print('acho que um pouco de tudo não é nada mal.')
        elif runa=='Grande Runa de Radahn':
            print('mais vida vai ajudar muito.')
        elif runa=='Grande Runa de Morgott':
            print('quanto mais vida melhor.')
        else:
            print('ela foi tão difícil de conseguir, tenho que testar ela pelo menos uma vez.')
        sequencia=[]
        for _ in range(10):
            sequencia.append(int(input()))   
        
        updano,runamalenaativada,nomeevida[1]=ativacao_runa(sequencia,lista_catalonica,nomeevida,runa)
        print()

#Fase Batalha
vilao_specs=input()
vilao_specs=vilao_specs.split(' - ')
vilao_specs[1],vilao_specs[2]=int(vilao_specs[1]),int(vilao_specs[2])
roundsmax=len(lista_armamento)
vida_atual=nomeevida[1]

while not morreu and num_turno<=roundsmax and not derrotado and not kbouaszarma:
    num_turno+=1
    print(f'{num_turno}° TURNO')
    print(f'Melhor conferir meus status antes de lutar -> vida: ({vida_atual}/{nomeevida[1]})')
    print(f'E o {vilao_specs[0]} ainda está com {vilao_specs[1]} pontos de vida')
    arma=lista_armamento.pop(0)
    arma[1]=int(arma[1]*updano)
    print(f'Atacando com {arma[0]}.\nConsegui causar {arma[1]} de dano no/a {vilao_specs[0]}!!!\nAcabei consumindo a/o {arma[0]}, hora de pegar outra arma do arsenal.')
    vilao_specs[1]-=arma[1]
    if runamalenaativada:
        valor_de_cura=int(0.05*nomeevida[1])
        if vida_atual==nomeevida[1] or vilao_specs[1]<=0:
            None
        else:
            vida_atual+=valor_de_cura
            if vida_atual>nomeevida[1]:
                valor_de_cura=vida_atual-nomeevida[1]
                vida_atual=nomeevida[1]
            print(f'Ainda bem que eu ativei a Grande Runa da Malenia, consegui recuperar {valor_de_cura}')
    if vilao_specs[1]<=0:
        derrotado=True
    else:
        print(f'Droga {vilao_specs[0]} ainda não morreu, acabei recebendo {vilao_specs[2]} de dano.')
        vida_atual-=vilao_specs[2]
        if vida_atual<=0:
            morreu=True   
        elif len(lista_armamento)==0:
            kbouaszarma=True#Eu sei que não é assim, mas é quase
    print()

#Fase Final
if derrotado:
    print('Great Enemy Felled')
    if len(lista_armamento)==0:
        print(f'Acabei usando tudo que eu trouxe, mas finalmente consegui derrotar a/o {vilao_specs[0]}.')
    else:
        print(f'Finalmente depois de tanto me preparar consegui derrotar a/o {vilao_specs[0]}.')
        armas_sobrando = []
        for arma in lista_armamento:
            armas_sobrando.append(arma[0])
        if len(armas_sobrando) > 0:
            print(f'Acho que me preparei bem eu ainda tenho {len(armas_sobrando)} arma/as sobrando são ela/as: {", ".join(armas_sobrando)}.')
else:    
    if morreu:
        print(f'You Died')
        print(f'Droga acabei morrendo para a/o {vilao_specs[0]} e ele ainda tem {vilao_specs[1]} pontos de vida, vou ter que trazer armas mais fortes da próxima vez.')
    elif kbouaszarma:
        print(f'Parece que eu não me preparei o suficiente, acabei usando tudo que tinha e a/o {vilao_specs[0]} ainda tem {vilao_specs[1]} pontos de vida, vou ter que me preparar mais da próxima vez.')
