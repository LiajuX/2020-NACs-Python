import math
import matplotlib.pyplot as plt

troncos = [180, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165]

def calculaXY(angulo1, angulo2):
    angulo1 = math.radians(angulo1)
    angulo2 = math.radians(angulo2)

    cosAngulo1 = math.cos(angulo1)
    sinAngulo1 = math.sin(angulo1)

    somaDeAngulos = angulo1 + angulo2

    xc = 8 * cosAngulo1
    yc = 8 * sinAngulo1
    xg = 8 * cosAngulo1 + 5 * math.cos(somaDeAngulos)
    yg = 8 * sinAngulo1 + 5 * math.sin(somaDeAngulos)

    return xc, yc, xg, yg

def printGrafico(x1, y1, x2, y2, titulo):
    plt.figure()

    plt.plot([0, x1], [0, y1], color='black')
    plt.plot([x1, x2], [y1, y2], color='black')

    plt.plot([0], [0], '-ro')
    plt.plot([x1], [y1], '-go')
    plt.plot([x2], [y2], '-bo')

    plt.axis((-10, 20, -10, 20))
    plt.suptitle(titulo, fontsize=22)
    plt.show()

X = int(input('Insira a quantidade de troncos (máximo de 12 troncos): '))
Y = float(input('Insira a distância entre a base e o local da retirada dos troncos em metros: '))
Z = float(input('Insira a velocidade do robô em m/s: '))
W = int(input('Insira a cada quantos segundos você quer que o robô envie print da posição do braço para a base: '))

deltaT = int(Y / Z)

pontosDeDescanso = calculaXY(90, 200)
printGrafico(pontosDeDescanso[0], pontosDeDescanso[1], pontosDeDescanso[2], pontosDeDescanso[3], 'Braço em Descanso')

# Deslocamento de ida
for i in range(deltaT):
    if i % W == 0:
        pontos = calculaXY(90, 270)
        printGrafico(pontos[0], pontos[1], pontos[2], pontos[3], 'Posição de Deslocamento - Ida')

for i in range(X):
    if troncos[i] != 180:
        pontos = calculaXY(troncos[i], 270)
        printGrafico(pontos[0], pontos[1], pontos[2], pontos[3], 'Garra Perpendicular ao Tronco ' + str(i+1))

        pontosDeitados = calculaXY(0, 360)
        printGrafico(pontosDeitados[0], pontosDeitados[1], pontosDeitados[2], pontosDeitados[3], 'Deitando o Tronco ' + str(i+1))

        printGrafico(pontosDeDescanso[0], pontosDeDescanso[1], pontosDeDescanso[2], pontosDeDescanso[3], 'Braço em Descanso - Tronco ' + str(i+1))
    else:
        print('Tronco 1 está deitado sobre o solo, os brigadistas conseguem passar!')

# Deslocamento de volta
for i in range(deltaT):
    if i % W == 0:
        pontos = calculaXY(90, 270)
        printGrafico(pontos[0], pontos[1], pontos[2], pontos[3], 'Posição de Deslocamento - Volta')

printGrafico(pontosDeDescanso[0], pontosDeDescanso[1], pontosDeDescanso[2], pontosDeDescanso[3], 'Braço em Descanso')
