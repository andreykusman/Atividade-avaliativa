def criar_jogo(dimensao):
    # Cria um tabuleiro vazio com a dimensão especificada
    jogo = [[' ' for _ in range(dimensao)] for _ in range(dimensao)]
    return jogo

def imprimir_jogo(jogo):
    dimensao = len(jogo)
    for i in range(dimensao):
        for j in range(dimensao):
            # Imprime o valor atual da célula no tabuleiro
            print(jogo[i][j], end='')

            # Adiciona um caractere de barra vertical "|" entre as células
            if j < dimensao - 1:
                print('|', end='')
        print()  # Move para a próxima linha

        # Adiciona uma linha horizontal "-" entre as linhas do tabuleiro, exceto a última linha
        if i < dimensao - 1:
            print('-' * (dimensao * 2 - 1))

def jogada_valida(jogo, linha, coluna):
    dimensao = len(jogo)
    # Verifica se a jogada é válida, ou seja, a célula está vazia e as coordenadas estão dentro dos limites do tabuleiro
    return 0 <= linha < dimensao and 0 <= coluna < dimensao and jogo[linha][coluna] == ' '

def fazer_jogada(jogo, jogador, linha, coluna):
    if jogada_valida(jogo, linha, coluna):
        # Registra a jogada do jogador no tabuleiro
        jogo[linha][coluna] = jogador
        return True  # Retorna True se a jogada foi bem-sucedida
    return False  # Retorna False se a jogada não for válida

def verificar_vitoria(jogo, jogador):
    dimensao = len(jogo)

    # Verifica se o jogador venceu nas linhas e colunas do tabuleiro
    for i in range(dimensao):
        if all(jogo[i][j] == jogador for j in range(dimensao)) or all(jogo[j][i] == jogador for j in range(dimensao)):
            return True

    # Verifica se o jogador venceu nas diagonais do tabuleiro
    if all(jogo[i][i] == jogador for i in range(dimensao)) or all(jogo[i][dimensao - i - 1] == jogador for i in range(dimensao)):
        return True

    return False  # Retorna False se o jogador não venceu

def jogo_da_velha(dimensao):
    jogo = criar_jogo(dimensao)
    jogador_da_rodada_atual = 'X'
    jogada_rest = dimensao * dimensao  # Número total de jogadas possíveis

    while jogada_rest > 0:
        imprimir_jogo(jogo)
        print(f'Vez do jogador {jogador_da_rodada_atual}')
        linha = int(input(f'Digite a linha da sua jogada (0 a {dimensao - 1}): '))
        coluna = int(input(f'Digite a coluna da sua jogada (0 a {dimensao - 1}): '))

        if fazer_jogada(jogo, jogador_da_rodada_atual, linha, coluna):
            if verificar_vitoria(jogo, jogador_da_rodada_atual):
                imprimir_jogo(jogo)
                print(f'O jogador {jogador_da_rodada_atual} venceu!')
                break
            jogador_da_rodada_atual = 'O' if jogador_da_rodada_atual == 'X' else 'X'
            jogada_rest -= 1
        else:
            print('Jogada inválida. Tente novamente.')

    if jogada_rest == 0:
        imprimir_jogo(jogo)
        print('O jogo empatou!')

if __name__ == "__main__":
    dimensao = int(input('Digite a dimensão do tabuleiro (quadrado): '))
    jogo_da_velha(dimensao)

