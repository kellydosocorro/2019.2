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

def reflexao(p1,p2):

    result = []
    trocaXY, trocaX, trocaY = False, False, False

    x1,y1 = ponto(p1)
    x2,y2 = ponto(p2)

    m = calculo_m(x1,x2,y1,y2)
    result.append(m)

    if m >1 or m < -1:
        x1,y1 = y1,x1
        x2, y2 = y2, x2
        trocaXY = True
        #result.append(trocaXY)
        result.append(x1)
        result.append(y1)
        result.append(x2)
        result.append(y2)

    if x1 > x2:
        x1 = -x1
        x2 = -x2
        trocaX = True
        #result.append(trocaX)
        result.append(x1)
        result.append(x2)

    if y1 > y2:
        y1 = -y1
        y2 = -y2
        trocaY = True
        #result.append(trocaY)
        result.append(y1)
        result.append(y2)
		
    #return result
    return result
	
def main():
		
    ponto1 = input("Digite os valores para o ponto 1 (x,y): ")
    ponto2 = input("Digite os valores para o ponto 2 (x,y): ")

    resultado = reflexao(ponto1, ponto2)
	
    x1,y1 = resultado[1], resultado[2]
    x2,y2 = resultado[3], resultado[4]

    e = 0
    m = resultado[0]

    while x1 < x2:
        if e>=0:
            y1 = y1+1
            e=e-1
        x1 = x1+1
        e = e+m
		
        print("e = {}".format(e))
        print("m = {}".format(m))
        print("Ponto ({},{})".format(x1,y1))

main()


