from itertools import permutations

def mostrarMatriz(m):
    print("MATRIZ:")
    for i in range(8):
        for j in range(8):
            print(m[i][j], end="   ")
        print("\n")

def setarDirecaoDados(direcao):
    combinacao = list(permutations(direcao, 6))
    return combinacao

def mudarPosicao(matriz, direcao_dado, posicao, direcoes, coluna, linha, movimentos, dm):

    movimento_atual = direcoes[direcao_dado[posicao - 1]]
    coluna += posicao * movimento_atual[0]
    linha += posicao * movimento_atual[1]
    
    movimentos.append(dm[direcao_dado[posicao - 1]])

    # Verifica se nova posição está fora da matriz
    if (coluna > 7 or coluna < 0) or (linha > 7 or linha < 0):
        return (-1, -1, -1, -1)

    return (matriz[linha][coluna], linha, coluna, movimentos)

def main():
    coluna = 0
    linha = 0
    matriz = [
            [6, 3, 1, 1, 2, 2, 3, 1],
            [6, 4, 6, 3, 4, 2, 4, 1],
            [3, 2, 4, 2, 4, 5, 2, 3],
            [2, 4, 4, 4, 2, 1, 2, 3],
            [1, 2, 3, 4, 2, 2, 2, 5],
            [5, 5, 4, 4, 5, 1, 5, 5],
            [3, 3, 4, 4, 3, 4, 2, 2],
            [1, 2, 3, 6, 2, 4, 1, 2]
            ]
    
    # Direções como (coluna, linha) e nomes das direções
    direcoes = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    direcao_nome = ["cima", "baixo", "esquerdo", "direito", "diagDB", "diagBE", "diagDC", "diagEC"]
    possiveis_direcoes = [0,1,2,3,4,5,6,7]

    print("----------INICIO----------\n")
    coluna = 0
    linha = 7
    posicao = matriz[linha][coluna]

    todas_direcoes = setarDirecaoDados(possiveis_direcoes)
    print("Possibilidades: ", len(todas_direcoes))

    for direcao_dado in todas_direcoes:
        count = 0
        posicao = matriz[linha][coluna]
        movimentos = []

        while True:
            (posicao, linha, coluna, movimentos) = mudarPosicao(matriz, direcao_dado, posicao, direcoes, coluna, linha, movimentos, direcao_nome)
            
            if posicao == -1:
                break

            count += 1
            if count >= 64:
                break

            if linha == 0 and coluna == 7 and posicao == 1:
                print("CHEGOU!")
                print("Movimentos realizados:", movimentos)
                print("Direcao_dados:", direcao_dado)
                break

    mostrarMatriz(matriz)
    print("\nFim da combinação\n")

main()
