expressoes = ("+","-","*","/","p","f")
print("Uso de expressões pós-sign")
print()
sair = False
expressao = []
while (sair != True):
    expressao.append(input("Digite o valor (f - fim)-> "))
    #print(expressao)
    if expressao[-1] in expressoes:
        if expressao[-1] == "f":
            expressao.pop()
            sair = True
        elif expressao[-1] == "+":
            expressao.pop()
            expressao.append(int(expressao.pop(-2)) + int(expressao.pop(-1)))
        elif expressao[-1] == "-":
            expressao.pop()
            expressao.append(int(expressao.pop(-2)) - int(expressao.pop(-1)))
        elif expressao[-1] == "*":
            expressao.pop()
            expressao.append(int(expressao.pop(-2)) * int(expressao.pop(-1)))
        elif expressao[-1] == "/":
            expressao.pop()
            expressao.append(int(expressao.pop(-2)) / int(expressao.pop(-1)))
        elif expressao[-1] == "p":
            expressao.pop()
            expressao.append(int(expressao.pop(-2)) ** int(expressao.pop(-1)))
    print(expressao)
print("Fim...")