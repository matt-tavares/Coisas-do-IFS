import os
def LimparTela():
    return os.system("cls")

class HashMap:
    def __init__(self):
        self.tam_max = 97
        self.mapa = [None] * self.tam_max

    def Hash(self, chave):
        return chave % self.tam_max

    def Inserir(self, chave, produto, quantidade):
        chave_hash = self.Hash(chave)
        chave_valor = [chave, produto, quantidade]

        if self.mapa[chave_hash] is None:
            self.mapa[chave_hash] = list([chave_valor])
            return True
        else:
            for par in self.mapa[chave_hash]:
                if par[0] == chave:
                    return False
            self.mapa[chave_hash].append(chave_valor)
            return True

    def Buscar(self, chave):
        chave_hash = self.Hash(chave)
        if self.mapa[chave_hash] is not None:
            for par in self.mapa[chave_hash]:
                if par[0] == chave:
                    print("Código: ",par[0], "\nProduto: ",par[1], "\nQuantidade: ",par[2])
                    return input("\nPressione ENTER para continuar...")
        return input("Dado não encontrado! Pressione ENTER para continuar...")

    def Apagar(self, chave):
        chave_hash = self.Hash(chave)
        if self.mapa[chave_hash] is None:
            LimparTela()
            input("Dado não encontrado! Pressione ENTER para continuar...")
            return False
        for i in range(0, len(self.mapa[chave_hash])):
            if self.mapa[chave_hash][i][0] == chave:
                self.mapa[chave_hash].pop(i)
                LimparTela()
                input("Produto excluído! Pressione ENTER para continuar...")
                return True
        return False

    # def Chave(self):
    #     arr = []
    #     for i in range(0, len(self.mapa)):
    #         if self.mapa[i]:
    #             arr.append(self.mapa[i][0])
    #     return arr

    # def MostrarTabela(self):
    #     print("---Lista Completa---")
    #     for dado in self.mapa:
    #         if dado is not None:
    #             print(str(dado))

    def Mostrar(self):
        achou = False
        for dado in self.mapa:
            if dado is not None:
                for i in dado:
                    achou = True
                    print("="*40)
                    print("Código: ",i[0], "\nProduto: ",i[1], "\nQuantidade: ",i[2])
                    print("="*40)
                    print()
        if achou:
            input("Pressione ENTER para continuar...")
        else:
            input("Não há produtos cadastrados! Pressione ENTER para continuar...")


def TeamPaulo():
    print("    #   #      #########  #########  #########  ###     ###")
    print("  #########        #      #          #       #  #  #   #  #")
    print("   #    #          #      #########  #########  #   # #   #")
    print("  ########         #      #          #       #  #    #    #")
    print("   #    #          #      #########  #       #  #         #")
    print()
    print()
    print("    #########  #########  #       #  #          #########")
    print("    #       #  #       #  #       #  #          #       #")
    print("    #########  #########  #       #  #          #       #")
    print("    #          #       #  #       #  #          #       #")
    print("    #          #       #  #########  #########  #########")
    input()

if __name__ == "__main__":
    dados = HashMap()

    while 1:
        LimparTela()
        print("="*70)
        print("="*30,"  MENU  ","="*30)
        print("1: Cadastar\n"
              "2: Consultar produtos\n"
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
                    flag = dados.Inserir(int(codigo), produto, quantidade)
                    LimparTela()
                    if flag:
                        input("Cadastro concluído! Pressione ENTER para continuar...")
                    else:
                        input("Código existente! Pressione ENTER para continuar...")
                    break

                elif opc == "0":
                    break

                else:
                    input("Opção inválida! Pressione ENTER para continuar...")

        elif opc == "2":
            LimparTela()
            print("="*70)
            print("="*23, " PRODUTOS CADASTRADOS ", "="*23)
            print("="*70)
            dados.Mostrar()

        elif opc == "3":
            LimparTela()
            print("="*70)
            print("="*26, " BUSCAR PRODUTO ", "="*26)
            print("="*70)
            codigo = input("Código do produto: ")
            LimparTela()
            print("INFORMAÇÕES DO PRODUTO BUSCADO")
            print()
            print(dados.Buscar(int(codigo)))

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
                    LimparTela()
                    print("=" * 70)
                    print("=" * 24, " EXCLUIR CADASTRADOS ", "=" * 23)
                    print("=" * 70)
                    codigo = input("Código do produto a ser excluído: ")
                    dados.Apagar(int(codigo))
                    break

                elif opc == "0":
                    break

                else:
                    input("Opção inválida! Presione ENTER para continuar...")

        elif opc == "0":
            LimparTela()
            TeamPaulo()
            break

        else:
            input("Opção inválida! Pressione ENTER para continuar...")
