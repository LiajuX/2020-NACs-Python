alunos = []

#Cadastra alunos
while True:
    alunos.append(input("Cadastre o nome completo do aluno(a) " + str(len(alunos)+1) + ": "))

    c = input("Deseja cadastrar outro aluno? Responda com sim ou não.\n")

    if c != "sim":
        break

#Imprime nomes dos alunos cadastrados
for i in range(len(alunos)):
    print("Aluno " + str(i+1) + ":" , alunos[i])

continua = "sim"

#Pesquisa sequencial
while continua == "sim":
    pesquisa = input("Qual o nome que deseja pesquisar? ")
    achou = False
    i = 0
    
    while i < len(alunos) and achou == False:
        if pesquisa == alunos[i]:
            achou = True
        else:
            i += 1
            
    if achou == True:
        print("Sua pesquisa pelo aluno(a) " + pesquisa + " foi encontradada na posição:",i+1)
    else:
        print("Sua pesquisa pelo aluno(a) " + pesquisa + " não foi encontrada!")
        
    continua = input("Deseja realizar uma nova pesquisa? Responda com sim ou não.\n")
    
print("Pesquisa Encerrada!")
