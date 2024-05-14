# Definição das palavras e suas posições na grade
palavras = {
    "PALETA": {"pos": (0, 0), "direcao": "H"},        # Horizontal, posição (0,0)
    "RIOLOGIA": {"pos": (2, 0), "direcao": "H"},      # Horizontal, posição (2,0)
    "METRO": {"pos": (6, 1), "direcao": "H"},         # Horizontal, posição (6,1)
    "SGUA": {"pos": (8, 0), "direcao": "H"},          # Horizontal, posição (8,0)
    "ESQUELETO": {"pos": (10, 0), "direcao": "H"},    # Horizontal, posição (10,0)
    "CULINARIA": {"pos": (12, 0), "direcao": "H"},    # Horizontal, posição (12,0)
    "TEMPESTADE": {"pos": (14, 0), "direcao": "H"},   # Horizontal, posição (14,0)
    "PORTUGUES": {"pos": (0, 0), "direcao": "V"},     # Vertical, posição (0,0)
    "AGOSTO": {"pos": (1, 5), "direcao": "V"},         # Vertical, posição (1,5)
    "ESLAID": {"pos": (0, 3), "direcao": "V"},     # Vertical, posição (0,3)
    "DENTISTA": {"pos": (0, 8), "direcao": "V"},      # Vertical, posição (0,8)
    "SOL": {"pos": (1, 6), "direcao": "V"},           # Vertical, posição (1,6)
    "CORACAO": {"pos": (0, 9), "direcao": "V"},       # Vertical, posição (0,9)
    "PIZZA": {"pos": (0, 10), "direcao": "V"},        # Vertical, posição (0,10)
}


# Tamanho da grade
tamanho = 15


# Inicializando a grade com espaços em branco
grade = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]


# Função para preencher a grade com uma palavra
def preencher_palavra(palavra, info, grade):
    x, y = info["pos"]
    if info["direcao"] == "H":
        for i, letra in enumerate(palavra):
            grade[x][y + i] = letra
    elif info["direcao"] == "V":
        for i, letra in enumerate(palavra):
            grade[x + i][y] = letra


# Função para exibir a grade no console
def exibir_grade(grade):
    for linha in grade:
        print(' '.join(linha))


# Função para verificar respostas do usuário
def verificar_resposta(palavra, resposta):
    return palavra == resposta.upper()


# Pistas horizontais e verticais
pistas_horizontais = {
    1: "Instrumento usado por artistas para misturar tintas.",
    4: "Ciência que estuda os rios.",
    7: "Unidade de medida de comprimento no sistema métrico.",
    8: "Estado líquido que compõe a maior parte do nosso planeta, no lugar do primeiro A, coloque S",
    10: "Estrutura óssea que sustenta o corpo humano.",
    12: "Arte de preparar pratos saborosos.",
    13: "Fenômeno meteorológico que provoca descargas elétricas.",
}


pistas_verticais = {
    1: "Língua falada no Brasil.",
    2: "Período do ano com temperaturas elevadas.",
    3: "Slide em baianês.",
    5: "Profissional que cuida da saúde bucal.",
    6: "Estrela do nosso sistema solar.",
    9: "Órgão do corpo responsável pela circulação sanguínea.",
    11: "Comida feita de massa e recheio, comum na Itália.",
}


# Função para perguntar as respostas aos usuários
def perguntar_respostas(pistas_horizontais, pistas_verticais, palavras, grade):
    print("\nHorizontais:")
    for num, pista in pistas_horizontais.items():
        while True:
            resposta = input(f"{num}. {pista} ")
            palavra = list(palavras.keys())[list(pistas_horizontais.keys()).index(num)]
            if verificar_resposta(palavra, resposta):
                preencher_palavra(palavra, palavras[palavra], grade)
                exibir_grade(grade)
                print("Correto!")
                break
            else:
                print("Incorreto. Tente novamente.")


    print("\nVerticais:")
    for num, pista in pistas_verticais.items():
        while True:
            resposta = input(f"{num}. {pista} ")
            palavra = list(palavras.keys())[list(pistas_verticais.keys()).index(num) + len(pistas_horizontais)]
            if verificar_resposta(palavra, resposta):
                preencher_palavra(palavra, palavras[palavra], grade)
                exibir_grade(grade)
                print("Correto!")
                break
            else:
                print("Incorreto. Tente novamente.")


# Inicialmente exibir a grade vazia
print("Grade de Palavras Cruzadas:")
exibir_grade(grade)


# Perguntar as respostas aos usuários
perguntar_respostas(pistas_horizontais, pistas_verticais, palavras, grade)
