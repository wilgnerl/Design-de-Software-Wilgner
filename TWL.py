#importando as bibliotecas
import random 

#Declarando dados utilizados na rodada
dado1 = 0
dado2 = 0
dadospoint = 0
resultado = 0
aposta = 0
fichas = 100


#fazendo o sorteio
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
resultado = dado1 + dado2

print('Resultado:',resultado)

#verificando a condição de ter ganho ou não para o tipo de jogo Twelve
if resultado == 12:
            print('você ganhou')
            fichas = fichas + aposta*30
            print('Agora você tem: ', fichas)
                    
else: 
            print('você perdeu')
            fichas = fichas -  aposta
            print('Agora você tem: ', fichas)
                    