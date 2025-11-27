#Fun?No.Ções

def bonusvitoria(beta,alpha):

    beta = beta * (1 + (alpha /100))

    return beta

def batalha(lutador,vida_guerreiroZ,motivacao):

    numero_do_turno=1
    vida_restante_vegeta=100
    motivacao_guerreiroZ=float(input())

    soberba=False
    batalha_encerrada= False
    vegeta_derrotado= False

    while not batalha_encerrada:

        print(f'--- Turno {numero_do_turno} ---')

        #VegetaAí

        tipo_de_golpeV=input()
        qtd_danoV=whatdedamage(tipo_de_golpeV,motivacao)
        
        if tipo_de_golpeV=='Potente':
            if not soberba:
                soberba=True
            else:
                vegeta_derrotado=True
                vida_restante_vegeta=0
                print('Vegeta usou dois Golpes Potentes seguidos e desmaiou com o esforço!')
                batalha_encerrada=True
        elif tipo_de_golpeV=='Normal':
            soberba=False

        if not vegeta_derrotado:
            print(f'Vegeta usou Golpe {tipo_de_golpeV} e causou {qtd_danoV:.0f} de dano!')
            vida_guerreiroZ-=qtd_danoV

            if vida_guerreiroZ<=0:
                vida_guerreiroZ=0
                batalha_encerrada=True

        #ContraQuem?

        if not batalha_encerrada:
            
            tipo_de_golpeZ=input()
            qtd_danoZ=whatdedamage(tipo_de_golpeZ,motivacao_guerreiroZ)

            print(f'{lutador} usou Golpe {tipo_de_golpeZ} e causou {qtd_danoZ:.0f} de dano!')


            vida_restante_vegeta-=qtd_danoZ

            if vida_restante_vegeta<0:
                vida_restante_vegeta = 0
                vegeta_derrotado=True
                batalha_encerrada=True
       
        print(f'|Vegeta: {vida_restante_vegeta:.0f} HP vs {lutador}: {vida_guerreiroZ:.0f} HP|')
        print()
        numero_do_turno+=1


    if not vegeta_derrotado:
        print('Vitória de Vegeta!')
        print(f'Vegeta venceu a batalha contra {lutador} com {vida_restante_vegeta:.0f} HP restantes!')
        print()
        motivacao=bonusvitoria(motivacao,vida_restante_vegeta)
        return False,motivacao
    else:
        print(f'Vegeta foi derrotado! A Terra está a salvo graças a {lutador}!')
        return True, motivacao

def whatdedamage(tpde_golpe,mtv):

    if tpde_golpe=='Normal':
        dmg=20
    else:
        dmg=40
    return int(dmg*mtv)

#Input e Introdução
champion=False
motivacao_inicial=float(input())
guerreiroevida=[['Piccolo',100],['Gohan',100],['Goku',200]]
over=False
round=0

print('A saga de Vegeta começa!')
print()


# A PARTE MAIS DIFÌCIL DO CÒDIGO
while not over:
    print(f'--- Iniciando o combate contra {guerreiroevida[round][0]} ---')
    print()


    over,motivacao_inicial=batalha(guerreiroevida[round][0],guerreiroevida[round][1],motivacao_inicial)

    if round == 2:
        if not over:
            champion=True
            over=True
    
    round+=1


if champion:
    print('Vegeta derrotou todos os Guerreiros Z! A Terra foi conquistada!')


    