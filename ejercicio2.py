matriz = []

def matr(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz

def llenar_matriz(n):
    matriz =  matr(n)
    for i in range(n):
        for j in range (n):
            matriz[i][j] = float(input("valor de [",str(i),"][",str(j),"] ="))
    return matriz
def orednar(n):
    mx = llenar_matriz(n)
    for x in range(n):
        for y in range(n):
            if mx[x][x]==0:
                mx[x+1][x]=matriz[x][x]
def gauss(n):
    for z in range(n-1):
        for x in range(n-z):
            if (matriz[z][z]!=0):
                p=matriz[x+z][z]/matriz[z][z]
                for y in range(n):
                    matriz[x+z][y]= matriz[x+z][y]-matriz[x+z][y]*p
def det(n):
    det =1
    for i in range(n):
        det=matriz[i][i]*det
    print("\n El determinante de la matriz es = ", det)

def matrix_recurrencia(M, n):

