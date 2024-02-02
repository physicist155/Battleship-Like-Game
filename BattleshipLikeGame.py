"""
Autor: Henrique de Almeida Cabral Teixeira
Contato: henriquetx13@gmail.com
Github: https://github.com/physicist155

"""


import random

def main():
    n = 1
    mat = le_arquivo_cria_matriz()
    nlin = len(mat)
    print()
    print("Olá! Posicione o seu barco em uma coluna para começar o jogo e divirta-se! (Cuidado com os tiros...)")
    print()
    pos_i = posicao_inicial_barco(mat)
    poslin = 1
    poscol = pos_i


    while n != 0:
        print('Jogada de número', n)
        print()
        barco = movimenta_barco(mat, poslin, poscol, 'saida.txt')
        trata_tres_tiros_alvos(mat, 'saida.txt')
        print("**************************************************************************************************************")
        print()
        poslin = barco[0]
        poscol = barco[1]
        n += 1

        if poslin == nlin - 2 and mat[poslin][poscol] != '+':
            print('Parabéns! Você ganhou! O barco chegou á última linha do mapa ser sem atingido!')
            print("**************************************************************************************************************")
            print("******************************** By: H.A.C. Teixeira - henriquetx13@gmail.com ********************************")


            n = 0
        elif mat[poslin][poscol] == '+':
            print('Você perdeu!')
            print("**************************************************************************************************************")
            print("******************************** By: H.A.C. Teixeira - henriquetx13@gmail.com ********************************")            
            n = 0
        else:
            continue


def le_arquivo_cria_matriz():
    # Lê a primeira linha do .txt e extrai o número de linhas e
    arquivo = "mapa.txt"
    arqEntra = open(arquivo, 'r')
    linha = arqEntra.readline()

    lista_strings = linha.split()

    nlin = int(lista_strings[0])
    ncol = int(lista_strings[1])


    # Monta modelo da matriz
    matriz = []
    for i in range(0, nlin + 2, 1):
        linha = []
        for j in range(0, ncol + 2, 1):
            linha.append("#")

        matriz.append(linha)

    # Adiciona os elementos do .txt a matriz
    for i in range(1, nlin + 1, 1):
        linha = arqEntra.readline()
        for j in range(1, ncol + 1, 1):
            matriz[i][j] = linha[j - 1]

    arqEntra.close()
    return matriz




def escreve_matriz_tela(mat):
    nlin = len(mat)
    ncol = len(mat[1])
    mat2 = []
    for i in range(0, nlin, 1):
        linha = []
        for j in range(0, ncol, 1):
            linha.append(mat[i][j])
        mat2.append(linha)

    for i in range(1, nlin - 1, 1):
        for j in range(1, ncol - 1, 1):
            if mat2[i][j] == 'X' or mat2[i][j] == 'Z' or mat2[i][j] == 'Y' or mat2[i][j] == 'S' or mat2[i][j] == '-':
                mat2[i][j] = "."
            else:
                continue
    for i in range(0, nlin, 1):
        for j in range(0, ncol, 1):
            if type(mat2[i][j]) == 'int':
                print("%6d" % (mat2[i][j]), end='')
            else:
                print("%6s" % (mat2[i][j]), end='')
        print()


def posicao_inicial_barco(mat):
    t = 0
    ncol = len(mat[1])
    while t == 0:
        posicao = int(input('Digite a coluna que deseja posicionar o barco: '))
        #Verifica se existe algum barco ou borda na posição escolhida
        if mat[1][posicao] != 'Y' and mat[1][posicao] != 'S' and mat[1][posicao] != 'X' and mat[1][
            posicao] != 'Z' and 0 < posicao < ncol - 1:
            mat[1][posicao] = 'B'
            t = 1
        else:
            print('Posição inválida')
            t = 0

    return posicao


