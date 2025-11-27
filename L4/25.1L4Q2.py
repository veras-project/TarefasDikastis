#Funções
def whatsthepower(alpha):
    return len(alpha) % 8

def RtheyApair(beta,gama):
    if (beta =='Goku' and gama== 'Jiren') or (beta=='Jiren' and gama=='Goku'):
        return True
    elif (beta =='Frieza' and gama== 'Jiren') or (beta=='Jiren' and gama=='Frieza'):
        return True
    elif (beta =='Gohan' and gama== 'Namekuseijins') or (beta=='Namekuseijins' and gama=='Gohan'):
        return True
    elif (beta =='Androide 17' and gama== 'Ribrianne') or (beta=='Ribrianne' and gama=='Androide 17'):
        return True
    else:
        return False


#Aquela Parte +EZ

qtd_batalhas=int(input())

print(f'O torneio do poder irá começar com {qtd_batalhas} batalhas no dia de hoje! Vamos ver quais universos vão conseguir se manter vivos até o final do dia!')

#Variáveis

fighter1tech=[]
fighter2tech=[]
fighter3tech=[]
trio=False

#Looping

for _ in range(qtd_batalhas):
    bruto1=input()
    fighter1tech=bruto1.split(' - ')

    bruto2=input()
    fighter2tech=bruto2.split(' - ')

    #x1 ou covardia?

    trio=RtheyApair(fighter1tech[0], fighter2tech[0])

    if trio:
        bruto3=input()
        fighter3tech=bruto3.split(' - ')

        print(f'A intensidade dos dois lutadores motivou {fighter3tech[0]} a entrar na batalha também!')

        pow1=whatsthepower(fighter1tech[1])
        pow2=whatsthepower(fighter2tech[1])
        pow3=whatsthepower(fighter3tech[1])

        if fighter1tech[0] in ["Goku", "Frieza", "Androide 17", "Gohan"]:
            powf=pow1 + pow3

            if powf> pow2:
                print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {fighter1tech[1]}, {fighter2tech[1]} e {fighter3tech[1]}! A batalha acaba com {fighter1tech[0]} e {fighter3tech[0]} no topo!')
            else:
                print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {fighter1tech[1]}, {fighter2tech[1]} e {fighter3tech[1]}! A batalha acaba com {fighter2tech[0]} no topo!')

        else:
            powf=pow2 + pow3

            if powf> pow1:
                print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {fighter1tech[1]}, {fighter2tech[1]} e {fighter3tech[1]}! A batalha acaba com {fighter2tech[0]} e {fighter3tech[0]} no topo!')
            else:
                print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {fighter1tech[1]}, {fighter2tech[1]} e {fighter3tech[1]}! A batalha acaba com {fighter1tech[0]} no topo!')
 



    else:
        pow1=whatsthepower(fighter1tech[1])
        pow2=whatsthepower(fighter2tech[1])

        if pow1>pow2:
            print(f'Incrível! {fighter1tech[0]} mostrou sua força e defenderá seu universo até o final!')
        else:
            print(f'Incrível! {fighter2tech[0]} mostrou sua força e defenderá seu universo até o final!')
