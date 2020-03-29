#Declaração de Bibliotecas
import random
import time

#Declarando fichas
fichas = 100

#Apresentando fichas:
print('Essas são suas fichas:',fichas)
time.sleep(2)

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
if pergunta == 2:
    print('Você escolheu Field')
if pergunta == 3:
    print('Você escolheu Any Craps')
if pergunta == 4:
    print('Você escolheu Twelve')

escolha = True
while escolha:
    
    pergunta1 = input('Você deseja Apostar ou Sair ?')
    if pergunta1 == 'sair':
        escolha = False
    else:
        if fichas == 0:
            escolha = False
        else:
            fichas = fichas - 10
            if fichas == 0:
                print('Sua quantidade de fichas:',fichas)
                time.sleep(1)
                print('Voce perdeu')
                escolha = False
            else:
                print('Sua quantidade de fichas:',fichas)
        




 