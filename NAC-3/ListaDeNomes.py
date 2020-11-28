n = []

def ordenaEImprimeLista(lista,iInicial,iFinal):
    for i in range(iInicial,iFinal+1):
        for j in range(i,iFinal+1):
            if lista[i] > lista[j]:
                x = lista[i]
                lista[i] = lista[j]
                lista[j] = x

        print("Nome " + str(i) + ":" , lista[i])

print("Monte uma lista de 20 nomes.")
    
for i in range(20):
    n.append(input("Insira o nome " + str(i+1) + ": "))

while True:
    iInicial = int(input("Insira um índice inicial entre 0 e 19: "))    
    iFinal = int(input("Insira um índice final entre o valor do índice inicial e 19: "))

    if iFinal>= iInicial and iInicial <= 19 and iInicial >= 0 and iFinal <= 19 and iFinal >= 0:
        ordenaEImprimeLista(n,iInicial,iFinal)
    else:
        print("Índice inválido")

    c = input("Deseja ordenar uma faixa diferente da lista? Responda com sim ou não.\n")
    if c != "sim":
        break
    
