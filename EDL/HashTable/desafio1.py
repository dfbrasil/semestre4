# Desafio 1: Rastreamento de Componentes em Tempo Real
# Objetivo
# Desenvolver um sistema para rastrear componentes individuais na linha de produção, utilizando tabelas hash.
# Descrição
# Chave da Tabela Hash: ID único do componente.
# Valores Associados: Status atual, localização, histórico de processos.
# Aplicação: Monitoramento em tempo real dos componentes na linha de produção.
from random import choice


#inicialização da hash_table
hash_table = {}

status = ["ativo", "inativo"]
localizacao = ["Bloco A", "Bloco B", "Bloco C"]

#tratamento das colisões
for id in range(1,10):
    hash_table[id] = []

print("Quantos Ids serão incluídos?")
qtd_ids = int(input())

#inclusão dos elementos
for id in range(1,10):
    status_rand = choice(status)
    localizacao_rand = choice(localizacao)
    hash_table[id].append((status_rand, localizacao_rand))

while (True):
    print("Digite sua opção:")
    print("1 - Ler todos os IDs.")
    print("2 - Ler um ID.")
    print("3 - Excluir um ID.")    
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
    
    else:
        break