def movimenta_barco(mat, blin, bcol, arqSaida):
    nlin = len(mat)
    ncol = len(mat[1])
    comando = input(
        'Digite "b" para movimento o barco para baixo; "d" para movimentar o barco para direita; "e" para movimentar o barco para esquerda: ')
    #Verifica se o movimento é válido e escreve no arquivo de saída se o movimento foi possível e qual a posição do barco após o movimento
    if comando == 'b':
        if mat[blin + 1][bcol] != 'Y' and mat[blin + 1][bcol] != 'S' and mat[blin + 1][bcol] != 'X' and mat[blin + 1][
            bcol] != 'Z':
            mat[blin + 1][bcol] = 'B'
            mat[blin][bcol] = '-'

            escreve_matriz_tela(mat)
            return blin + 1, bcol
        else:
            print('Movimento Inválido')
            return blin, bcol

    elif comando == 'd':
        if mat[blin][bcol + 1] != 'Y' and mat[blin][bcol + 1] != 'S' and mat[blin][bcol + 1] != 'X' and mat[blin][
            bcol + 1] != 'Z' and bcol < ncol:
            mat[blin][bcol + 1] = 'B'
            mat[blin][bcol] = '-'

            escreve_matriz_tela(mat)
            return blin, bcol + 1
        else:
            print('Movimento Inválido')
            return blin, bcol

    elif comando == 'e':
        if mat[blin][bcol - 1] != 'Y' and mat[blin][bcol - 1] != 'S' and mat[blin][bcol - 1] != 'X' and mat[blin][
            bcol - 1] != 'Z' and bcol > 1:
            mat[blin][bcol - 1] = 'B'
            mat[blin][bcol] = '-'

            escreve_matriz_tela(mat)

            return blin, bcol - 1

        else:
            print()
            print('Movimento Inválido')
            print()
            print()



            return blin, bcol


    else:
        print('Comando Inválido')

        return blin, bcol


