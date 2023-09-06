import random
from colorama import Fore, Style, init

# Inicialize o Colorama para adicionar cores à saída do console
init(autoreset=True)

# Lista de palavras para o jogo
palavras = []

# Lê as palavras do arquivo "lista_palavras.txt" com codificação UTF-8
with open("lista_palavras.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        palavras.append(linha.strip())

# Escolhe aleatoriamente uma palavra da lista
palavra = random.choice(palavras)

# Inicialize as variáveis
palavra_adivinhada = ["_"] * len(palavra)  # Lista de traços representando a palavra a ser adivinhada
tentativas = []  # Lista de letras que o jogador tentou
vidas = 6  # Número de vidas restantes

# Teclado virtual com todas as letras do alfabeto
teclado = list("abcdefghijklmnopqrstuvwxyz")

# Função para mostrar o estado atual do jogo
def mostrar_jogo():
    # Cria uma representação formatada da palavra a ser adivinhada
    palavra_formatada = ""
    for i, letra in enumerate(palavra):
        if palavra_adivinhada[i] == "_":
            palavra_formatada += "_"
        elif palavra_adivinhada[i] == letra:
            palavra_formatada += Fore.GREEN + letra + Style.RESET_ALL
        elif letra in palavra_adivinhada:
            palavra_formatada += Fore.YELLOW + letra + Style.RESET_ALL
        else:
            palavra_formatada += Fore.RED + letra + Style.RESET_ALL

    print("Palavra: " + palavra_formatada)  # Exibe a palavra a ser adivinhada
    print("Tentativas anteriores: " + ", ".join(tentativas))  # Exibe as letras já tentadas
    print("Vidas restantes: " + str(vidas))  # Exibe o número de vidas restantes

    # Cria uma representação formatada do teclado virtual
    teclado_formatado = ""
    for letra in teclado:
        if letra in palavra_adivinhada:
            teclado_formatado += Fore.GREEN + letra + Style.RESET_ALL
        elif letra in tentativas:
            teclado_formatado += Fore.YELLOW + letra + Style.RESET_ALL
        else:
            teclado_formatado += letra
    print("Teclado: " + " ".join(teclado_formatado))  # Exibe o teclado virtual

# Loop principal do jogo
while True:
    mostrar_jogo()  # Mostra o estado atual do jogo

    palavra_digitada = input("Digite uma palavra: ").lower()  # O jogador digita uma palavra (tentativa)

    if palavra_digitada == palavra:
        print("Parabéns! Você acertou a palavra: " + palavra)
        break
    elif palavra_digitada in tentativas:
        print(Fore.RED + "Você já tentou esta palavra. Tente novamente." + Style.RESET_ALL)
    else:
        tentativas.append(palavra_digitada)  # Adiciona a palavra digitada às tentativas
        vidas -= 1  # Decrementa o número de vidas

        if vidas == 0:
            print("Você perdeu! A palavra correta era: " + palavra)
            break

        # Atualiza as letras corretas na palavra adivinhada
        for i, letra in enumerate(palavra):
            if letra == palavra_digitada[i]:
                palavra_adivinhada[i] = letra

        # Remove as letras incorretas do teclado
        for letra in palavra_digitada:
            if letra in teclado:
                teclado.remove(letra)

    # Verifica se todas as letras da palavra foram adivinhadas
    if all(letra != "_" for letra in palavra_adivinhada):
        print("Parabéns! Você adivinhou a palavra: " + palavra)
        break

