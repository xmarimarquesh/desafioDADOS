

def mostrarMatriz(m):
    print("MATRIZ:")
    for i in range(8):
        for j in range(8):
            print(m[i][j], end="   ")
        print("\n")

def mostrarDirecoes(d):
    for chave, valor in d.items():
        print(f"{chave}: {valor}")

def setarDirecaoDados(direcao):
    for i in range(6):
        if(direcao[i] != 8):
            direcao[i] = direcao[i] + 1
        else: 
            direcao[i] = 0

    return direcao

def mudarPosicao(matriz, direcao_dado, posicao, direcoes, x, y):
    
    x += posicao * direcoes[direcao_dado[posicao - 1]][0]
    y += posicao * direcoes[direcao_dado[posicao - 1]][1]

    if x > 7 or x < 0 or y > 7 or y < 0:
        return -1
    return (matriz[y][x], x, y)

def main():
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
    
    direcao_dado = [0, 0, 0, 0, 0, 0]
    
    # (COLUNA, LINHA)  -  (X, Y)
    #           cima    baixo   esquerdo  direito diagDB   diagBE    diagDC  diagEC   
    direcoes = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, -1), (-1, -1), (1, 1), (-1, 1)]

    #mostrarDirecoes(direcoes)
    #mostrarDirecoes(direcao_dado)

    print("----------INICIO----------\n")

    x = 0
    y = 7
    posicao = matriz[y][x]

    # print(f"Posicao inicial: {posicao}\n")	

    # direcao_dado = setarDirecaoDados(direcao_dado)

    count = 0
    while True:
        print(f"pos({y},{x})")
        print(f"matriz: {matriz[y][x]}")

        result = mudarPosicao(matriz, direcao_dado, posicao, direcoes, x, y)

        if result == -1:
            print("Quebrou")
            break
        
        posicao = result[0]
        x = result[1]
        y = result[2]

        count += 1
        if(count >= 64):
            break



    mostrarMatriz(matriz)


main()