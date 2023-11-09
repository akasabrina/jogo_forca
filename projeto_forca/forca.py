from desenho   import desenha_forca  
from unidecode import unidecode 
import os 
import random  

# Função para mapear o número do tema para uma categoria específica
def tema(num_tema):
    match num_tema:
        case 1:
            return "animais"
        case 2:
            return "profissoes"
        case 3:
            return "paises"

# Função para mapear o número da dificuldade para o número de chances
def dificuldade(num_dificuldade):
    match num_dificuldade:
        case 1:
            return int(9)  # Fácil - 9 chances
        case 2:
            return int(7)  # Médio - 7 chances
        case 3: 
            return int(5)  # Difícil - 5 chances

# Função para carregar uma palavra secreta do arquivo de temas
def carrega_palavra_secreta(tema_palavra):
    palavras = []
    with open(f"tema/{tema_palavra}.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()  # Remove espaços em branco e caracteres de nova linha
            palavras.append(linha)

    # Gera um número aleatório entre 0 e o número de palavras disponíveis no tema
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


# Função para inicializar as letras da palavra secreta com '_' e espaços em branco
def inicializa_letras(palavra):
    secret = []
    for letra in palavra:
        # Verifica se a letra é um espaço em branco
        if letra == " ":
            secret.append(" ")
        # Verifica se a letra é um traço (por exemplo, em palavras compostas)
        elif letra == "-":
            secret.append("-")
        else:
            secret.append("_")
    return secret

# Função para solicitar um chute ao jogador
def pede_chute():
    while True:
        chute = input("\nDigite uma letra: ")  # Solicita a entrada do jogador

        # Verifica se a entrada do jogador tem exatamente um caractere e é uma letra
        if len(chute) == 1 and chute.isalpha():
            os.system("cls")  # Limpa a tela (para sistemas Windows)
            chute = chute.strip().upper()  # Remove espaços extras e converte para maiúsculas
            return chute
        else:
            os.system("cls")  # Limpa a tela (para sistemas Windows)
            print("Por favor, digite apenas uma letra válida.")


# Função para marcar o chute correto na palavra secreta
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):  # Verifica se a letra inserida pelo jogador corresponde à letra atual
            letras_acertadas[index] = letra  # Substitui o caractere '_' em letras_acertadas pela letra correta
        index += 1  # Avança para o próximo índice na próxima iteração do loop


# Função que permite ao jogador escolher um tema para jogar
def inicio():
    os.system("cls")  # Limpa a tela (para sistemas Windows)
    print("\n-------- Bem-vindo ao jogo da Forca! --------\n")
    print("Escolha um tema para jogar.\n[1] Animais\n[2] Profissões\n[3] Países")

    while True:  # Loop infinito para garantir que o jogador insira uma opção válida
        try:
            num = int(input("Tema: "))
            if 1 <= num <= 3:
                return num
            else:
                os.system('cls')
                # Informa ao jogador que a opção inserida não é válida
                print("Por favor, escolha uma opção válida .\n[1] Animais\n[2] Profissões\n[3] Países")  
        except ValueError:
            os.system('cls')
            # Informa ao jogador que deve inserir um número válido, caso contrário, ocorre um erro de valor
            print("Por favor, digite uma opção válida.\n[1] Animais\n[2] Profissões\n[3] Países")  


# Função para permitir ao jogador escolher a dificuldade do jogo
def tela_dificuldade():
    os.system("cls")  # Limpa a tela (para sistemas Windows)
    
    print("Escolha a dificuldade que quer jogar.")
    print("[1] Fácil - 9 chances\n[2] Médio - 7 chances\n[3] Difícil - 5 chances")

    while True:  # Loop infinito para garantir que o jogador insira uma opção válida
        try:
            num_dificuldade = int(input("Dificuldade: "))
            if 1 <= num_dificuldade <= 3:
                return num_dificuldade 
            else:
                os.system('cls')
                # Informa ao jogador que a opção inserida não é válida
                print("Por favor! Insira uma opção válida. \n[1] Fácil - 9 chances\n[2] Médio - 7 chances\n[3] Difícil - 5 chances")  
        except ValueError:
            os.system('cls')
            # Informa ao jogador que deve inserir um número válido, caso contrário, ocorre um erro de valor
            print("Por favor! Insira uma opção válida. \n[1] Fácil - 9 chances\n[2] Médio - 7 chances\n[3] Difícil - 5 chances")  


# Função que pergunta ao jogador se deseja jogar novamente após o fim do jogo
def proxima_partida():
    while True:  # Loop infinito para solicitar a decisão do jogador sobre a próxima partida
        print("Próxima partida?\n[1] Sim \n[2] Não ")
        
        try:
            jogar = int(input("Escolha: "))
            
            if jogar == 1:  # Se o jogador escolher 1 (sim), o jogo será reiniciado
                os.system("cls")
                break
            elif jogar == 2:  # Se o jogador escolher 2 (não), o jogo termina
                os.system("cls")
                print(f"Obrigado por jogar!")
                exit()  # Encerra o programa
            else:
                os.system("cls")
                # Informa ao jogador que a opção inserida não é válida
                print("Opção inválida. Por favor, escolha 1 para jogar novamente ou 2 para sair.")  

        except ValueError:  # Se o jogador inserir algo que não seja um número inteiro
            os.system("cls")  # Limpa a tela (para sistemas Windows)
            print("Opção inválida. Por favor, escolha 1 para jogar novamente ou 2 para sair.")  # Informa ao jogador que deve inserir uma opção válida


