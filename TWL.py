import random 

#Declarando dados utilizados na rodada
dado1 = 0
dado2 = 0
dadospoint = 0
resultado = 0
aposta = 0
fichas = 100

TWL = True
while TWL:
    pergunta1 = input("Você deseja apostar ou sair? ")

    if pergunta1 == 'sair':
            TWL = False
    if pergunta1 != 'sair':
        #fazendo o sorteio dos dados e a soma dos resultados
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            resultado = dado1 + dado2     
            #verificando a condição de ter ganho ou não
            if resultado == 12:
                print('você ganhou')
                fichas = fichas + aposta*30
                print('Agora você tem: ', fichas)
                TWL = False
            else: 
                print('você perdeu')
                fichas = fichas -  aposta
                print('Agora você tem: ', fichas)
                TWL = False
            