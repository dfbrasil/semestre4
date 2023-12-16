
hash_table = {}

while(True):
    
    print("1 - Incluir leitura:")
    print("2 - Ler todos o sensores:")
    print("3 - Ler sensor:")
    print("4 - Excluir sensor:")
    print("5 - Editar valores do sensor:")
    opcao = int(input())
        
    if opcao == 1:
        print("Digite o ID do sensor:")
        id_sensor = int(input())
        print("Digite a leitura do sensor:")
        leitura = float(input())

        if id_sensor not in hash_table:
            hash_table[id_sensor] = []
            
        hash_table[id_sensor].append((id_sensor, leitura))

    elif opcao == 2:
        if len(hash_table)>0:
            for id_sensor, items_list in hash_table.items():
                print(f"ID: {id_sensor}, Leitura{items_list}")
        else:
            print("Tabela Vazia")
            
    elif opcao == 3:
        print("Digite o ID do sensor:")
        id_sensor = int(input())
        if id_sensor in hash_table:
            print(f"{hash_table[id_sensor]}")
        else:
            print("ID do Sensor inválido")
        
    elif opcao == 4:
        print("Digite o ID do sensor:")
        id_sensor = int(input())
        if id_sensor in hash_table:
            del hash_table[id_sensor]
        else:
            print("ID do Sensor inválido")
    
    elif opcao == 5:
        print("Digite o ID do sensor:")
        id_sensor = int(input())
        if id_sensor in hash_table:
            print("Digite a nova leitura do sensor:")
            nova_leitura = float(input())
            hash_table[id_sensor][-1] = (hash_table[id_sensor][-1][0], nova_leitura)
        else:
            print("ID do Sensor inválido")
    else:
        break