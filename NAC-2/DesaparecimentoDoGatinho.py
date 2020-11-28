P = int(input('Quantas pessoas serão entrevistadas? '))

Q = list(range(0,5))

contador = 0

sim = 0

while contador < P:
    print('Responda todas as perguntas com s SIM ou n para NÃO:')
    Q[0] = input('Você sabia que Garfield, o gato de Dona Giorgina, está desaparecido? ')
    Q[1] = input('Você estava em casa no dia 25/09? ')
    Q[2] = input('Você ouviu um miado na rua nesse mesmo dia? ')
    Q[3] = input('Você viu um gato laranja na vizinhança na última semana? ')
    Q[4] = input('Você teve alguma interação com esse gato? ')

    for i in range(0,5,1):
        if Q[i] == 's':
            sim += 1
            
    if sim == 2:
        print('Suspeita')        
    elif sim == 3 or sim == 4:
        print('Cúmplice!')
    elif sim == 5:
        print('Ladrão de Gato!')
    else:
        print('Inocente. Não sabe de nada')

    sim = 0

    contador += 1
