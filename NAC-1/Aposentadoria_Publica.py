sexo = input("Informe seu sexo, M para masculino e F para feminino: ")
idade = int(input("Informe sua idade: "))
contribuicao = int(input("Informe seu tempo de contribuição para o INSS: "))

if sexo == "F" and idade >= 60 and contribuicao >= 15 or contribuicao >= 30 or idade + contribuicao >= 86:
    print("Você já pode se aposentar!")
elif idade >= 65 and contribuicao >= 15 or contribuicao >= 35 or idade + contribuicao >= 96:
    print("Você já pode se aposentar!")
else:
    print("Você ainda não pode se aposentar!")

