from Functions import Functions
from ManipulateData import ManipulateData
from BTree import BTree
from Hash import HashMap

mostrar = Functions()
data_functions = ManipulateData()
B = BTree()
B.populate_tree()

H = HashMap()
H.populate_hash()


def show_admin_menu():
    print()
    print('-------------------------------------------------------------')
    print('-----------------Menu de Admin-------------------------------')
    print('-------------------------------------------------------------')
    print('1 - Ordenar arquivo de dados')
    print('2 - Mostrar todos os dados')
    print('3 - Busca binária por ID')
    print('4 - Criar arquivo de índices por ID')
    print('5 - Criar arquivo de índices por Nome')
    print('6 - Ordenar índices por Nome')
    print('7 - Criar indices por id com salto')

    option1 = int(input('Informe a opção: '))

    if option1 is 1:
        data_functions.ordenar()
    elif option1 is 2:
        mostrar.show_all_registers()
    elif option1 is 3:
        mostrar.binarySearch_it('1320547053177573378')
    elif option1 is 4:
        mostrar.create_index_file()
    elif option1 is 5:
        mostrar.crete_index_by_name()
        data_functions.order_index_name()
    elif option1 is 6:
        data_functions.order_index_name()
    elif option1 is 7:
        mostrar.create_index_file_by_id()
    else:
        print('Inválido')

def show_menu():
    print('9 - Sair')
    print('1 - Menu de admin')
    print('2 - Menu de apresentação')

    option = int(input('Informe a opção: '))

    return option

def show_menu_apresentacao():
    print()
    print('-------------------------------------------------------------')
    print('-----------------Menu de Apresentação------------------------')
    print('-------------------------------------------------------------')
    print('0 - Percorrer todo arquivo de dados')
    print('1 - Pesquisa binária no arquivo de dados')
    print('2 - Pesquisa binária no arquivo de índices ID')
    print('3 - Pesquisa binária no arquivo de índices USER')
    print('4 - Pesquisa árvore binária (Em memória)')
    print('5 - Hash por data (Em memória)')
    print('6 - Resposta da hipotese')
    print('7 - Outra forma pesquisa binaria dados por índice')

    option2 = int(input('Informe a opção: '))

    if option2 is 0:
        mostrar.show_all_registers()
    elif option2 is 1:
        mostrar.binarySearch_it('1320547053177573378')
    elif option2 is 2:
        mostrar.binarySearch_it_ID('1320878233915719684')
    elif option2 is 3:
        mostrar.binarySearch_USER('ygorasmar')
    elif option2 is 4:
        position = B.find('glhrrrme')
        if position != False:
            print(position)
            pos = int(position.position)
            mostrar.direct_in_data(position=pos)
        else:
            print('Não encontrado')
    elif option2 is 5:
        pos_hash = int(H.get('2020-10-28 19:59:38'))
        mostrar.direct_in_data(position=pos_hash)
    elif option2 is 7:
        mostrar.binarySearch_it_index_id('1320878233915719684')
    elif option2 is 6:
        hipo = mostrar.answare_hypothesis()

        print('__________________________________________________________')
        print('|         Incêndios foram criminosos ou acidentais       |')
        print('|________________________________________________________|')
        print('| Hipótese             |    Quantidade de citações       |')
        print('|________________________________________________________|')
        print('| Criminoso:           |            {}                   |'.format(hipo['criminoso']))
        print('| Acidental:           |            {}                   |'.format(hipo['acidente']))
        print('| Ação Humana:         |            {}                    |'.format(hipo['acao humana']))
        print('|________________________________________________________|')
        print('__________________________________________________________')
        print('|         Possiveis principais motivos dos incêndios     |')
        print('|________________________________________________________|')
        print('| Motivo               |    Quantidade de citações       |')
        print('|________________________________________________________|')
        print('| Gado:                |            {}                  |'.format(hipo['gado']))
        print('| Boi:                 |            {}                  |'.format(hipo['boi']))
        print('| Pasto:               |            {}                   |'.format(hipo['pasto']))
        print('| Aquecimento Global:  |            {}                   |'.format(hipo['aquecimento global']))
        print('| #ForaSalles:         |            {}                   |'.format(hipo['#forasalles']))
        print('| Seca:                |            {}                   |'.format(hipo['seca']))
        print('|________________________________________________________|')
        print('__________________________________________________________')
        print('|               Onde pegou mais fogo?                    |')
        print('|________________________________________________________|')
        print('| Local               |    Quantidade de citações        |')
        print('|________________________________________________________|')
        print('| Pantanal:           |            {}                  |'.format(hipo['pantanal']))
        print('| Amazônia:           |            {}                  |'.format(hipo['amazonia']))
        print('|________________________________________________________|')
    else:
        print('Inválido')


if __name__ == '__main__':
    option = 0
    while option is not 9:
        option = show_menu()
        print()

        if option == 1:
            show_admin_menu()
        elif option == 2:
            show_menu_apresentacao()
        elif option == 9:
            option = 9
        else:
            print('Inválido')


