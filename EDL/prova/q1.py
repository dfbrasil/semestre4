# 1. Criar um algoritmo de gerenciamento de inventário com inserção, busca e exclusão usando tabelas Hash.
# a. Chave da Tabela Hash: Código único do item no padrão XXX dígitos.
# b. Valores Associados: Quantidade em estoque, Latitude, Longitude, informações do fornecedor, CEP e OBS

hash_table = {}

def inserir_dado(id, qtd, lat, lon, inf, cep, obs):
    if id in hash_table:
        print("ID já cadastrada")
    else:
        id_completa = str(id).zfill(3)
        hash_table[id]={"ID":id_completa, "Quantidade":qtd, "Latitude":lat, "Longitude":lon, "Informações":inf, "CEP":cep, "Observação":obs}
        
def buscar_dado(id):
    if id in hash_table:
        print (hash_table[id])
    else:
        print("Id inávlido")

def deletar_dado(id):
    if id in hash_table:
        del hash_table[id]
    else:
        print("Id inávlido")

while(True):
    print("1 - Inserir Item")
    print("2 - Buscar Item")
    print("3 - Excluir Item")
    print("0 - Sair")
    
    option = int(input("Escolha uma opção: "))

    if option == 1:
        id = input("Digite o código do item: ")
        qtd = int(input("Digite a quantidade em estoque: "))
        lat = float(input("Digite a latitude: "))
        lon = float(input("Digite a longitude: "))
        inf = input("Digite as informações do fornecedor: ")
        cep = input("Digite o CEP: ")
        obs = input("Digite observações: ")

        inserir_dado(id, qtd, lat, lon, inf, cep, obs)
        print("Item inserido com sucesso!")
    
    elif option == 2:
        id = input("Digite o código do item: ")
        buscar_dado(id)
    
    elif option == 3:
        id = input("Digite o código do item: ")
        deletar_dado(id)
    
    elif option == 0:
        break