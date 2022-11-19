def jogar():
    print()
    print("*" * 50)
    print('{:*^50}'.format(' Bem vindo ao jogo da Forca! '))
    print("*" * 50)

    palavra_secreta = 'banana'
    enforcou = False 
    acertou = False
    letras_acertadas = ["_ "] * len(palavra_secreta)

    print(letras_acertadas)
    while (not enforcou) and (not acertou):
        chute = input('Tente uma letra?')
        chute = chute.strip()

        indice = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[indice] = letra
            indice += 1
        print(letras_acertadas)

print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()
