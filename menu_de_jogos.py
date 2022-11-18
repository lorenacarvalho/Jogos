import adivinhacao
import forca
import os

def escolher_jogo():
    print()
    print("*" * 50)
    print('{:*^50}'.format(' MENU DE JOGOS '))
    print("*" * 50)
    print('(1)Jogo da Forca  (2)Jogo de Adivinhação')
    jogo = int(input('Escolha seu jogo: '))

    os.system('clear') or None
    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()  

      
if __name__ == '__main__':
    escolher_jogo()