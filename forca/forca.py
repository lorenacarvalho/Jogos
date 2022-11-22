import random

LETRA_ESCONDIDA = '_'


def formatar(letras_acertadas):
    palavra = ''
    for letra in letras_acertadas:
        palavra += ' ' + letra + ' '
    return palavra


def jogar():
    print()
    print("*" * 50)
    print('{:*^50}'.format(' Bem vindo ao jogo da Forca! '))
    print("*" * 50)

    palavras_possiveis = []
    with open("forca/palavras_possiveis.txt", "r") as arquivo:
        palavras_possiveis = [linha.strip() for linha in arquivo]

    indice = random.randrange(0, len(palavras_possiveis))
    palavra_secreta = palavras_possiveis[indice].upper()

    letras_acertadas = [LETRA_ESCONDIDA for i in palavra_secreta]
    print(formatar(letras_acertadas))

    erros = 0
    ERROS_MAX = 6

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
            print('Ops, letra errada! Faltam {} tentativas'.format(ERROS_MAX - erros))

        if erros == ERROS_MAX:
            break
        if LETRA_ESCONDIDA not in letras_acertadas:
            break
        print(formatar(letras_acertadas))

    if LETRA_ESCONDIDA not in letras_acertadas:
        print(formatar(letras_acertadas))
        print('Você ganhou!!')
    else:
        print('Você perdeu :(')
    print("** Fim do jogo ** ")


if (__name__ == "__main__"):
    jogar()
