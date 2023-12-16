
from random import choice

#inicialização da hash_table
hash_table = {}

status = ["ativo", "inativo"]
localizacao = ["Bloco A", "Bloco B", "Bloco C"]

#inclusão dos elementos
for id in range(1,10):
    status_rand = choice(status)
    localizacao_rand = choice(localizacao)
    hash_table[id]=[(status_rand, localizacao_rand)]

while (True):
    print("Digite sua opção:")
    print("1 - Ler todos os IDs.")
    print("2 - Ler um ID.")
    print("3 - Excluir um ID.")
    print("4 - Editar um ID:")
    print("0 - Sair")

    option = int(input())
    
    if option == 1:
        #ler todos os componentes
        for id in range(1,10):
            print ("ID:", id, hash_table.get(id, "componente não encontrado"))
    
    elif option == 2:
        #ler único componente
        print("Digite a ID a ser mostrada:")
        read_id = int(input())
        if read_id in hash_table:
            print("ID:", read_id, hash_table[read_id])
        else:
            print("Id não encontrado")
    
    elif option == 3:
        #Apagar componente
        print("Digite a ID a ser apagada:")
        del_id = int(input())
        if del_id in hash_table:
            del hash_table[del_id]
        else:
            print("Id não encontrado")
    
    elif option == 4:
        print("Digite um ID a ser editado:")
        update_id = int(input())
        if update_id in hash_table:
            novo_status = choice(status)
            nova_localizacao = choice(localizacao)
            hash_table[update_id] = [(novo_status, nova_localizacao)]
        else:
            print("Id não encontrado")
    
    elif option == 0:
        break
