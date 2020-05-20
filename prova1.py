def tipo(entrada):
    '''Função para testar o tipo do dado digitado
    Retorna um string informando o tipo do dado (int, float ou string)'''
    import re
    if re.match('^\d+$', entrada):
        return "int"
    elif re.match('^\d+\.\d+$', entrada):
        return "float"
    else:
        return "str"


import os

'''Matrizes irão armazenar os containers em forma de pilhas.
Cada setor guarda, em pilhas, carga de um único tipo.'''
setor1 = [[], [], [], [], [], [], [], [], [], []]  # Eletrônicos
setor2 = [[], [], [], [], [], [], [], [], [], []]  # Alimentos
setor3 = [[], [], [], [], [], [], [], [], [], []]  # Matéria-prima
setor4 = [[], [], [], [], [], [], [], [], [], []]  # Química
setor5 = [[], [], [], [], [], [], [], [], [], []]  # Armamento

fila = []
# Navios pré-existentes
fila.append(dict(nome='Navio 01', pais='Argentina', container_navio='50', container_descarga='20', tipo_carga='1'))
fila.append(dict(nome='Navio 02', pais='China', container_navio='70', container_descarga='30', tipo_carga='2'))
fila.append(dict(nome='Navio 03', pais='EUA', container_navio='70', container_descarga='10', tipo_carga='3'))
fila.append(dict(nome='Navio 04', pais='Portugal', container_navio='100', container_descarga='15', tipo_carga='4'))
fila.append(dict(nome='Navio 05', pais='Bélgica', container_navio='80', container_descarga='40', tipo_carga='5'))
# =============================

