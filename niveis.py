#cabeçalho até a escolha do nível de dificuldade
def modo_infinito(numero_secreto):
    chute = int(input('Digite um número entre 1 e 100: '))
    rodadas = 0
    while chute != numero_secreto:
        rodadas += 1
        print('\nTentativa {}'.format(rodadas))
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto 
        
        if chute <= 0 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
        elif chute_maior:
            print('Você errou! Você digitou um numero maior que o numero secreto \n')
        elif chute_menor:
            print('Você errou! Você digitou um numero menor que o numero secreto \n')
        chute = int(input('Tente novamente! Digite um número: '))
    else :
        print('Você acertou!')
    
def modo_limitado(numero_secreto, nivel):
    pontos = 1000
    for rodada in range(1, nivel + 1):
    
        print('\nTentativa {}'.format(rodada))
        chute = int(input('Digite um número: '))
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto 
        acerto = chute == numero_secreto
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        if chute <= 0 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
        elif acerto:
            print("\nVocê acertou! \nPontuação total: {}".format(pontos))
            break
        elif chute_maior:
            print('Você errou! Você digitou um numero maior que o numero secreto. \n')
        elif chute_menor:
            print('Você errou! Você digitou um numero menor que o numero secreto. \n')
        if rodada == nivel:
            print("O número secreto era: {}. Você fez {} pontos.".format(numero_secreto, pontos))
      