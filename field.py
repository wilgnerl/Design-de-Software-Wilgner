#declarando bibliotecas 
import random 

#Declarando dados utilizados na rodada
dado1 = 0
dado2 = 0
dadospoint = 0
resultado = 0
aposta = 0
fichas = 100

#escolha é uma flag para o While
FIL = True
while FIL:
                dado1 = random.randint(1,6)
                dado2 = random.randint(1,6)
                resultado = dado1 + dado2 
                print('Resultado:',resultado)
                time.sleep(1)

            #verificando as regras do jogo com base no resultado do sorteio
                if resultado == 5 or resultado == 6 or resultado == 7 or resultado == 8:
                    print("Você perdeu")
                    fichas = fichas - aposta
                    print('Agora você tem: ', fichas)
                    FIL = False

                elif resultado == 3 or resultado == 4 or resultado == 9 or resultado == 10 or resultado == 11:
                    print('você ganhou')
                    fichas = fichas + aposta
                    print('Agora você tem: ', fichas)
                    FIL = False

                elif resultado == 2:
                    print('você ganhou')
                    fichas = fichas + 2*aposta
                    print('Agora você tem: ', fichas)
                    FIL = False
                    
                elif resultado == 12:
                    print('você ganhou')
                    fichas = fichas + 3*aposta
                    print('Agora você tem: ', fichas)
                    FIL = False


