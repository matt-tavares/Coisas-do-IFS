import os

def LimparTela():
    return os.system("cls")

class ListaEncadeada:
    def __init__(self, indice=None, proximo=None, cod_produto=None, descricao=None, quantidade=None):
        self.indice = indice
        self.proximo = proximo
        self.cod_produto = cod_produto
        self.descricao = descricao
        self.quantidade = quantidade

class Tabela:
    def __init__(self, indice=None, proximo=None, lista=None):
        self.indice = indice
        self.proximo = proximo
        self.lista = lista
        self.listaB = ListaEncadeada()

tam_max = 4 # Variável para definir o tamanho máximo das listas do hash

def InstanciarTabela(tabela, posicao):
    if tabela == None:
        tabela = Tabela(posicao, None, None)

    #if contador_tabela == 0:
    #    tabela.indice = posicao
    #    tabela.proximo =

    else:
        while tabela:
            cabeca = tabela
            tabela = tabela.proximo
        cabeca.proximo = Tabela(posicao,None, None)

def InstanciarLista(lista, posicao):
    if lista == None:
        lista = ListaEncadeada(posicao)
    while lista:
        cabeca = lista
        lista = lista.proximo
    cabeca.proximo = ListaEncadeada(posicao, None, None, None)

def Hash(valor):
    return int(valor) % tam_max

def Hash2(valor):
    return 1 + (valor % (tam_max - 1))

def HashLista(lista, entrada):
    pos = Hash(entrada.cod_produto)
    flag = 0
    if lista == None:
        lista = entrada
    if pos == 0:
        lista.cod_produto = entrada.cod_produto
        lista.descricao = entrada.descricao
        lista.quantidade = entrada.quantidade
    else:
        while pos != flag and lista != None:
            lista = lista.proximo
            flag += 1
        lista.cod_produto = entrada.cod_produto
        lista.descricao = entrada.descricao
        lista.quantidade = entrada.quantidade

def InserirTabela(lista, entrada, matricula): #ainda incompleta
    enter = entrada
    pos = Hash(matricula)
    if pos == 0:
        #lista.matricula = matricula
        lista.listaB = enter
        HashLista(lista.listaB, enter)
    repeticao = 0
    while repeticao != pos and lista != None:
        lista = lista.proximo
        repeticao += 1
    #lista.matricula = matricula
    lista.listaB = enter
    HashLista(lista.listaB, enter)

def Mostrar(lista): # Ainda está incompleta
    if lista.indice == None:
        print("Lista vazia...")
    while lista:
        print(lista.indice,"\n")
        lista = lista.proximo

if __name__ == "__main__":
    contador_tabela = 0
    dado = ListaEncadeada(0, None, None, None)
    tabela = Tabela(0, None, None)

    # Instanciar as listas
    for i in range(1, tam_max):
        InstanciarLista(dado, i)

    # Instanciar a tabela
    for i in range(1, tam_max):
        InstanciarTabela(tabela, i)

    while tabela != None:
        if tabela.indice == 0:
            tabela.lista = dado
        else:
            tabela = tabela.proximo
            dado = dado.proximo
            tabela.lista = dado

    while 1:
        LimparTela()
        print("="*70)
        print("="*30,"  MENU  ","="*30)
        print("1: Cadastar\n"
              "2: Consultar tipos de produto\n"
              "3: Buscar produto\n"
              "4: Excluir\n"
              "0: Sair")
        print("="*70)
        opc = input("Opção: ")


        if opc == "1":
            while 1:
                LimparTela()
                print("="*70)
                print("="*25," MENU DE CADASTRO ","="*25)
                print("1: Cadastrar produto\n"
                      "0: Voltar ao menu anterior")
                print("="*70)
                opc = input("Opção: ")

                if opc == "1":
                    LimparTela()
                    print("=" * 70)
                    print("=" * 24, " CADASTRO DO PRODUTO ", "=" * 23)
                    print("="*70)
                    codigo = input("Código do produto: ")
                    produto = input("Produto: ")
                    quantidade = input("Quantidade: ")
                    data = ListaEncadeada(None, None, codigo, produto, quantidade)
                    InserirTabela(tabela, data, codigo)



                    contador_tabela += 1
                    break

                elif opc == "0":
                    break
                else:
                    input("Opção inválida! Pressione ENTER para continuar...")

        elif opc == "2":
            print("Consultar")
            input()

        elif opc == "3":
            print("Buscar")
            input()

        elif opc == "4":
            while 1:
                LimparTela()
                print("=" * 70)
                print("=" * 25, " MENU DE EXCLUSÃO ", "=" * 25)
                print("1: Excluir produto\n"
                      "0: Voltar ao menu anterior")
                print("=" * 70)
                opc = input("Opção: ")

                if opc == "1":
                    print("Excluir produto")
                    input()
                    break
                elif opc == "0":
                    break
                else:
                    input("Opção inválida! Presione ENTER para continuar...")

        elif opc == "0":
            break

        else:
            input("Opção inválida! Pressione ENTER para continuar...")
