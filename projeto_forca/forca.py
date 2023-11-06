from unidecode import unidecode
import os
import random

def tema(num):
    match num:
        case 0:
            return "animais"
        case 1:
            return "profissoes"
        case 2:
            return "paises"
        case _:
            return "Insira um numero de 0 a 2"

def dificuldade(chances):
    match chances:
        case 0:
            return "Facíl"
        case 1:
            return "Médio"
        case 2:
            return "Difícil"
        case _:
            return "Insira um numero de 0 a 2"

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
    secret = []
    for letra in palavra:
        if letra == " ":
            secret.append(" ")
        elif letra == "-":
            secret.append("-")
        else:
            secret.append("_")
    return secret

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

def calcular_pontos(erros):
    match erros: 
        case 0:
            return pontos == 700
        case 1:
            return pontos == 600
        case 2:
            return pontos == 500
        case 3:
            return pontos == 400
        case 4:
            return pontos == 300
        case 5:
            return pontos == 200
        case 6:
            return pontos == 100
        case _:
            return pontos == 0
        

# Função que soma os pontos obtidos nesta rodada à pontuação total do jogador
def somar_pontos(pontuacao_atual, pontos):
    pontuacao_atual += pontos  # Soma os pontos à pontuação total atual do jogador
    return pontuacao_atual  # Retorna a pontuação atualizada do jogado

def jogar():
    flag = True
    while(flag==True):
        print("\n-------- Bem vindo ao jogo da Forca! --------\n")

        print("Escolha um tema para jogar.\n[0] Animais\n[1] Profissões\n[2] Países")
        num = int(input("Tema: "))
        os.system("cls")
        print("Escolha uma dificulade do jogo.\n[0] Facíl\n[1] Normal\n[2] Difícil")
        chances = int(input("Dificuldade: "))
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
            os.system("cls")
            
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

            enforcou = erros == chancess
            acertou = "_" not in letras_acertadas

        if (acertou):
            print("\nParabéns, você ganhou!")
            print(f"A palavra era {palavra_secreta}\n")
        else:
            print("\nPuxa, você foi enforcado!")
            print(f"A palavra era {palavra_secreta}\n")
        print (f"Sua pontuação foi de {pontuacao_atual}\n")
        print('-------- FIM DE JOGO --------')

        jogar = int(input("Gostaria de jogar novamente?\n[0]não [1]sim -> "))
        if jogar == 1:
            flag = True
            os.system("cls")
        else:
            flag = False


if(__name__ == '__main__'):
    jogar()
