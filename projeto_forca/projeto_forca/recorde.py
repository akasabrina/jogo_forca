# Função que calcula os pontos com base no número de erros do jogador
def calcular_pontos(erros):
    if erros == 0:
        pontos = 700
    elif erros == 1:
        pontos = 600
    elif erros == 2:
        pontos = 500
    elif erros == 3:
        pontos = 400
    elif erros == 4:
        pontos = 300
    elif erros == 5:
        pontos = 200
    elif erros == 6:
        pontos = 100
    else:
        pontos = 0
    return pontos  # Retorna a pontuação com base nos erros

# Função que soma os pontos obtidos nesta rodada à pontuação total do jogador
def somar_pontos(pontuacao_atual, pontos):
    pontuacao_atual += pontos  # Soma os pontos à pontuação total atual do jogador
    return pontuacao_atual  # Retorna a pontuação atualizada do jogado