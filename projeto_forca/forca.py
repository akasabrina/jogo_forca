from unidecode import unidecode
import os
import random

def carrega_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras(palavra):
    return ["-" if letra == "-" else "_" for letra in palavra]


def pede_chute():
    chute = input("\nDigite uma letra: ")
    os.system("cls")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    flag = True
    while(flag==True):
        print("\n-------- Bem vindo ao jogo da Forca! --------\n")

        palavra_secreta = carrega_palavra_secreta()
        palavra_secreta2 = unidecode(palavra_secreta)

        letras_acertadas = inicializa_letras(palavra_secreta)

        enforcou = False
        acertou = False
        erros = 0
        letras_faltando = len(letras_acertadas)
        letras_usadas = []

        print(letras_acertadas)
        while (not acertou and not enforcou):
            chute = pede_chute()

            if chute not in letras_usadas:
                if (chute in palavra_secreta2):
                    letras_usadas.append(chute)
                    letras_faltando = str(letras_acertadas.count('_'))
                    marca_chute_correto(chute, letras_acertadas, palavra_secreta2)

                    print(f"\nLetras usadas: {letras_usadas}\n")
                    print('Ainda faltam acertar {} letras'.format(letras_faltando))
                    print('Você ainda tem {} tentativas'.format(7-erros))
                    desenha_forca(erros)

                    if (letras_faltando == "0"):
                        print("PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(palavra_secreta.upper()))

                else:
                    letras_usadas.append(chute)
                    erros += 1
                    letras_faltando = str(letras_acertadas.count('_'))

                    print(f"\nLetras usadas: {letras_usadas}\n")
                    print('Ainda faltam acertar {} letras'.format(letras_faltando))
                    print('Você ainda tem {} tentativas'.format(7-erros))

                    desenha_forca(erros)

                enforcou = erros == 7
                acertou = "_" not in letras_acertadas

                print(letras_acertadas)
                
            else:
                print("Essa letra já foi usada")
                os.system("PAUSE")
            

        if (acertou):
            print("\nParabéns, você ganhou!")
            print(f"A palavra era {palavra_secreta}\n")
        else:
            print("\nPuxa, você foi enforcado!")
            print(f"A palavra era {palavra_secreta}\n")

        print('-------- FIM DE JOGO --------')

        jogar = input("Gostaria de jogar novamente?\n [y] sim [n] não -> ")
        if jogar.lower() == "y":
            flag = True
            os.system("cls")
        else:
            flag = False

if(__name__ == '__main__'):
    jogar()