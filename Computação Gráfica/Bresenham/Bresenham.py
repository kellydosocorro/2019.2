# Bresenham 

def calculo_m(x1,x2,y1,y2):
    deltaY = y2-y1
    deltaX = x2-x1

    if deltaX > 0:   
        return deltaY/deltaX
    else:
        return deltaY

def ponto(ponto):
    x,y = [int(p) for p in ponto.split(',')]
    return x,y

def reflection(m,p1,p2):

    troca = []

    x1,y1 = ponto(p1)
    x2,y2 = ponto(p2)
    
    if m>1 or m< -1:
        x1,y1 = y1,x1
        x2,y2 = y2,x2
        troca.append(True)
    else:
        troca.append(False)

    if x1 > x2:
        x1 = -x1
        x2 = -x2
        troca.append(True)
    else:
        troca.append(False)

    if y1 > y2:
        y1 = -y1
        y2 = -y2
        troca.append(True)
    else:
        troca.append(False)
        
    return [[x1,y1],[x2,y2], troca]

def negativa(lista):
    for i in range(len(lista)):
        lista[i] = -lista[i]
    return lista

def Bresenham(p1,p2):

    x1,y1 = ponto(p1)
    x2,y2 = ponto(p2)

    m = 0
    e = 0

    m = calculo_m(x1,x2,y1,y2)
    
    resultado = reflection(m,p1,p2)

    X1,Y1 = resultado[0]
    X2,Y2 = resultado[1]

    m = calculo_m(X1,X2,Y1,Y2)
    e = m - 0.5

    pontosX = []
    pontosY = []

    pontosX.append(X1)
    pontosY.append(Y1)

    while(X1 < X2):
        if (e >= 0):
            Y1 = Y1+ 1
            e = e - 1  
        X1 = X1+1
        e = m + e
        pontosX.append(X1)
        pontosY.append(Y1)

    # Inverte a ordem
    if resultado[2][0] == True:
        pontosX, pontosY = pontosY, pontosX
    if resultado[2][1] == True:
        pontosX = [-p for p in pontosX]
    if resultado[2][2] == True:
        pontosY = [-p for p in pontosY]
    
    print(pontosX)
    print(pontosY)


# Escopo principal

def main():

    ponto1 = input("Digite os valores para o ponto 1 (x,y): ")
    ponto2 = input("Digite os valores para o ponto 2 (x,y): ")

    Bresenham(ponto1,ponto2)

main()

    

