# Criar uma tabela hash para o IFRN
# – Inserir funcionário
# – Deletar funcionário
# – Tratar colisões
# – Buscar funcionário

from random import randint

hash_table = {}
for i in range(1, 10):
    hash_table[i] = []

for _ in range(1,10):
    matricula_funcionaraio = randint(0,3)
    id_rand = randint(1, 9)
    hash_table[id_rand].append(matricula_funcionaraio)
    
while(True):
    print("Digite 1 para visualizar")
    print("Digite 2 para deletar:")
    print("Digite 3 para visualizar todos")

    option = int(input())
    
    if option == 1:
        print("digite o id de busca do funcionario:")
        id_busca = int(input())
        if id_busca in hash_table:
            print("matrícula:", hash_table[id_busca])
        else:
            print("Id inávlido")
    
    elif option == 2:
        print("Digite o id do funcionário:")
        id_busca = int(input())
        if id_busca in hash_table:
            del hash_table[id_busca]
            
    elif option == 3:
        for i in range(1, 10):
            if i in hash_table:
                print(f"ID: {i}, Matrículas: {hash_table[i]}")
            else:
                print("Id inválido ou excluido")
    else:
        break
    