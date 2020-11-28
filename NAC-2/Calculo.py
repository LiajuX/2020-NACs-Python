def calculaGeometrica(x,y,z):
    r = (x * y * z)**(1 / 3)
    return r

def calculaPonderada(x,y,z):
    r = (x + 2 * y + 3 * z) / 6
    return r

def calculaHarmonica(x,y,z):
    r = 1 / (1/x + 1/y + 1/z)
    return r

def calculaAritmetica(x,y,z):
    r = (x + y + z) / 3
    return r

while True:
    Menu = input('Escolha o cálculo de média conforme o menu: \na para Geométrica \nb para Ponderada \nc para Harmônica \nd para Aritmética \n')

    x = int(input('Insira um valor inteiro e positivo para x: '))
    y = int(input('Insira um valor inteiro e positivo para y: '))
    z = int(input('Insira um valor inteiro e positivo para z: '))

    if Menu == 'a':
        r = calculaGeometrica(x,y,z)
        print('Resultado =', r)
    elif Menu == 'b':
        r = calculaPonderada(x,y,z)
        print('Resultado =', r)
    elif Menu == 'c':
        r = calculaHarmonica(x,y,z)
        print('Resultado =', r)
    elif Menu == 'd':
        r = calculaAritmetica(x,y,z)
        print('Resultado =', r)
    else:
        print('Opção inválida')
        
    c = input('Deseja repetir o menu? digite s para SIM e n para NÃO ')
    if c != 's':
        break
    
        
