# Importa o módulo tkinter como tk, usado para criar a interface gráfica
import tkinter as tk
# Importa submódulos específicos do tkinter
from tkinter import messagebox, simpledialog
# Importa a função unidecode do módulo unidecode, usada para remover acentos de palavras
from unidecode import unidecode
# Importa o módulo random para gerar números aleatórios
import random

# Define a classe JogoDaForcaGUI
class JogoDaForcaGUI:
    # Método de inicialização da classe
    def __init__(self, master):
        # Atribui a instância de tkinter ao atributo master
        self.master = master
        # Configura o título da janela principal
        self.master.title("Jogo da Forca")
        # Configura as dimensões da janela principal
        self.master.geometry("1000x600")
        # Configura a cor de fundo da janela principal
        self.master.configure(bg="#09240B")
        # Inicializa variáveis de controle do jogo
        self.tema = 0
        self.tema_escolhido = tk.StringVar()  # Variável para armazenar o tema escolhido
        self.tema_escolhido.set("")  # Inicializa com uma string vazia
        
        self.dificuldade = 0
        self.chances = 0
        self.palavra_secreta = ""
        self.palavra_secreta_sem_acentos = ""
        self.letras_acertadas = []
        self.erros = 0
        # Chama o método para inicializar a interface
        self.menu_principal()


    def menu_principal(self):
        tk.Label(self.master, text="Jogo Da Forca", font=("Comic Sans Ms", 36), bg="#09240B", fg="#FFFFFF", width=15, height=1).pack(pady=200)
        tk.Button(self.master, text="começar", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF", width=8, height=1, command=self.inicializar_interface).pack(pady=10)
        self.canvas_forca = tk.Canvas(self.master, width=280, height=500, bg="#09240B", highlightthickness=0, bd=0)  # Define a área para desenhar a forca
        self.canvas_forca.place(x=0, y=85, anchor=tk.NW)
        
        self.forca_desenho_menu()
    def forca_desenho_menu(self):
        # Verifica se o canvas_forca existe
        if hasattr(self, "canvas_forca") and self.canvas_forca:
            # Limpa a forca anterior
            self.canvas_forca.delete("all")


            # Coordenadas iniciais
            x, y = 100, 50

            # Desenha a haste vertical e horizontal desde o início
            self.canvas_forca.create_line(x + 0, y, x + 0, y + 335, width=10, fill="White")  # Haste vertical
            self.canvas_forca.create_line(x, y + 5, x + 135, y + 5, width=10, fill="White")  # Haste horizontal
            self.canvas_forca.create_line(x, y + 40, x + 55, y + 5, width=10, fill="White")  # Haste diagonal
            self.canvas_forca.create_line(x - 50, y + 335, x + 70, y + 335, width=10, fill="White")  # base
            self.canvas_forca.create_line(x + 125, y, x + 125, y + 55, width=2, fill="White")  # Corda

            self.cabeca()
            self.tronco()
            self.braco_esq()
            self.braco_dir()
            self.perna_esq()
            self.perna_dir()
            self.olho_esq()
            self.olho_dir()


    # Método para inicializar a interface gráfica
    def inicializar_interface(self):
        self.limpar_tela()
        # Chama o método para configurar o menu de escolha
        self.menu_escolha()

    # Método para configurar o menu de escolha de tema e dificuldade
    def menu_escolha(self):
        # Cria um frame para o menu de tema
        self.frame_tema = tk.Frame(self.master)
        # Faz o frame ser exibido na interface
        self.frame_tema.pack(pady=10)

        # Cria um rótulo para indicar a escolha de tema
        tk.Label(self.frame_tema, text="Escolha um tema:", font=("Comic Sans Ms", 36), bg="#09240B", fg="#FFFFFF", width=15, height=1).pack(pady=0)

        # Cria um frame vazio para espaçamento
        tk.Frame(self.frame_tema, bg="#09240b").pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # Cria botões para temas específicos, cada um com um comando associado
        tk.Button(self.frame_tema, text="Animais", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF", width=8, height=1, command=lambda: self.escolher_tema(1)).pack(side=tk.LEFT)
        tk.Button(self.frame_tema, text="Profissões", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF", width=8, height=1, command=lambda: self.escolher_tema(2)).pack(side=tk.LEFT)
        tk.Button(self.frame_tema, text="Países", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF", width=8, height=1, command=lambda: self.escolher_tema(3)).pack(side=tk.LEFT)
        # Cria um frame vazio para espaçamento
        tk.Frame(self.frame_tema, bg="#09240b").pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Cria um frame para o menu de dificuldade
        self.frame_dificuldade = tk.Frame(self.master)
        # Faz o frame ser exibido na interface
        self.frame_dificuldade.pack(pady=10)

        # Cria um rótulo para indicar a escolha de dificuldade
        tk.Label(self.frame_dificuldade, text="Escolha uma dificuldade:", font=("Comic Sans Ms", 36), bg="#09240B", fg="#FFFFFF", width=20, height=1).pack(pady=0)

        # Cria um frame vazio para espaçamento
        tk.Frame(self.frame_dificuldade, bg="#09240b").pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # Cria botões para dificuldades específicas, cada um com um comando associado
        tk.Button(self.frame_dificuldade, text="Fácil", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF", width=8, height=1, command=lambda: self.escolher_dificuldade(1)).pack(side=tk.LEFT)
        tk.Button(self.frame_dificuldade, text="Médio", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF", width=8, height=1, command=lambda: self.escolher_dificuldade(2)).pack(side=tk.LEFT)
        tk.Button(self.frame_dificuldade, text="Difícil", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF", width=8, height=1, command=lambda: self.escolher_dificuldade(3)).pack(side=tk.LEFT)

        # Adiciona um frame vazio para centralizar horizontalmente
        tk.Frame(self.frame_dificuldade, bg="#09240b").pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Cria um frame para a exibição do jogo
        self.frame_jogo = tk.Frame(self.master, bg="#09240B")
        # Faz o frame ser exibido na interface
        self.frame_jogo.pack(pady=10)

        # Cria rótulos para exibir o tema e a dificuldade escolhidos
        self.label_tema_escolhido = tk.Label(self.frame_jogo, text="Tema escolhido:", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF")
        self.label_tema_escolhido.pack(pady = 10)
        self.label_tema = tk.Label(self.frame_jogo, text="", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF")
        self.label_tema.pack()

        self.label_dificuldade_escolhida = tk.Label(self.frame_jogo, text="Dificuldade escolhida:", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF")
        self.label_dificuldade_escolhida.pack()
        self.label_dificuldade = tk.Label(self.frame_jogo, text="", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF")
        self.label_dificuldade.pack()

        # Define a variável para rastrear se as escolhas foram feitas
        self.escolhas_feitas = False
        # Chama o método para verificar se as escolhas foram feitas
        self.verificar_escolhas()

    # Método para verificar se ambas as escolhas foram feitas e, se sim, habilitar o botão "Iniciar Jogo"
    def verificar_escolhas(self):
        if self.tema and self.dificuldade:
            self.escolhas_feitas = True

            # Verifica se o botão de iniciar jogo existe e destrói-o se sim
            if hasattr(self, "btn_iniciar_jogo") and self.btn_iniciar_jogo.winfo_exists():
                self.btn_iniciar_jogo.destroy()

            # Cria um novo botão de iniciar jogo apenas se ambas as escolhas foram feitas
            if self.tema and self.dificuldade:
                self.btn_iniciar_jogo = tk.Button(self.frame_jogo, text="Iniciar Jogo", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF", command=self.iniciar_jogo)
                self.btn_iniciar_jogo.pack()

    # Método para escolher o tema
    def escolher_tema(self, num_tema):
        self.tema = num_tema
        nome_tema = self.tema_nome(self.tema)
        self.label_tema.config(text=f"{nome_tema}")
        self.tema_escolhido.set(nome_tema)
        self.verificar_escolhas()

    # Método para escolher a dificuldade
    def escolher_dificuldade(self, num_dificuldade):
        self.dificuldade = num_dificuldade
        numero_dificuldade = self.lista_dificuldades(self.dificuldade)
        self.label_dificuldade.config(text=f'{numero_dificuldade}')
        self.verificar_escolhas()

    # Método para carregar uma palavra secreta do arquivo de palavras
    def carregar_palavra_secreta(self):
        try:
            # Lista para armazenar as palavras do arquivo
            palavras = []
            # Abre o arquivo correspondente ao tema escolhido e lê as palavras
            with open(f"tema/{self.tema_nome(self.tema)}.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    palavras.append(linha)

            # Gera um número aleatório para escolher uma palavra do arquivo
            numero = random.randrange(0, len(palavras))
            palavra_secreta = palavras[numero].upper()
            # Atribui a palavra secreta e realiza a formatação sem acentos
            self.palavra_secreta = palavra_secreta
            self.palavra_secreta_sem_acentos = unidecode(palavra_secreta)
            # Inicializa a lista de letras acertadas com "_" para cada letra da palavra
            self.letras_acertadas = ["_" if letra.isalpha() else " " for letra in self.palavra_secreta_sem_acentos]
            # Chama o método para atualizar a interface
            self.atualizar_interface()

        except FileNotFoundError as e:
            # Exibe uma mensagem de erro caso o arquivo não seja encontrado
            messagebox.showerror("Erro", f"Erro ao carregar palavras: {e}")
            # Reinicializa a interface
            return self.inicializar_interface()
        except Exception as e:
            # Exibe uma mensagem de erro desconhecido
            messagebox.showerror("Erro", f"Erro desconhecido ao carregar palavras: {e}")

    # Método para iniciar o jogo
    def iniciar_jogo(self):
        # Verifica se as escolhas foram feitas antes de iniciar o jogo
        if self.escolhas_feitas:
            # Chama o método para configurar a interface do jogo
            self.menu_jogo()

    # Método para configurar a interface do jogo
    def menu_jogo(self):
        try:
            # Limpa variáveis relacionadas à partida anterior
            self.palavra_secreta = ""
            self.palavra_secreta_sem_acentos = ""
            self.letras_acertadas = []
            self.letras_usadas = []
            self.erros = 0

            # Destrói os widgets existentes no frame_jogo
            self.limpar_tela()

            # Verifica se tema e dificuldade foram escolhidos antes de iniciar o jogo
            if self.tema == 0 or self.dificuldade == 0:
                messagebox.showwarning("Atenção", "Escolha um tema e uma dificuldade antes de iniciar o jogo.")
                return

            # Adiciona widgets necessários para a nova partida
            self.label_mensagem= tk.Label(self.master, text="Não seja enforcado! Boa Sorte", font=("Comic Sans Ms", 36), bg="#09240B", fg="#FFFFFF").pack(pady=10)
            self.label_tema_escolhido = tk.Label(self.master, text="Tema escolhido:", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF")
            self.label_tema_escolhido.pack(pady=25)

            self.label_tema = tk.Label(self.master, textvariable=self.tema_escolhido, font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF")
            self.label_tema.pack(pady =25)

            # Atualiza os rótulos relevantes
            tk.Label(self.master, text="Letras usadas: ", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF").pack()

            self.label_letras_usadas = tk.Label(self.master, text=" ", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF")
            self.label_letras_usadas.pack()

            self.label_letras_acertadas = tk.Label(self.master, text="Palavra: ", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF")
            self.label_letras_acertadas.pack(pady= 25)

            tk.Button(self.master, text="Chutar letra", font=("Comic Sans Ms", 20), bg="#09240B", fg="#FFFFFF", command=self.pedir_chute).pack()

            self.canvas_forca = tk.Canvas(self.master, width=280, height=500, bg="#09240B", highlightthickness=0, bd=0)  # Define a área para desenhar a forca
            self.canvas_forca.place(x=0, y=85, anchor=tk.NW)

            # Chama a função para desenhar a forca inicial
            self.forca_desenho(self.erros, self.dificuldade)
            # Carrega uma nova palavra secreta
            self.carregar_palavra_secreta()

            # Atualiza a interface depois de carregar a nova palavra secreta
            self.atualizar_interface()

            # Verifica se o jogo chegou ao fim
            if not "_" in self.letras_acertadas or self.erros == self.chances:
                # Se sim, reinicia a interface após 1000 milissegundos (1 segundo)
                self.master.after(1000, self.inicializar_interface)
        except FileNotFoundError as e:
            # Se ocorrer um erro ao carregar palavras, exibe uma mensagem de erro
            messagebox.showerror("Erro", f"Erro ao carregar palavras: {e}")
            # Reinicia a interface
            self.inicializar_interface()

    # Função para limpar a tela
    def limpar_tela(self):
        # Verifica se o canvas_forca existe e o destroi
        if hasattr(self, "canvas_forca") and self.canvas_forca:
            self.canvas_forca.destroy()
        # Verifica se o frame_jogo existe e destrói widgets existentes nele
        if hasattr(self, "frame_jogo") and self.frame_jogo.winfo_exists():
            for widget in self.frame_jogo.winfo_children():
                widget.destroy()
            # Destroi o frame_jogo
            self.frame_jogo.destroy()

        # Verifica se o frame_tema existe e destrói widgets existentes nele
        if hasattr(self, "frame_tema") and self.frame_tema.winfo_exists():
            for widget in self.frame_tema.winfo_children():
                widget.destroy()
            # Destroi o frame_tema
            self.frame_tema.destroy()

        # Verifica se o frame_dificuldade existe e destrói widgets existentes nele
        if hasattr(self, "frame_dificuldade") and self.frame_dificuldade.winfo_exists():
            for widget in self.frame_dificuldade.winfo_children():
                widget.destroy()
            # Destroi o frame_dificuldade
            self.frame_dificuldade.destroy()

        # Destroi todos os widgets no mestre
        for widget in self.master.winfo_children():
            widget.destroy()

        # Cria novamente os frames para que possam ser usados posteriormente
        self.frame_tema = tk.Frame(self.master)
        self.frame_dificuldade = tk.Frame(self.master)
        self.frame_jogo = tk.Frame(self.master, bg="#09240B")

    # Função para desenhar a forca com base nos erros e na dificuldade
    def forca_desenho(self, erros,dificuldade):
        # Verifica se o canvas_forca existe
        if hasattr(self, "canvas_forca") and self.canvas_forca:
            # Limpa a forca anterior
            self.canvas_forca.delete("all")

            if dificuldade == 1:  # Fácil
                self.chances = 9
            elif dificuldade == 2:  # Médio
                self.chances = 7
            elif dificuldade == 3:  # Difícil
                self.chances = 5

            # Coordenadas iniciais
            x, y = 100, 50

            # Desenha a haste vertical e horizontal desde o início
            self.canvas_forca.create_line(x + 0, y, x + 0, y + 335, width=10, fill="White")  # Haste vertical
            self.canvas_forca.create_line(x, y + 5, x + 135, y + 5, width=10, fill="White")  # Haste horizontal
            self.canvas_forca.create_line(x, y + 40, x + 55, y + 5, width=10, fill="White")  # Haste diagonal
            self.canvas_forca.create_line(x - 50, y + 335, x + 70, y + 335, width=10, fill="White")  # base
            self.canvas_forca.create_line(x + 125, y, x + 125, y + 55, width=2, fill="White")  # Corda

        # Switch case para diferentes partes da forca de acordo com erros e dificuldade
        match (dificuldade):
            case 1:  # Dificuldade: Fácil
                self.chances=9
                if erros == 1:
                    self.cabeca()

                if erros == 2:
                    self.cabeca()
                    self.tronco()
                if erros == 3:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                if erros == 4:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()

                if erros == 5:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                    self.perna_esq()
                if erros == 6:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                    self.perna_esq()
                    self.perna_dir()
                if erros == 7:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                    self.perna_esq()
                    self.perna_dir()
                    self.olho_esq()
                if erros == 8:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                    self.perna_esq()
                    self.perna_dir()
                    self.olho_esq()
                    self.olho_dir()
                if erros == 9:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                    self.perna_esq()
                    self.perna_dir()
                    self.olho_esq()
                    self.olho_dir()

            case 2:  # Dificuldade: Médio
                self.chances=7
                if erros == 1:
                    self.cabeca()

                if erros == 2:
                    self.cabeca()
                    self.tronco()
                if erros == 3:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                if erros == 4:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()

                if erros == 5:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                    self.perna_esq()
                if erros == 6:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                    self.perna_esq()
                    self.perna_dir()
                if erros == 7:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                    self.perna_esq()
                    self.perna_dir()

            case 3:  # Dificuldade: Difícil
                self.chances=5
                if erros == 1:
                    self.cabeca()

                if erros == 2:
                    self.cabeca()
                    self.tronco()
                if erros == 3:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                if erros == 4:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                    self.perna_esq()
                    self.perna_dir()

                if erros == 5:
                    self.cabeca()
                    self.tronco()
                    self.braco_esq()
                    self.braco_dir()
                    self.perna_esq()
                    self.perna_dir()
                    self.olho_esq()
                    self.olho_dir()

    # Funções para desenhar diferentes partes da forca
    def cabeca(self):
        x, y = 100, 50
        raio_cabeca = 20
        self.canvas_forca.create_oval(x + 125 - raio_cabeca, y + 75 - raio_cabeca, x + 125 + raio_cabeca, y + 75 + raio_cabeca, outline="white", width=2)

    def tronco(self):
        x, y = 100, 50
        self.canvas_forca.create_line(x + 125, y + 95, x + 125, y + 175, width=2, fill="white")  # Desenha o corpo

    def braco_esq(self):
        x, y = 100, 50
        self.canvas_forca.create_line(x + 90, y + 135, x + 125, y + 95, width=2, fill="white")  # Desenha os braço esquerdo

    def braco_dir(self):
        x, y = 100, 50
        self.canvas_forca.create_line(x + 160, y + 135, x + 125, y + 95, width=2, fill="white")  # Desenha os braço direito

    def perna_esq(self):
        x, y = 100, 50
        self.canvas_forca.create_line(x + 125, y + 175, x + 95, y + 210, width=2, fill="white")  # Desenha perna esquerda

    def perna_dir(self):
        x, y = 100, 50
        self.canvas_forca.create_line(x + 125, y + 175, x + 160, y + 210, width=2, fill="white")  # Desenha perna direita

    def olho_esq(self):
        x, y = 100, 50
        # olho esquerdo
        self.canvas_forca.create_line(x + 113, y + 75, x + 123, y + 65, width=2, fill="white")
        self.canvas_forca.create_line(x + 113, y + 65, x + 123, y + 75, width=2, fill="white")

    def olho_dir(self):
        x, y = 100, 50
        # olho_direito
        self.canvas_forca.create_line(x + 129, y + 75, x + 139, y + 65, width=2, fill="white")  # Desenha os braço esquerdo
        self.canvas_forca.create_line(x + 129, y + 65, x + 139, y + 75, width=2, fill="white")  # Desenha os braço direito

    # Função para pedir uma letra ao usuário
    def pedir_chute(self):
        try:
            # Se a janela principal existe, pede uma letra ao usuário
            if self.master and getattr(self.master, 'winfo_exists', None)() == 1:
                chute = simpledialog.askstring("Chutar letra", "Digite uma letra:")

            # Se o usuário forneceu uma letra, converte para maiúsculas e processa o chute
            if chute:
                chute = chute.upper()

                # Verifica se a entrada é válida
                if len(chute) != 1 or not chute.isalpha():
                    messagebox.showwarning("Atenção", "Por favor, digite apenas letras.")
                    return

                # Verifica se a letra já foi usada
                if chute in self.letras_usadas:
                    messagebox.showwarning("Atenção", "Esta letra já foi escolhida. Tente outra.")
                    return

                # Processa o chute
                self.processar_chute(chute)

        except Exception as e:
            # Exibe uma mensagem de erro se ocorrer um problema ao pedir o chute
            messagebox.showerror("Erro", f"Erro ao pedir chute: {e}")

        # Função para processar o chute do usuário
    def processar_chute(self, chute):
        try:
            # Adiciona a letra à lista de letras usadas
            self.letras_usadas.append(chute)

            # Verifica se a letra está na palavra secreta
            if chute in self.palavra_secreta_sem_acentos:
                # Marca a letra correta na palavra
                self.marcar_chute_correto(chute)
            else:
                # Incrementa o número de erros
                self.erros += 1

            # Atualiza a interface
            self.atualizar_interface()

            # Desenha a forca de acordo com os erros
            self.forca_desenho(self.erros, self.dificuldade)

            # Verifica se o jogador ganhou
            if not "_" in self.letras_acertadas:
                messagebox.showinfo("Parabéns!", "Você ganhou!")
                self.iniciar_jogo()

            # Verifica se o jogador foi enforcado
            elif self.erros == self.chances:
                # Verifica se a janela principal ainda existe
                if self.master and getattr(self.master, 'winfo_exists', None)() == 1:
                    messagebox.showinfo("Fim de Jogo", f"Você foi enforcado! A palavra era {self.palavra_secreta}")
                    self.limpar_tela()
                    self.inicializar_interface()

        except Exception as e:
            # Verifica se a janela principal ainda existe
            if self.master and getattr(self.master, 'winfo_exists', None)() == 1:
                # Exibe uma mensagem de erro se ocorrer um problema ao processar o chute
                messagebox.showerror("Erro", f"Erro ao processar chute: {e}")


    # Função para marcar a letra correta na palavra
    def marcar_chute_correto(self, chute):
        for i, letra in enumerate(self.palavra_secreta_sem_acentos):
            if letra == chute:
                self.letras_acertadas[i] = self.palavra_secreta[i]

    # Atualiza a interface exibindo as letras acertadas e as letras usadas
    def atualizar_interface(self):
        letras_acertadas_str = " ".join(self.letras_acertadas)
        letras_usadas_str = " ".join(self.letras_usadas)

        # Configura os textos das labels para mostrar as letras acertadas e usadas
        self.label_letras_acertadas.config(text=f"Palavra: {letras_acertadas_str}")
        self.label_letras_usadas.config(text=f" {letras_usadas_str}")

    # Retorna o nome do tema com base no número do tema
    def tema_nome(self, num_tema):
        temas = {1: "animais", 2: "profissoes", 3: "paises"}
        

        return temas[num_tema]

    # Retorna o nome da dificuldade com base no número da dificuldade
    def lista_dificuldades(self, num_dificuldade):
        dificuldades = {1: "Fácil", 2: "Médio", 3: "Difícil"}
        return dificuldades[num_dificuldade]

    # Inicia o jogo da forca ao criar a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    jogo_da_forca_gui = JogoDaForcaGUI(root)
    root.mainloop()
