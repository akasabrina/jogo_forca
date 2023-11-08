def desenha_forca(num, erros):
    # Imprime as partes fixas da forca
    print("  _______     ")
    print(" |/      |    ")

    match num:
        case 1: # Dificuldade: Fácil
            # Condições para desenhar diferentes partes da forca de acordo com o número de erros e da dificuldade
            if (erros == 1):
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")

            if (erros == 2):
                print(" |      (_)   ")
                print(" |       |    ")
                print(" |            ")
                print(" |            ")

            if (erros == 3):
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")

            if (erros == 4):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")

            if (erros == 5):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if (erros == 6):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")

            if (erros == 7):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

            if (erros == 8):
                print(" |     (X_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

            if (erros == 9):
                print(" |     (X_X)  ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

        case 2: # Dificuldade: Médio
            # Condições para desenhar diferentes partes da forca de acordo com o número de erros e da dificuldade
            if (erros == 1):
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")

            if (erros == 2):
                print(" |      (_)   ")
                print(" |       |    ")
                print(" |            ")
                print(" |            ")
            
            if (erros == 3):
                print(" |      (_)   ")
                print(" |       |    ")
                print(" |       |    ")
                print(" |            ")

            if (erros == 4):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if (erros == 5):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")
            
            if (erros == 6):
                print(" |     (X_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")
            
            if (erros == 7):
                print(" |     (X_X)  ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

        case 3: # Dificuldade: Difícil
            # Condições para desenhar diferentes partes da forca de acordo com o número de erros e da dificuldade
            if (erros == 1):
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
            
            if (erros == 2):
                print(" |      (_)   ")
                print(" |       |    ")
                print(" |       |    ")
                print(" |            ")

            if (erros == 3):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if (erros == 4):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")
            
            if (erros == 5):
                print(" |     (X_X)  ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

    # Parte inferior da forca e uma linha em branco
    print(" |            ")
    print("_|___         ")
    print()