repeticao1 = True
while repeticao1:
    # os.system('cls')
    opc = input(
        "*********************************\nSISTEMA DE GERENCIAMENTO DE CARGA\n    E DESCARGA DE CONTAINERS\n*********************************\n         MENU DE OPÇÕES\n\n1 - Adicionar Navio\n2 - Consultar Fila de Navios\n3 - Chamar Navio para Descarga\n4 - Retirar containers da pilha\n5 - Visualizar containers empilhados\n6 - Encerrar programa\n\n*********************************\nEscolha uma opção: ")
    os.system('cls')
    if tipo(opc) == "int":
        opc = int(opc)
        if opc == 1:
            #	repeticao1 = False
            repeticao2 = True
            while repeticao2:
                fila.append(dict(nome=input(
                    "**************************\nAdicionar um navio à fila\n**************************\nNome do navio: "),
                                 pais=input('País de origem: '),
                                 container_navio=input("Quantidade de containers no navio: "),
                                 container_descarga=input('Quantidade de comtainers que serão descarregados: '),
                                 tipo_carga=input(
                                     'Tipo da carga:\n1 - Alimentos\n2 - Eletrônicos\n3 - Matéria-Prima\n4 - Química\n5 - Armamento\nOpção:')))
                os.system('cls')
                # os.system('cls')
                if tipo(fila[-1]['container_navio']) != 'int' or tipo(fila[-1]['container_descarga']) != 'int' or tipo(
                        fila[-1]['tipo_carga']) != 'int':
                    os.system('cls')
                    tecla = input(
                        'A quantidade e tipo de containers, e o tipo da carga devem receber números inteiros!')
                    fila.pop(-1)
                    os.system('cls')
                elif int(fila[-1]['container_navio']) < int(fila[-1]['container_descarga']):
                    os.system('cls')
                    tecla = input(
                        'A quantidade de containers abordo do navio não pode ser menor que a quantidade a ser descarregada.\nPressione ENTER para continuar...')
                    fila.pop(-1)
                    os.system('cls')
                else:
                    tecla = input('Navio adicionado à fila.\nPressione ENTER para continuar...')
                    os.system('cls')
                    repeticao2 = False
        # repeticao1 = False
        elif opc == 2:
            # print('Consultar fila')
            if len(fila) == 0:
                tecla = input('Não há navios na fila!\nPressione ENTER para continuar...')
                os.system('cls')
            else:
                print('Fila de navios para desembarque\n')
                for i in range(len(fila)):
                    print('Navio: ', fila[i]['nome'], '\nPaís de origem: ', fila[i]['pais'],
                          '\nQuantidade de containers a bordo do navio: ', fila[i]['container_navio'],
                          '\nQuantidade de containers que serão desembarcados: ', fila[i]['container_descarga'],
                          '\nTipo da carga: ', fila[i]['tipo_carga'], '\n', '-' * 55)
                tecla = input('Pressione ENTER para continuar...')
                os.system('cls')
        elif opc == 3:
            if len(fila) == 0:
                tecla = input('Não há navios na fila!\nPressione ENTER para continuar...')
                os.system('cls')
            else:
                print('Descarga de Containers\n\nInformações sobre o navio\n', '-' * 55, '\nNome: ', fila[0]['nome'],
                      '\nPaís de origem: ', fila[0]['pais'], '\nQuantidade de containers abordo do navio: ',
                      fila[0]['container_navio'], '\nQuantidade de containers que serão desembarcados: ',
                      fila[0]['container_descarga'], '\nTipo da carga: ', fila[0]['tipo_carga'], '\n', '-' * 55)
                if int(fila[0]['tipo_carga']) == 1:
                    print('Eletrônicos')

                    i = 0
                    while int(fila[0]['container_descarga']) > 0:
                        if len(setor1[i]) < 10:
                            setor1[i].insert(0, 'EL1')
                            x = int(fila[0]['container_descarga'])
                            x -= 1
                            (fila[0]['container_descarga']) = x
                        elif len(setor1[i]) == 10:
                            i += 1
                            if len(setor1[-1]) == 10:
                                print('Setor está cheio!')
                                break
                        else:
                            break


                elif int(fila[0]['tipo_carga']) == 2:
                    print('Alimentação')

                    i = 0
                    while int(fila[0]['container_descarga']) > 0:
                        if len(setor2[i]) < 10:
                            setor2[i].insert(0, 'AL1')
                            x = int(fila[0]['container_descarga'])
                            x -= 1
                            (fila[0]['container_descarga']) = x
                        elif len(setor2[i]) == 10:
                            i += 1
                            if len(setor2[-1]) == 10:
                                print('Setor está cheio!')
                                break
                        else:
                            break


                elif int(fila[0]['tipo_carga']) == 3:
                    print('Matéria-Prima')

                    i = 0
                    while int(fila[0]['container_descarga']) > 0:
                        if len(setor3[i]) < 10:
                            setor3[i].insert(0, 'MP1')
                            x = int(fila[0]['container_descarga'])
                            x -= 1
                            (fila[0]['container_descarga']) = x
                        elif len(setor3[i]) == 10:
                            i += 1
                            if len(setor3[-1]) == 10:
                                print('Setor está cheio!')
                                break
                        else:
                            break


                elif int(fila[0]['tipo_carga']) == 4:
                    print('Química')

                    i = 0
                    while int(fila[0]['container_descarga']) > 0:
                        if len(setor4[i]) < 10:
                            setor4[i].insert(0, 'QU1')
                            x = int(fila[0]['container_descarga'])
                            x -= 1
                            (fila[0]['container_descarga']) = x
                        elif len(setor4[i]) == 10:
                            i += 1
                            if len(setor4[-1]) == 10:
                                print('Setor está cheio!')
                                break
                        else:
                            break


                elif int(fila[0]['tipo_carga']) == 5:
                    print('Armamento Militar')

                    i = 0
                    while int(fila[0]['container_descarga']) > 0:
                        if len(setor5[i]) < 10:
                            setor5[i].insert(0, 'AM2')
                            x = int(fila[0]['container_descarga'])
                            x -= 1
                            (fila[0]['container_descarga']) = x
                        elif len(setor5[i]) == 10:
                            i += 1
                            if len(setor5[-1]) == 10:
                                print('Setor está cheio!')
                                break
                        else:
                            break


                fila.pop(0)
                tecla = input('Pressione ENTER para continuar...')
                os.system('cls')


        elif opc == 4:
            print('Retirar containers da pilha')
            repeticao3 = True
            while repeticao3:
                opc2 = input('Pilhas\n1- Eletrônicos\n2 - Alimentos\n3 - Matéria-Prima\n4 - Químicos\n5 - Armamento\nOpção: ')
                if tipo(opc2) == 'int':
                    opc2 = int(opc2)
                    repeticao3 = False
                    if opc2 == 1:
                        print('Eletrônicos')
                    elif opc2 == 2:
                        print('Alimentos')
                    elif opc2 == 3:
                        print('Matéria-Prima')
                    elif opc2 == 4:
                        print('Químicos')
                    elif opc2 == 5:
                        print('Armamento')
                else:
                    tecla = input('Dado ínvalido!\nPressione ENTER para continuar...')
        elif opc == 5:
            print('Setor de Eletrônicos')
            print('       A   -  B   -  C   -  D   -  E   -  F   -  G   -  H   -  I   -  J')
            print('    --------------------------------------------------------------------')
            for i in range(10):
                print('{:02}'.format(i + 1), '', setor1[i])
            print('------------------------------------------------------------------------')
            print('Setor de Alimentos')
            print('       A   -  B   -  C   -  D   -  E   -  F   -  G   -  H   -  I   -  J')
            print('    --------------------------------------------------------------------')
            for i in range(10):
                print('{:02}'.format(i + 1), '', setor2[i])
            print('------------------------------------------------------------------------')
            print('Setor de Matéria-Prima')
            print('       A   -  B   -  C   -  D   -  E   -  F   -  G   -  H   -  I   -  J')
            print('    --------------------------------------------------------------------')
            for i in range(10):
                print('{:02}'.format(i + 1), '', setor3[i])
            print('------------------------------------------------------------------------')
            print('Setor de Química')
            print('       A   -  B   -  C   -  D   -  E   -  F   -  G   -  H   -  I   -  J')
            print('    --------------------------------------------------------------------')
            for i in range(10):
                print('{:02}'.format(i + 1), '', setor4[i])
            print('------------------------------------------------------------------------')
            print('Setor de Armamento Militar')
            print('       A   -  B   -  C   -  D   -  E   -  F   -  G   -  H   -  I   -  J')
            print('    --------------------------------------------------------------------')
            for i in range(10):
                print('{:02}'.format(i + 1), '', setor5[i])
            tecla = input('Precione ENTER para continuar...')
            os.system('cls')
        elif opc == 6:
            repeticao1 = False
        elif opc < 1 or opc > 6:
            tecla = input('Opção inválida!\nPressione ENTER para continuar...')
            os.system('cls')

    else:
        tecla = input('Opção inválida!\nPressione ENTER para continuar...')
        os.system('cls')