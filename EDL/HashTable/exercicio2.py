from random import randint

hash_table = {}

for i in range(1,10):
    hash_table[i] = []
    
for _ in range(1,11):
    matricula = randint(1,4)
    id_rand = randint(1, 9)
    hash_table[id_rand].append(matricula)
    
while(True):
    print("Digite 1 para listar todas as matrículas")
    print("Digite 2 para buscar uma matrícula")
    print("Digite 3 para deletar uma matrícula")
    
    option = int(input())
    if option == 1:
        for i in range(1,10):
            print("matrícula: ",hash_table.get(i, 'Id não encontrado'))
    elif option == 2:
        print("Digite o ID para fazer a busca")
        id_busca = int(input())
        if id_busca in hash_table:
            print(f'A matrículad do ID {id_busca} é: {hash_table[id_busca]}')
    elif option == 3:
        print("Digite o ID para fazer a deleção")
        id_busca = int(input())
        if id_busca in hash_table:
            del hash_table[id_busca]
        else:
            print("ID excluído")
    else:
        break