#Declaração de Bibliotecas
import random
import time

#Declarando fichas
fichas = 100

#Declarando dados utilizados para rodada
dado1 = 0
dado2 = 0
dadosPoint = 0
resultado = 0
NovoResultado = 0
inicio = True

#Variaveis de permissão
PLB = False
Point = False
FIL = False
ACS = False
TWL = False
escolha = False

#Variavel de aposta
aposta =  0


while inicio:
    pergunta1 = input('Você deseja Apostar ou Sair ?')
    if pergunta1 == 'Sair' or fichas == 0:
        inicio = False
    
    else:
        print('Essas são suas fichas:',fichas)
        if fichas == 0:
            PBL = False
            PLB = False
            Point = False
            FIL = False
            ACS = False
            TWL = False
            inicio = False
        
        time.sleep(1)
        pergunta2 = int(input('Quantas das suas fichas você quer apostar ? '))
        aposta = pergunta2
        
        if pergunta2 > fichas:
            print('Você não tem fichas suficientes')
            time.sleep(1)
            print('Suas fichas:',fichas)
            print('Comece denovo!')
            PBL = False
            PLB = False
            Point = False
            FIL = False
            ACS = False
            TWL = False
            inicio = False

        #Apresentando opções de apostas:
        print('Opções de apostas:')
        time.sleep(1)
        print('1 - Pass line Bet')
        time.sleep(1)
        print('2 - Field')
        time.sleep(1)
        print('3 - Any Craps')
        time.sleep(1)
        print('4 - Twelve')
        time.sleep(1)

        #Escolha a opção de aposta:
        pergunta = int(input('Escolha uma opção de apostas de 1 a 4: '))


        #Mostrando qual aposta foi escolhida
        if pergunta == 1:
            print('Você escolheu Pass Line Bet')
            PBL = True
        if pergunta == 2:
            print('Você escolheu Field')
        if pergunta == 3:
            print('Você escolheu Any Craps')
            ACS = True
        if pergunta == 4:
            print('Você escolheu Twelve')

        while ACS == True:
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            resultado = dado1 + dado2
            print('Resultado:',resultado)
            time.sleep(1)

            if resultado == 2 or resultado == 3 or resultado == 12:
                print('você ganhou')
                fichas = fichas + (aposta*7)
                print('Agora você tem: ', fichas)
                ACS = False
            
            else:
                print('Você perdeu')
                fichas = fichas - aposta
                print('Agora você tem: ', fichas)
                ACS = False