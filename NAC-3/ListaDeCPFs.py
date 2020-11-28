n = []

#Carrega a lista com os CPFs
i = 0
while i < 10:
    CPF = input("Informe o CPF da pessoa " + str(i+1) + ": ")

    #Verifica se o número inserido realmente é um CPF
    if len(CPF) != 11:
        print("O CPF inserido não é válido.")
    else:
        n.append(CPF)
        i += 1

#Ordena os CPFs em ordem crescente 
for i in range(10-1):
    for j in range(i+1,10):
        if n[i] > n[j]:
            x = n[i]
            n[i] = n[j]
            n[j] = x

#Imprime a lista
for i in range(10):
    print("CPF " + str(i+1) + ":" , n[i])

continua = 'sim'

#Pesquisa binária
while continua == 'sim':
    pesquisa = input("Qual o CPF que deseja pesquisar? ")
    achou = False
    comeco = 0
    final = 9

    while comeco <= final and achou == False:
        meio = (comeco + final) // 2 

        if pesquisa == n[meio]:
            achou = True
        else:
            if pesquisa < n[meio]:
                final = meio - 1
            else:
                comeco = meio + 1
                
    if achou == True:
        print("Sua pesquisa pelo CPF " + pesquisa + " foi encontrada na posição:", meio+1)
    else:
        print("Sua pesquisa pelo CPF " + pesquisa + " não foi encontrada!")

    continua = input("Deseja relizar uma nova pesquisa? Responda com sim ou não.\n")

print("Pesquisa Encerrada!")

