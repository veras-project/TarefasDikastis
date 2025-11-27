#Fun?Never.Recursion
def print_inicial_forcavital(vit,boss):
    if boss=='Sif, a Grande Loba Cinzenta':
        print('Venha até mim guardiã do túmulo de Artorias... Vamos acabar logo com isso!')

    else:
        print('Enfim estou de frente ao Senhor das Cinzas! Nossa batalha será lendária e ecoará em todos os cantos de Lordran!!!')
    
    statsplayer=vit.split(' ')

    vida_jogador=float(statsplayer[0])*20
    dano_jogador=float(statsplayer[1])*5

    return dano_jogador,vida_jogador

def porrada(dps,hp,dpsboss,hpboss,boss,tente):
    if(hpboss<=0):
        return False, dps, hp, dpsboss, hpboss, boss, tente
    elif(hp<=0):
        return True, dps, hp, dpsboss, hpboss, boss, tente
    else:
        hpboss-=dps
        if(hpboss<=0):
            return False, dps, hp, dpsboss, hpboss, boss, tente
        else:
            if(boss=='Sif, a Grande Loba Cinzenta' and hpboss<=343.2):#Ficar De olho no menor igual aqui
                hp-=(dpsboss-15)
                tente+=1
                if(tente==1):
                    print("Sif, a Grande Loba Cinzenta está gravemente ferida! Essa é sua chance, acabe com o sofrimento dela!")#Ficar de Olho se é toda as vezes que ela tiver com pouca vida
            elif(boss=='Sif, a Grande Loba Cinzenta' and hpboss>343.2):
                hp-=dpsboss
            elif(boss=='Gwyn, Lorde das Cinzas' and hpboss<=2092.5):
                hp-=(dpsboss+10)
            else:
                hp-=dpsboss
            
            if(hp<=0):
                return True, dps, hp, dpsboss, hpboss, boss, tente

    perdeu,dps,hp,dpsboss,hpboss,boss,tente=porrada(dps,hp,dpsboss,hpboss,boss,tente)

    return perdeu, dps, hp, dpsboss,hpboss, boss, tente

#Variáveis Auxiliares
perdeu=True
tentativas=0
turno=0
tente=0
#Input Primarios e Prints
experiencia_jogador=input()
vitalidade_forca=input()
chefe_desafiado=input()

#Conversor EXP e VIT-->DPSplayer, DPSboss, LIFEplayer
DPSj,HPj=print_inicial_forcavital(vitalidade_forca,chefe_desafiado)
if chefe_desafiado=='Sif, a Grande Loba Cinzenta':
    HPb=3432.0
    DPSb=35.0
else:
    HPb=4185.0
    DPSb=55.0

#Recusão, ativar!
while perdeu:
    tentativas+=1
    if tentativas>=2:
        if experiencia_jogador=='Iniciante':
            DPSj=1.05*DPSj
            DPSb=0.9*DPSb
        elif experiencia_jogador=='Veterano':
            DPSj=1.1*DPSj
            DPSb=0.8*DPSb
        else:
            DPSj=1.2*DPSj
            DPSb=0.67*DPSb 
    perdeu,_,_,_,_,_,_=porrada(DPSj,HPj,DPSb,HPb,chefe_desafiado,tente) 

print(f'Você precisou de {tentativas} tentativas para vencer o(a) {chefe_desafiado}!')
if experiencia_jogador=='Iniciante':
    if tentativas<=5:
        print('Esse iniciante teve muita sorte, no próximo boss ele vai conhecer a verdadeira DOR!!!')
    elif tentativas>5 and tentativas<=10:
        print('Até que não foi tão ruim assim, continue assim novato!')
    else:
        print('Bem vindo a Dark Souls.')

elif experiencia_jogador=='Veterano':
    if tentativas<=5:
        print('Você já andou por Lordran antes, não é? Impressionante.')
    elif tentativas>5 and tentativas<=10:
        print('Nada mal, guerreiro. Mas os próximos desafios não terão piedade.')
    else:
        print('Mesmo os veteranos sangram em Dark Souls...')
else:
    if tentativas==1:
        print('Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!')
    elif tentativas>1 and tentativas<=10:
        print('Seu conhecimento sobre o ciclo é profundo. Quase como se já tivesse vivido isso mil vezes...')
    else:
        print('Nem mesmo os Mestres escapam ilesos da chama...')

if chefe_desafiado=='Sif, a Grande Loba Cinzenta':
    print('A grande loba cai com honra. No fundo dos seus olhos, havia apenas lealdade.')
else:
    print('A chama se apaga, e o silêncio reina em Lordran. Você derrotou o Senhor das Cinzas...')
    if tentativas==1:
        print('O ciclo foi quebrado... Você se tornou o verdadeiro Senhor das Cinzas. Um novo destino começa...')
    else:
        print('Mas o ciclo... o ciclo continua.')

