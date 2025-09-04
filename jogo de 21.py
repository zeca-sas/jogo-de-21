import random
import time
    #listas#

cartas_bot=[]
cartas_jog=[]
cartas=[2,3,4,5,6,7,8,9,10,10,10,10]

#====================================#
    #funçoes do jogo#
    
#rodada bot
def inimigo():
    chance=(random.choice(cartas))
    cartas_bot.append(chance)    

#rodada jogador
def jogada ():
    if jogo ==1 :
        escolha=(random.choice(cartas))
        cartas_jog.append(escolha)

#informações do jogo
def inf ():
    if informações == 1:
        return("""
Objetivo: chegar o mais perto de 21 sem passar.

Cartas: 2-10 valem o número; J, Q, K valem 10; Ás vale 1 ou 11.

Cada jogador recebe 2 cartas.

Pode “pedir” mais cartas ou “parar”.

O jogo dura 5 rodadasa.
               
============================================================================
""")

#tabela de pontuação
def pontos():
    return(f"""
suas cartas são as: {cartas_jog} que somando dá {sum(cartas_jog)}
============================================================================
as cartas do bot são: {cartas_bot} que somando dá {sum(cartas_bot)}
""")

#vitorioso
def vitori():
    if sum(cartas_jog)>sum(cartas_bot) and sum(cartas_jog)<=21:
        return("vitória do jogador")
    elif sum(cartas_jog)>sum(cartas_bot) and sum(cartas_jog)>21:
        return("derrota")
    elif sum(cartas_bot)>sum(cartas_jog) and sum(cartas_bot)<=21:
        return("derrota")
    elif sum(cartas_bot)>sum(cartas_jog) and sum(cartas_bot)>21:
        return("vitória do jogador")
    elif sum(cartas_jog) == sum(cartas_bot):
        return("empate")               
                     
#====================================#
jogador_continua = True
#====================================#

informações=int(input("""Gostaria de um breve tutorial?
[1]Sim                 
[2]Não                        
"""))
if informações == 1:
    print(inf())

for i in range(5):
    if jogador_continua == True:
        jogo=int(input("""esse é um jogo de 21:
        [1] comprar uma carta
        [2] parar o jogo
        """))
    print("----------------------------------------------------------------------------")
    if jogo == 1:
        jogada()
        if sum(cartas_bot)<17 or (sum(cartas_jog)>sum(cartas_bot) and sum(cartas_jog)<=21):
            inimigo()
        print(cartas_jog)
    elif jogo ==2:
        jogador_continua = False
        if sum(cartas_bot)<17 or (sum(cartas_jog)>sum(cartas_bot) and sum(cartas_jog)<=21):
            inimigo()
        break
        jogada()
    else:
        print("TOMAR NO SEU CU OU É 1 OU 2 SEU ANIMAL FILHA DA PUTA")
    print(pontos())
    print("----------------------------------------------------------------------------")
print(vitori())