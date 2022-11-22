
def jogar():
    print()
    print("*" * 50)
    print('{:*^50}'.format(' Bem vindo ao jogo da Forca! '))
    print("*" * 50)

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ["_ " for i in palavra_secreta]
 
    erros = 0

    print(letras_acertadas)

    while True:
        chute = input('Tente uma letra? ')
        chute = chute.strip().upper()
        
        if chute in palavra_secreta:
            indice = 0
            print('Certo!')
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[indice] = letra
                indice += 1   
        else: 
            erros += 1
            print('Ops, letra errada! Faltam {} tentativas'.format(6 - erros)) 

        if erros == 6:
            break
        if '_ ' not in letras_acertadas:
            break
        print(letras_acertadas)


    if '_ ' not in letras_acertadas:
        print('Você ganhou!!')
    else:
        print('Você perdeu :(')
    print("** Fim do jogo ** ")
    
if(__name__ == "__main__"):
    jogar()
