class No:
    def __init__(self,item=None,dir=None,esq=None):
        self.item = item
        self.dir = dir
        self.esq = esq

class ArvoreBinaria:
    def __init__(self):
        self.raiz = No(None,None,None)
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor,None,None) # Cria um novo Nó
        if self.raiz == None:
            self.raiz = novo
        else: # Se não for raiz
            atual = self.raiz
            while True:
                anterior = atual
                if valor <= atual.item: # Ir para a esquerda
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = None
                        return
                    # Fim da condição ir a esquerda
                    else: # Ir para a direita
                        atual = atual.dir
                        if atual == None:
                            anterior.dir = novo
                            return
                        # Fim da condição ir a direita

    def buscar(self, chave):
        if self.raiz == None:
            return None # Se árvore vazia
        atual = self.raiz # Começa a procurar desde a raiz
        while atual.item != chave: # Enquanto não encontrou
            if chave < atual.item:
                atual = atual.esq # Caminha para a esquerda
            else:
                atual = atual.dir # Caminha para a direita
            if atual == None:
                return None # Não encontrou uma folha -> Sai
        return atual # Começou o laço e chegou aqui é pq encontrou item

    # O sucessor é o nó mais a esquerda sa subarvore a direita do nó que foi passado como paramentro do metodo
    def noSucessor(self,apaga): # O parametro é a referencia para o nó que deseja-se apagar
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.dir # caminha para a direita

        while atual != None: # Enquanto não chegar no Nó mais a esuqerda
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esq #Caminha para a esquerda

    #*********************************************************************************
    # Quando sair do while "sucessor" será o Nó mais a esquerda da subarvore a direita
    # "paidosucessor" será o pai de sucessor e "apaga" o Nó que deverá ser eliminado
    #*********************************************************************************

        if sucessor != apaga.dir: # Se sucessor não é o filho a direita do Nó que deverá ser eliminado
            paidosucessor.esq = sucessor.dir # pai do sucessor herda os filhos do sucessor que sempre serão a direita
            # lembrando que o sucessor nunca poderá ter filhos a esquerda, pois, ele sempre será o
            # o Nó mais a esquerda da subarvore a direita do Nó apaga
            # Lembrando tbm que sucessor sempre será o filho a esquerda do pai
            sucessor.dir = apaga.dir # Guardando a referencia a direita do sucessor para
                                     # quando ele assumir a posição correta na árvore
            return sucessor

    def remover(self, valor):
        if self.raiz == None:
            return False # Árvore vazia
        atual = self.raiz
        pai = self.raiz
        filho_esq = True
        # ****** Buscando o valor ******
        while atual.item != valor: # Enquanto não encontrou
            pai = atual
            if valor < atual.item: # Caminha para a esquerda
                atual = atual.esq
                filho_esq = True # é filho a esquerda? sim
            else: # caminha para direita
                atual = atual.dir
                filho_esq = False # é filho a esquerda? não
            if atual == None:
                return False # encontrou uma folha -> sai
        # fim do laço while de buscar o valor

        #**************************************************************
        # se chegou aqui quer dizer que encontrou o valor (valor)
        #"atual": contem a referencia ao No a ser eliminado
        #"pai": contem a referencia para o pai do No a ser eliminado
        #"filho_esq": é verdadeiro se atual é filho a esquerda do pai
        #**************************************************************

        # se nao possui nenhum filho (é uma folha), elimine-o
        if atual.esq == None and atual.dir == None:
            if atual == self.raiz:
                self.raiz = None # se raiz
            else:
                if filho_esq:
                    pai.esq = None # se for filho a esquerda do pai
                else:
                    pai.dir = None # se for filho a direita do pai
        # se é pai e nao possui um filho a esquerda, substitui pela subarvore a direita
        elif atual.dir == None:
            if atual == self.raiz:
                self.raiz = atual.dir # se raiz
            else:
                if filho_esq:
                    pai.esq = atual.dir # se for filho a esquerda do pai
                else:
                    pai.dir = atual.dir # se for filho a direita do pai

        # se possui mais de um filho, se for avô ou outro grau de parentesco
        else:
            sucessor = self.noSucessor(atual)
            # Usando sucessor que seria o No mais a esquerda da subarvore a direita do No
            # que deseja-se remover
            if atual == self.raiz:
                self.raiz = sucessor # se raiz
            else:
                if filho_esq:
                    pai.esq = sucessor # se for filho a esquerda do pai
                else:
                    pai.dir = sucessor # se for filho a direita do pai
            sucessor.esq = atual.esq # acertando o ponteiro a esquerda do sucessor
                                     # agora que ele assumiu a posição correta na arvore
        return True

    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esq)
            print(atual.item,end=" ")
            self.inOrder(atual.dir)