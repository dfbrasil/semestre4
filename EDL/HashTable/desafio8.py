
from random import choice

hash_table = {}

def incluir_dado(id, dados, demanda, avaliacao):
    if id in hash_table:
        print("ID inválido")
    else:
        hash_table[id]={"ID":id, "dados":dados, "demanda": demanda, "avaliacao": avaliacao}

def buscar(id):
    if id in hash_table:
        return hash_table[id]
    else:
        print("ID não cadastrada")
    
def print_all():
    if len(hash_table)>0:
        for id_cat, items_cat in hash_table.items():
            print(f"Items:{items_cat}")
            
def print_id(id):
    if id in hash_table:
        print(hash_table[id])
    else:
        print("ID não cadastrada")
        
def update_id(id, dados, demanda, avaliacao):
    if id not in hash_table:
        print("ID inválido")
    else:
        hash_table[id]={"ID":id, "dados":dados, "demanda": demanda, "avaliacao": avaliacao}
        
def delete_id(id):
    if id not in hash_table:
        print("ID inválido")
    else:
        del hash_table[id]

while True:
    print("1 - Adicionar Categoria")
    print("2 - Mostrar todos as Categorias")
    print("3 - Mostrar categoria de ID específica")
    print("4 - Editar uma ID específica")
    print("5 - Deletar uma ID específica")
    print("0 - Sair")
    
    option = int(input())
    
    if option == 1:
        print("Digite a ID")
        id_cat = int(input())
        print("Digite os Dados de venda")
        data_venda = str(input())
        print("Digite a Demanda")
        data_demanda = float(input())
        print("Digite a Avaliação")
        data_avaliacao = int(input())
        incluir_dado(id_cat, data_venda, data_demanda, data_avaliacao)
    
    elif option == 2:
        print_all()
        
    elif option == 3:
        print("Qual a ID você quer visaulizar?")
        id = int(input())
        print_id(id)
        
    elif option == 4:
        print("Digite a ID")
        id_cat = int(input())
        if buscar(id_cat):
            print("Digite os novos Dados de venda")
            nova_data_venda = str(input())
            print("Digite a nova Demanda")
            nova_data_demanda = float(input())
            print("Digite a nova Avaliação")
            nova_data_avaliacao = int(input())
            update_id(id_cat, nova_data_venda, nova_data_demanda, nova_data_avaliacao)
    
    elif option == 5:
        print("Digite a ID")
        id_cat = int(input())
        delete_id(id_cat)
    
    else:
        break