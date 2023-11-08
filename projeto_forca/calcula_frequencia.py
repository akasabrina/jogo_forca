from unidecode import unidecode

letra = "a"
letra2 = "b"
tema = "animais"
palavras = []
palavras_letra = []
palavras_letra2 = []

#abre o arquivo .txt do tema escolhido e conta o total de palavras
with open(f"tema/{tema}.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavras.append(unidecode(linha.strip()))
total_palavras = len(palavras)
print(f"Total de palavras do tema {tema}: {total_palavras}")

# Verifica palavra por palavra se a letra está presente
for palavra in palavras:
    if letra in palavra:
        palavras_letra.append(palavra)
        if letra2 in palavra:
            palavras_letra2.append(palavra)

# contagem e frequência relativa de uma letra
total_palavras_letra = len(palavras_letra)
percent_relat = (total_palavras_letra/total_palavras)*100
print(f"Número de palavras com as letras '{letra}': {total_palavras_letra}")
print(f"Frequência relativa {percent_relat:.2f}%")

# contagem e frequência relativa de duas letras
total_palavras_letra2 = len(palavras_letra2)
percent_relat2 = (total_palavras_letra2/total_palavras)*100
print(f"Número de palavras com as letras '{letra}' e '{letra2}': {total_palavras_letra2}")
print(f"Frequência relativa {percent_relat2:.2f}%")