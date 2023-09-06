# Jogo da Velha 4x4 em Python
# - O jogo é jogado em um tabuleiro 4x4.
# - Dois jogadores, X e O, alternam suas jogadas.
# - Cada jogador deve inserir suas jogadas no formato 'linha coluna' (por exemplo, '2 3' para a segunda linha e terceira coluna).

# Função para imprimir o jogo
def imprimir_jogo(jogo):
    for linha in jogo:
        print(" | ".join(linha))
        print("-" * 23)

# Função para verificar se um jogador venceu
def verificar_vitoria(jogo, jogador):
    # Verificar linhas e colunas
    for i in range(4):
        if all(jogo[i][j] == jogador for j in range(4)) or all(jogo[j][i] == jogador for j in range(4)):
            return True

    # Verificar diagonais
    if all(jogo[i][i] == jogador for i in range(4)) or all(jogo[i][3 - i] == jogador for i in range(4)):
        return True

    return False

# Função principal do jogo
def jogo_da_velha():
    jogo = [[" " for _ in range(4)] for _ in range(4)]
    jogador_atual = "X"

#contador de jogadas
    jogadas_restantes = 16

    while True:
        imprimir_jogo(jogo)
        print(f"Vez do jogador {jogador_atual}")
# define a linha e a coluna digitadas pelo jogador
        try:
            linha, coluna = map(int, input("Digite sua jogada (linha coluna): ").split())
# verifica se a resposta esta correta,caso a pessoa tenha colocado na mesma posiçao que outro participante,sera repitido o progama.
            if jogo[linha - 1][coluna - 1] != " ":
                print("Essa posição já está ocupada. Tente novamente.")
                continue
# vai diminuindo as opcoes
            jogo[linha - 1][coluna - 1] = jogador_atual
#contador diminuindo
            jogadas_restantes -= 1

#imprime se o 0 ou x ganhou,imprime o nome do vencedor com a tabela
            if verificar_vitoria(jogo, jogador_atual):
                imprimir_jogo(jogo)
                print(f"Jogador {jogador_atual} venceu! Parabéns!")
                break

# if imprime se caso nenhum dos dois conseguirem formar uma linha com quatro
            if jogadas_restantes == 0:
                imprimir_jogo(jogo)
                print("O jogo terminou em empate!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"

# verifica se a resposta esta correta, caso nao esteja ele reinicia a jogada ate competidor acertar a resposta exemplo: 1 3
        except (ValueError, IndexError):
            print("Jogada inválida. Por favor, digite uma jogada válida.")
# executor de bloco de codigo quando o script esta diretamente em um usuario
if __name__ == "__main__":
    jogo_da_velha()
