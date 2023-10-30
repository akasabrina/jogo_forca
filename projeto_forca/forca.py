from unidecode import unidecode
import os
import random

def tema(num):
    match num:
        case 0:
            return "animais"
        case 1:
            return "profissoes"


def carrega_palavra_secreta(num):
    palavras = []
    tema_palavra = tema(num)
    with open(f"tema/{tema_palavra}.txt", "r", encoding="utf-8") as arquivo:
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

    if len(chute) == 1:
        os.system("cls")
        chute = chute.strip().upper()
        return chute
    else:
        print("Digite apenas uma letra.")
        pede_chute()


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

        print("Escolha um tema para jogar.\n[0] Animais\n[1] Profissões")
        num = int(input("Tema: "))
        os.system("cls")
        palavra_secreta = carrega_palavra_secreta(num)
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
                    marca_chute_correto(chute, letras_acertadas, palavra_secreta2)

                else:
                    erros += 1

                letras_usadas.append(chute)
                letras_faltando = str(letras_acertadas.count('_'))
                print(f"\nLetras usadas: {letras_usadas}\n")
                print('Ainda faltam acertar {} letras'.format(letras_faltando))
                print('Você ainda tem {} tentativas'.format(7-erros))
                desenha_forca(erros)
                print(letras_acertadas)

            else:
                print("Essa letra já foi usada")
                os.system("PAUSE")

            enforcou = erros == 7
            acertou = "_" not in letras_acertadas

        if (acertou):
            print("\nParabéns, você ganhou!")
            print(f"A palavra era {palavra_secreta}\n")
        else:
            print("\nPuxa, você foi enforcado!")
            print(f"A palavra era {palavra_secreta}\n")

        print('-------- FIM DE JOGO --------')

        jogar = int(input("Gostaria de jogar novamente?\n[0]não [1]sim -> "))
        if jogar == 1:
            flag = True
            os.system("cls")
        else:
            flag = False

if(__name__ == '__main__'):
    jogar()