# Função que exibe a mensagem de fim de jogo e pergunta ao jogador se deseja jogar novamente
def Fim():
    os.system("cls")
    print('-------- FIM DE JOGO --------')
    
    while True:  # Loop infinito para solicitar a decisão do jogador sobre jogar novamente ou sair do jogo
        print("Gostaria de jogar novamente?\n[1] Sim\n[2] Não")

        try:
            jogar = int(input("Escolha: "))

            if jogar == 1:  # Se o jogador escolher 1 (sim), o jogo será reiniciado
                os.system("cls")
               
        
                return True  # Reinicia o loop principal para iniciar um novo jogo
            elif jogar == 2:  # Se o jogador escolher 2 (não), o jogo termina
                os.system("cls")
                print(f"Obrigado por jogar!")  # Exibe uma mensagem de agradecimento ao jogador
                exit()  # Termina o programa
            else:  # Se o jogador inserir um número diferente de 1 ou 2
                os.system("cls")
                print("Opção inválida. Por favor, escolha 1 para jogar novamente ou 2 para sair.")  # Informa ao jogador que a opção inserida não é válida
        except ValueError:  # Se o jogador inserir algo que não seja um número inteiro
            os.system("cls")
            print("Opção inválida. Por favor, escolha 1 para jogar novamente ou 2 para sair.")  # Informa ao jogador que deve inserir uma opção válida

# Função principal que inicia o jogo
def jogar():
    os.system("cls")
    flag = True  # Define a variável de controle para continuar jogando
    num_tema = inicio()
    num_dificuldade = tela_dificuldade()

    while flag:  # Loop principal do jogo, continua enquanto flag for True
        
        tema_palavra = tema(num_tema)  # Obtém o nome do tema escolhido
        
        chances = dificuldade(num_dificuldade)  # Obtém o número de chances com base na dificuldade
        os.system("cls")
    
        # Carrega uma palavra secreta aleatória do tema escolhido
        palavra_secreta = carrega_palavra_secreta(tema_palavra)
        palavra_secreta2 = unidecode(palavra_secreta)  # Remove acentos da palavra secreta
    
        letras_acertadas = inicializa_letras(palavra_secreta)  # Inicializa as letras acertadas com '_' e espaços
    
        enforcou = False  # Indica se o jogador foi enforcado
        acertou = False  # Indica se o jogador acertou a palavra
        erros = 0  # Contador de erros do jogador
        letras_faltando = len(palavra_secreta)  # Contador de letras faltando para acertar a palavra
        letras_usadas = []  # Lista para armazenar letras já usadas pelo jogador
    
        desenha_forca(num_dificuldade, erros)  # Desenha o estado inicial da forca
        print(letras_acertadas)  # Exibe as letras acertadas (inicialmente '_' e espaços) para o jogador
    
        while not acertou and not enforcou:  # Loop do jogo, continua enquanto o jogador não acertou ou foi enforcado
            chute = pede_chute() 
            os.system("cls") 
        
            if chute not in letras_usadas:
                if chute in palavra_secreta2:
                    marca_chute_correto(chute, letras_acertadas, palavra_secreta2)
                else:  # Se o chute não está na palavra secreta
                    erros += 1  # Incrementa o contador de erros do jogador
            
                letras_usadas.append(chute)  # Adiciona a letra à lista de letras usadas pelo jogador
                letras_faltando = str(letras_acertadas.count('_'))  # Calcula quantas letras ainda faltam para acertar
                print(f"Tema: {tema_palavra}\nLetras usadas: {letras_usadas}\n")
                print('Ainda faltam acertar {} letras'.format(letras_faltando))  # Informa quantas letras faltam para acertar a palavra
                print('Você ainda tem {} tentativas'.format(chances - erros))  # Informa quantas tentativas restantes ao jogador
                desenha_forca(num_dificuldade, erros)  # Desenha o estado atual da forca
                print(letras_acertadas)  # Exibe as letras acertadas para o jogador
            else:  # Se o jogador já usou a letra anteriormente
                os.system("cls")  # Limpa a tela do console
                print(f'Essa letra "{chute}" já foi usada')  # Informa ao jogador que a letra já foi usada
                print(f"\nLetras usadas: {letras_usadas}\n")  # Exibe a lista de letras já usadas pelo jogador
                print("-----Palavra Secreta-----\n")
                print(letras_acertadas)  # Exibe as letras acertadas para o jogador

            enforcou = erros == chances  # Verifica se o jogador foi enforcado (erros igual ao número de chances)
            acertou = "_" not in letras_acertadas  # Verifica se o jogador acertou todas as letras da palavra
    
        if acertou:  # Se o jogador acertou a palavra
            print("\nParabéns, você ganhou!")  # Informa ao jogador que ele ganhou o jogo
            print(f"A palavra era {palavra_secreta}\n")  # Exibe a palavra secreta ao jogador
            proxima_partida() # Se o jogador deseja jogar novamente
                
            
        else:  # Se o jogador foi enforcado
            print("\nPuxa, você foi enforcado!")  # Informa ao jogador que ele foi enforcado
            print(f"A palavra era {palavra_secreta}\n")  # Exibe a palavra secreta ao jogador
            os.system('pause')  # Pausa o programa para que o jogador possa ver a palavra antes de continuar
            while True:  # Loop externo para garantir que o jogo seja reiniciado após a função Fim()
                jogar()  # Chama a função principal do jogo
                Fim()  # Chama a função Fim() após o jogo terminar

if(__name__ == '__main__'):
    jogar()  # Chama a função jogar para iniciar o jogo
