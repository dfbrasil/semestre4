from random import choice

hash_table = {}
controle_qld = ["1", "2", "3", "4", "5"]
feedback = ["Ótimo", "Bom", "Regular", "Ruim", "Péssimo"]

def incluir_controle(id, controle_qld, feedback):
    controle = {"id": id, "controle_qld": controle_qld, "feedback": feedback}
    hash_table[id] = controle

def buscar_controle(id):
    return hash_table.get(id, None)

def print_all():
    if len(hash_table) > 0:
        for controle_id, controle in hash_table.items():
            print(controle)
    else:
        print("Hash table vazia")

def mostrar_controle_especifico(id):
    controle = buscar_controle(id)
    if controle:
        print(controle)
    else:
        print(f"Controle com ID {id} não encontrado.")

def editar_controle(id):
    controle = buscar_controle(id)
    if controle:
        print(f"Controle atual: {controle}")
        novo_controle_qld = input("Novo controle_qld: ")
        novo_feedback = input("Novo feedback: ")
        controle["controle_qld"] = novo_controle_qld
        controle["feedback"] = novo_feedback
        print(f"Controle editado: {controle}")
    else:
        print(f"Controle com ID {id} não encontrado.")

def deletar_controle(id):
    controle = buscar_controle(id)
    if controle:
        del hash_table[id]
        print(f"Controle com ID {id} deletado.")
    else:
        print(f"Controle com ID {id} não encontrado.")

while True:
    print("1 - Adicionar Controle")
    print("2 - Mostrar todos os controles")
    print("3 - Mostrar controle de ID específica")
    print("4 - Editar uma ID específica")
    print("5 - Deletar uma ID específica")
    print("0 - Sair")
        
    option = int(input())
    if option == 1:
        print("Qual ID terá incluso o controle?")
        prod_id = int(input())
    
        if buscar_controle(prod_id):
            print("Produto já cadastrado")
        else:
            controle_input = choice(controle_qld)
            feedback_input = choice(feedback)
            incluir_controle(prod_id, controle_input, feedback_input)
    elif option == 2:
        print_all()
    elif option == 3:
        print("Qual a ID a ser verificada?")
        prod_id = int(input())
        mostrar_controle_especifico(prod_id)
    elif option == 4:
        print("Qual a ID a ser editada?")
        prod_id = int(input())
        editar_controle(prod_id)
    elif option == 5:
        print("Qual a ID a ser deletada?")
        prod_id = int(input())
        deletar_controle(prod_id)
    elif option == 0:
        break
