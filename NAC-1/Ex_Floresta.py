contador = 1

n = int(input("Informe um valor inteiro e positivo: "))

S = 0

print("Resultado:")

while contador <= n:
    S += 1/contador
    contador += 1

print(S)
