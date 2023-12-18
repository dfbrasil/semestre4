# Criar um algoritmo para gerenciar ordens de produção usando tabelas hash.
# a. Chave da Tabela Hash: Número da ordem de produção no padrão (9898 - XXXX).
# b. Valores Associados: Status da ordem (Atrasado, Em dia e Adiantado), detalhes do produto, prazos de validade e Data de fabricação. Use os tipos corretos para

from random import choice

hash_table = {}

status = ["Atrasado", "Em dia", "Adiantado"]

def inserir_ordem(id, detalhe, prazo_validade, dada_fabricacao):
    if id not in hash_table:
        add_status = choice(status)
        id_completa = str(id).zfill(4)
        order_id = "9898 - " + str(id_completa)
        hash_table[id] = {"ID":order_id, "Status":add_status, "Detalhe":detalhe, "Prazo de Valdiade":prazo_validade, "Data de Fabricação": dada_fabricacao}

def buscar_ordem(order_id):
    if order_id in hash_table:
        print(hash_table[order_id])
    
    else:
        print("Ordem de Produção não encontrada.")

def deletar_ordem(order_id):
    if order_id in hash_table:
        del hash_table[order_id]
    else:
        print("Ordem de Produção não encontrada.")

def editar_ordem(id, novo_detalhe, novo_prazo_validade, nova_dada_fabricacao):
    if id in hash_table:
        add_status = choice(status)
        hash_table[id] = {"9898 -":id, "Status":add_status, "Detalhe":novo_detalhe, "Prazo de Valdiade":novo_prazo_validade, "Data de Fabricação": nova_dada_fabricacao}

while(True):
    print("1 - Inserir Ordem")
    print("2 - Buscar Ordem")
    print("3 - Excluir Ordem")
    print("4 - Editar Ordem")
    print("0 - Sair")
    
    option = int(input())

    if option == 1:
            order_id = input("Digite o número da ordem de produção: ")
            detalhe = input("Digite os detalhes do produto: ")
            data_validade = input("Digite o prazo de validade: ")
            data_fabricacao = input("Digite a data de fabricação: ")

            inserir_ordem(order_id, detalhe, data_validade, data_fabricacao)
            print("Ordem adicionada com sucesso!")

    elif option == 2:
        order_id = input("Digite o número da ordem de produção a ser buscada: ")
        buscar_ordem(order_id)
            
    elif option == 3:
        order_id = input("Digite o número da ordem de produção a ser apagada: ")
        order = deletar_ordem(order_id)
    
    elif option == 4:
        order_id = input("Digite o número da ordem de produção a ser editada: ")
        novo_detalhe = input("Digite os detalhes do produto: ")
        nova_data_validade = input("Digite o prazo de validade: ")
        nova_data_fabricacao = input("Digite a data de fabricação: ")
        editar_ordem(order_id, novo_detalhe, nova_data_validade, nova_data_fabricacao)
        
    elif option == 0:
        break