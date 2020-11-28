M = list(range(0,12))

Nome = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

Media = 0

for i in range(0,12,1):
    M[i] = float(input('Informe a quantidade de km de congestionamento médio no mês ' + str(i + 1) + ': '))
    Media += M[i]

Media = Media / 12

print('Média anual = %.1f' %Media + 'km')

for i in range(0,12,1):    
    if M[i] > Media:
        print(str(i + 1) + ' - ' + Nome[i] + ' teve congestionamento acima da média')

