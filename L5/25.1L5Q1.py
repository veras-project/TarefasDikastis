#Fun?No.Ções
def batalha_honrrosa(i,vit_sek,vit_genin,post_sek,post_genin,num_cabaças):
    if(vit_sek<=0 or post_sek>=100):
        if vit_sek<=0:
            print('Sekiro cai de joelhos, derrotado...')
            print('====================================')
            print('Vitória de Genichiro: Morte.')
        else:
            print('A postura do lobo foi quebrada! Ele não consegue se defender e é derrotado!')
            print('====================================')
            print('Vitória de Genichiro: Morte.')

        return None
    elif(vit_genin<=0 or post_genin>=100):
        i+=1
        print(f'--- Turno {i} ---')
        print('Genichiro está de joelhos e vulnerável! Acabe com isso, Lobo!')
        acao_sekiro=input()
        if acao_sekiro=='ataque':
            print('Sekiro executa um Golpe Mortal em Genichiro!')
            print('====================================')
            print('Vitória de Sekiro: Golpe Mortal!')
        else:
            print('O lobo hesitou no seu golpe final, Genichiro recupera sua postura! Cuidado, Lobo!')
            if post_genin>=100:
                post_genin-=50
                if vit_genin<50:
                    vit_genin=50
            else:
                vit_genin+=50
                post_genin=50
            batalha_honrrosa(i,vit_sek,vit_genin,post_sek,post_genin,num_cabaças)      
        return None
    else:
        lista_acoes_sekiro=['ataque','defesa','defesa perfeita','usar cabaça','desviar','contra ataque mikiri']
        lista_acoes_genichiro=['ataque','defesa','recuperação de postura','ataque kanji']
        i+=1
        print(f'--- Turno {i} ---')

        act_genin=input()
        while act_genin not in lista_acoes_genichiro:
            print('Genichiro não tem esse movimento em seu arsenal.')
            act_genin=input()
        act_sek=input()
        while act_sek not in lista_acoes_sekiro:
            print('O lobo não adquiriu esse movimento ainda.')
            act_sek=input()
    
        if act_genin=='ataque':
            if act_sek=='ataque':
                vit_sek-=25
                vit_genin-=10
                post_genin+=15
                print('Clima de tensão! Os dois atacam numa luta implacável!')
            elif act_sek=='defesa':
                vit_sek-=10
                post_sek+=20
                print('Sekiro firma sua espada e se defende, absorvendo o impacto em sua postura!')
            elif act_sek=='defesa perfeita':
                post_genin+=25
                print('Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!')
            elif act_sek=='usar cabaça':
                if num_cabaças>0:
                    num_cabaças-=1
                    vit_sek-=25
                    print('Sekiro tenta curar, mas é punido pelo ataque impiedoso de Genichiro!')
                else:
                    vit_sek-=25
                    print('Sekiro busca sua cabaça, mas ela está vazia!\nEnquanto Sekiro se distrai, Genichiro avança com um ataque certeiro!')
            elif act_sek=='desviar':
                print('O lobo desvia agilmente do ataque comum de Genichiro!')
            elif act_sek=='contra ataque mikiri':
                post_genin+=10
                print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro faz um movimento comum.')

        elif act_genin=='defesa':
            if act_sek=='ataque':
                post_genin+=5
                print('Genichiro prevê o movimento e apara o golpe de Sekiro com sua lâmina!')
            elif act_sek=='defesa':
                print('Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.')
            elif act_sek=='defesa perfeita':
                print('Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.')
            elif act_sek=='usar cabaça':
                if num_cabaças>0:
                    vit_sek+=25
                    num_cabaças-=1
                    print('Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.')
                else:
                    print('Sekiro busca sua cabaça, mas ela está vazia!\nGenichiro mantém a guarda, enquanto o lobo percebe seu erro.')
            elif act_sek=='desviar':
                print('O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.')
            elif act_sek=='contra ataque mikiri':
                print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.')

        elif act_genin=='recuperação de postura':
            if act_sek=='ataque':
                vit_genin-=10
                post_genin+=15
                print('Genichiro ia recuperar sua postura mas o lobo foi mais rápido, um grande ataque por parte do lobo!')
            elif act_sek=='defesa':
                post_genin=0
                print('Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
            elif act_sek=='defesa perfeita':
                post_genin=0
                print('Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
            elif act_sek=='usar cabaça':
                if num_cabaças>0:
                    num_cabaças-=1
                    post_genin=0
                    print('Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
                else:
                    post_genin=0
                    print('Sekiro busca sua cabaça, mas ela está vazia!\nGenichiro aproveita a hesitação do lobo para recuperar sua postura.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
            elif act_sek=='desviar':
                post_genin=0
                print('O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
            elif act_sek=='contra ataque mikiri':
                post_genin=0
                print('    O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.\nGenichiro consegue recuperar sua postura, cuidado lobo!')   
        elif act_genin=='ataque kanji':
            if act_sek=='usar cabaça':
                if num_cabaças>0:
                    num_cabaças-=1
                    vit_sek-=50
                    post_sek+=20
                    print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!')
                else:
                    vit_sek-=50
                    post_sek+=20
                    print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!\nPara piorar, Sekiro nem sequer tinha uma cabaça para usar!')

            elif act_sek=='desviar':
                print('O lobo desvia do ataque especial de Genichiro com muita agilidade!')
            elif act_sek=='contra ataque mikiri':
                post_genin+=25
                print('O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!')
            else:
                vit_sek-=50
                post_sek+=20
                print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!')
   
    batalha_honrrosa(i,vit_sek,vit_genin,post_sek,post_genin,num_cabaças)
    return None

                
            


    
#Variáveis Auxiliares
i=0
vitalidade_sekiro_inicial=100
postura_sekiro_inicial=0
vitaldade_genisha_incial=100
postura_genisha_inicial=0
quantidade_cabaças=2
#Esquema Principal
print('O duelo começa! Suas decisões determinarão o vencedor.')
batalha_honrrosa(i,vitalidade_sekiro_inicial,vitaldade_genisha_incial,postura_sekiro_inicial,postura_genisha_inicial,quantidade_cabaças)
