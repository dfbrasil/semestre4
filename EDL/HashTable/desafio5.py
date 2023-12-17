# Desafio 5: Gerenciamento de Ordens de Produção
# Objetivo
# Criar um sistema para gerenciar ordens de produção usando tabelas hash.
# Descrição
# Chave da Tabela Hash: Número da ordem de produção.
# Valores Associados: Status da ordem, detalhes do produto, prazos.
# Aplicação: Otimização do fluxo de produção e acompanhamento de ordens.
from random import choice, randint

hash_table = {}

status = ["Aberto","Fechado","Em Espera"]
detalhes = ["Novo", "Seminovo", "Usado"]
prazo = randint(1,31)

while(True):
    print('1 - Adicionar Ordem')
    print('2 - Verificar todas as Ordens')
    print('3 - Apagar Ordem')
    print('4 - Atualizar Ordem')
    print('0 - sair')
    
    option = int(input())
    
    if option == 1:
        
        print('Digite o ID da ordem')
        id_ordem = int(input())
        
        if id_ordem in hash_table:
            print('Id da ordem já existe')
        else:
            stt = choice(status)
            dtl = choice(detalhes)
            hash_table[id_ordem] = [id_ordem, stt, dtl, prazo]
    
    elif (option == 2):
        
        if len(hash_table)>0:
            for id_ordem, order_itens in hash_table.items():
                print(f'ID: {id_ordem}, Itens: {order_itens}')
        else:
            print('Hash Table Vazia')
            
    elif option == 3:
        
        print('Digite o ID da ordem')
        id_ordem = int(input())
        
        if id_ordem in hash_table:
            del hash_table[id_ordem]
        
        else:
            print('Id não cadastrada')
    
    elif option == 4:
        
        print('Digite o ID da ordem')
        id_ordem = int(input())
        
        if id_ordem in hash_table:
            stt = choice(status)
            dtl = choice(detalhes)
            hash_table[id_ordem] = [id_ordem, stt, dtl, prazo]
        
        else:
            print('Id não cadastrada')
    
    elif option == 0:
        break
        
            