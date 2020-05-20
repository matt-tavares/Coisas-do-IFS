pilha = []
pilhaOrdenacao = []
print("="*40, "\n ORDENAR NÚMEROS USANDO DUAS PILHAS")
print("="*40)
print()
print("Informe os valores da pilha")
print()
# PREENCHENDO A PILHA
for cont in range(7):
    #pilha.insert(0,int(input('Informe o valor ' + str(cont + 1) + ' para a pilha: ')))
    valor = int(input('Informe o valor ' + str(cont + 1) + ' para a pilha: '))
    #contOrdenacao = 0
    if len(pilha) > 0:
        while len(pilha) > 0 and valor < pilha[0]:
            pilhaOrdenacao.insert(0,pilha.pop(0))
#        print("pilhaOrdenacao-> ",pilhaOrdenacao)
        pilha.insert(0,valor)
        while len(pilhaOrdenacao) > 0:
            pilha.insert(0,pilhaOrdenacao.pop(0))
    else:
        pilha.insert(0,valor)
    print("Pilha -> ",pilha)
# ESVAZIANDO A PILHA
print()
print("Esvaziando Pilha ...")
while len(pilha) > 0:
    pilha.pop(0)
    print(pilha)
# FINALIZANDO O PROGRAMA
print()
print("Fim...")
input("Pressione ENTER para sair...")