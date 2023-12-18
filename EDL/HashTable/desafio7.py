# Desafio 7: Logística e Rastreamento de Remessas
# Objetivo
# Desenvolver um sistema para rastrear remessas usando tabelas hash.
# Descrição
# Chave da Tabela Hash: Número de rastreamento da remessa.
# Valores Associados: Localização atual, status da entrega, detalhes do destinatário.
# Aplicação: Eficiência no rastreamento e entrega de remessas.
from random_word import RandomWords
from random import choice

hash_table = {}

localizacao_atual = ["Bloco A", "Bloco B", "Bloco C"]
status_entrega = ["Em trânsito", "Entregue", "Atrasado"]
detalhes_destinatario = {"nome": RandomWords().get_random_word(),
                         "sobrenome": RandomWords().get_random_word(),
                         "endereco": RandomWords().get_random_word()}

while (True):
    print("1 - Adiocionar remessa")
    print("2 - Mostrar todas as remessas")
    print("3 - Mostrar remessa de ID específica")
    print("4 - Editar uma ID específica")
    print("5 - Deletar uma ID específica")
    
    option = int(input())
    
    if option == 1:
        print("Digite a ID para ser adicioanda")
        remessa_id = int(input())
        
        if remessa_id in hash_table:
            print("Id de memessa já cadastrada")
        else:
            localizacao_input = choice(localizacao_atual)
            status_input = choice(status_entrega)
            hash_table[remessa_id]=[remessa_id, localizacao_input, status_input, detalhes_destinatario]
    
    elif option == 2:
        if len(hash_table)>0:
            for remessa_id, remessa_items in hash_table.items():
                print(f"ID: {remessa_id}, ITEMS: {remessa_items}")
    
    else:
        break