def trata_tres_tiros_alvos(mat, arqSaida):
    nlin = len(mat)
    ncol = len(mat[1])


    for i in range(0, 3, 1):
        arq = open(arqSaida, 'w')
        #Utiliza a função randit para a posição aleatoria de cada tiro
        tiro_lin = random.randint(1, nlin - 1)
        tiro_col = random.randint(1, ncol - 1)

        if mat[tiro_lin][tiro_col] == 'B':
            #Caso o alvo antigido for B
            mat[tiro_lin][tiro_col] = '+'
            print('O alvo atingido foi B na posição(', tiro_lin, tiro_col, ')')


            escreve_matriz_tela(mat)



        elif mat[tiro_lin][tiro_col] == 'Z':
            # Caso o alvo antigido for Z
            mat[tiro_lin][tiro_col] = '*'
            print('O alvo Z foi atingido na posição(', tiro_lin, tiro_col, ')')


            escreve_matriz_tela(mat)


        elif mat[tiro_lin][tiro_col] == 'X':
            # Caso o alvo antigido for X
            if mat[tiro_lin + 1][tiro_col] == 'X':
                mat[tiro_lin + 1][tiro_col] = '*'
                mat[tiro_lin][tiro_col] = '*'
                print('O alvo X foi atingido na posição(', tiro_lin, tiro_col, ')')

                
                escreve_matriz_tela(mat)
            elif mat[tiro_lin - 1][tiro_col] == 'X':
                mat[tiro_lin - 1][tiro_col] = '*'
                mat[tiro_lin][tiro_col] = '*'
                print('O alvo X foi atingido na posição(', tiro_lin, tiro_col, ')')

                
                escreve_matriz_tela(mat)
            elif mat[tiro_lin][tiro_col + 1] == 'X':
                mat[tiro_lin][tiro_col + 1] = '*'
                mat[tiro_lin][tiro_col] = '*'
                print('O alvo X foi atingido na posição(', tiro_lin, tiro_col, ')')

                
                escreve_matriz_tela(mat)
            elif mat[tiro_lin][tiro_col - 1] == 'X':
                mat[tiro_lin][tiro_col - 1] = '*'
                mat[tiro_lin][tiro_col] = '*'
                print('O alvo X foi atingido na posição(', tiro_lin, tiro_col, ')')

                escreve_matriz_tela(mat)


        elif mat[tiro_lin][tiro_col] == 'S':
            # Caso o alvo antigido for S
            print('O alvo S foi atingido na posição(', tiro_lin, tiro_col, ')')

            arq.close()
            if mat[tiro_lin + 1][tiro_col] == 'S' or mat[tiro_lin - 1][tiro_col] == 'S':
                j = 1
                i = 0
                while i < 5 and j < 5:
                    if mat[tiro_lin + i][tiro_col] == 'S':
                        mat[tiro_lin + i][tiro_col] = '*'
                        i += 1
                    elif mat[tiro_lin - j][tiro_col] == 'S':
                        mat[tiro_lin - j][tiro_col] = '*'
                        j += 1
                    else:
                        break
                escreve_matriz_tela(mat)



            elif mat[tiro_lin][tiro_col + 1] == 'S' or mat[tiro_lin][tiro_col - 1] == 'S':
                j = 1
                i = 0
                while i < 5 and j < 5:
                    if mat[tiro_lin][tiro_col + i] == 'S':
                        mat[tiro_lin][tiro_col + i] = '*'
                        i += 1
                    elif mat[tiro_lin][tiro_col - j] == 'S':
                        mat[tiro_lin][tiro_col - j] = '*'
                        j += 1
                    else:
                        break
                escreve_matriz_tela(mat)

        elif mat[tiro_lin][tiro_col] == 'Y':
            # Caso o alvo antigido for Y
            if mat[tiro_lin + 1][tiro_col] == 'Y' and mat[tiro_lin][tiro_col + 1] == 'Y':
                mat[tiro_lin][tiro_col] = '*'
                mat[tiro_lin + 1][tiro_col] = '*'
                mat[tiro_lin][tiro_col + 1] = '*'
                mat[tiro_lin + 1][tiro_col + 1] = '*'


                escreve_matriz_tela(mat)
            elif mat[tiro_lin + 1][tiro_col] == 'Y' and mat[tiro_lin][tiro_col - 1] == 'Y':
                mat[tiro_lin][tiro_col] = '*'
                mat[tiro_lin + 1][tiro_col] = '*'
                mat[tiro_lin][tiro_col - 1] = '*'
                mat[tiro_lin + 1][tiro_col - 1] = '*'
                print('O alvo Y foi atingido na posição(', tiro_lin, tiro_col, ')')


                escreve_matriz_tela(mat)
            elif mat[tiro_lin - 1][tiro_col] == 'Y' and mat[tiro_lin][tiro_col + 1] == 'Y':
                mat[tiro_lin][tiro_col] = '*'
                mat[tiro_lin - 1][tiro_col] = '*'
                mat[tiro_lin][tiro_col + 1] = '*'
                mat[tiro_lin - 1][tiro_col + 1] = '*'
                print('O alvo Y foi atingido na posição(', tiro_lin, tiro_col, ')')


                escreve_matriz_tela(mat)
            elif mat[tiro_lin - 1][tiro_col] == 'Y' and mat[tiro_lin][tiro_col - 1] == 'Y':
                mat[tiro_lin][tiro_col] = '*'
                mat[tiro_lin - 1][tiro_col] = '*'
                mat[tiro_lin][tiro_col - 1] = '*'
                mat[tiro_lin - 1][tiro_col - 1] = '*'
                print('O alvo Y foi atingido na posição(', tiro_lin, tiro_col, ')')


                escreve_matriz_tela(mat)

        else:
            # Caso o alvo antigido for a Água
            print('Nenhum alvo foi atingido pelo tiro na posição(', tiro_lin, tiro_col, ')')

            escreve_matriz_tela(mat)

        print()




main()
