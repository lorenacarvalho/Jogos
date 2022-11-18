import random
import niveis

def jogar():      
    print()
    print("*" * 50)
    print('{:*^50}'.format(' Bem vindo ao jogo de Adivinhação! '))
    print("*" * 50)

    numero_secreto = random.randrange(1, 101)
    #print(numero_secreto)
    
    print('Níveis de dificuldade: \n(1)Fácil (2)Médio (3)Difícil (4)Modo Infinito')
    nivel = int(input('Escolha o nível de dificuldade: '))

    if nivel == 1:
        total_de_tentativas = 20
        niveis.modo_limitado(numero_secreto, nivel=total_de_tentativas)
    elif nivel == 2:
        total_de_tentativas = 10
        niveis.modo_limitado(numero_secreto, nivel=total_de_tentativas)
    elif nivel == 3:
        total_de_tentativas = 5
        niveis.modo_limitado(numero_secreto, nivel=total_de_tentativas)
    elif nivel == 4:
        niveis.modo_infinito(numero_secreto)
    else:
        print('Você não digitou um nível válido')

    print("\n* Fim de Jogo *")

if __name__ == "__main__" :
    jogar()