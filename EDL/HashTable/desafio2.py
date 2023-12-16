
from random import random, choice

#inicialização da Hash Table
hash_table = {}

while(True):
    
    print("1 - Incluir Componente:")
    print("2 - Ler todos o componentes:")
    print("3 - Ler ID:")
    print("4 - Excluir componente:")
    print("5 - Editar um ID:")
    print("0 - Sair")
    opcao = int(input())
    
    if opcao == 1:
        print("Digite a ID ao qual será incluída as informações")
        id_user = int(input())
        if id_user in hash_table:
            print("Id já cadastrada.")
        else:
            print("Digite a quantidade em estoque")
            estoque = int(input())
            print("Digite a localização")
            localizacao = str(input())
            print("Digite a informação do fornecedor")
            informacao = str(input())
            hash_table[id_user] = [(id_user, estoque, localizacao, informacao)]

        # if id_user not in hash_table:
        #     hash_table[id_user] = []
            

    if opcao == 2:
        if len(hash_table) > 0:
            for id_user, info_list in hash_table.items():
                print(f"Informações: {info_list}")
        else:
            print("Tabela Hash vazia!")

    elif opcao == 3:
        # Ler ID específica
        id_user = int(input("Digite a ID que deseja visualizar: "))
        if id_user in hash_table:
            print(f"Informações: {hash_table[id_user]}")
        else:
            print("ID não encontrada.")
            
    elif opcao == 4:
        print("Digite o id a ser exibido:")
        id_user = int(input())
        if id_user in hash_table:
            del hash_table[id_user]
        else:
            print("Id não encontrado!")
    
    elif opcao == 5:
        print("Digite a ID ao qual será editada as informações")
        id_user = int(input())
        if id_user in hash_table:
            print("Digite a nova quantidade em estoque")
            novo_estoque = int(input())
            print("Digite a nova localização")
            nova_localizacao = str(input())
            print("Digite a nova informação do fornecedor")
            nova_informacao = str(input())
            hash_table[id_user]=[(id_user, novo_estoque,nova_localizacao,nova_informacao)]
            
    elif opcao == 0:
        break
