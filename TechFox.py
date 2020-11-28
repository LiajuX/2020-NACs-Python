import math
import matplotlib.pyplot as plt

for i in range(3):
    L1 = float(input('Insira o valor de L1 do braço ' + str(i+1) + ': '))
    L2 = float(input('Insira o valor de L2 do braço ' + str(i+1) + ': '))

    for j in range(3):
        angulo1 = math.radians(int(input('Insira o valor em graus do ângulo θ1 na posição ' + str(j + 1) + ': ')))
        cosAngulo1 = math.cos(angulo1)
        sinAngulo1 = math.sin(angulo1)

        angulo2 = math.radians(int(input('Insira o valor em graus do ângulo θ2 na posição ' + str(j + 1) + ': ')))
        cosAngulo2 = math.cos(angulo2)
        sinAngulo2 = math.sin(angulo2)

        somaDeAngulos = angulo1 + angulo2

        xc = L1 * cosAngulo1
        yc = L1 * sinAngulo1
        xg = L1 * cosAngulo1 + L2 * math.cos(somaDeAngulos)
        yg = L1 * sinAngulo1 + L2 * math.sin(somaDeAngulos)

        plt.figure()

        plt.plot([0, xc], [0, yc], color='black')

        plt.plot([xc, xg], [yc, yg], color='black')

        plt.plot([0], [0], '-ro')
        plt.plot([xc], [yc], '-go')
        plt.plot([xg], [yg], '-bo')

        plt.axis((-10, 20, -10, 20))
        plt.suptitle('Braço ' + str(i + 1) + ' - Posição ' + str(j + 1), fontsize=22)
        plt.show()
