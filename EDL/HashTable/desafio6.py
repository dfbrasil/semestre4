
from random import choice, randint

controle_qld = randint(1,11)
feedback = ["Ótimo", "Bom", "Regular", "Ruim", "Péssimo"]

hash_table = {}

while (True):
    print("1 - Adiocionar Controle")
    print("2 - Mostrar todos os controles")
    print("3 - Mostrar controle de ID específica")
    print("4 - Editar uma ID específica")
    print("5 - Deletar uma ID específica")
    
    option = int(input())
    if option == 1:
        print("Qual ID terá incluso o controle?")
        prod_id = int(input())
      
        if prod_id in hash_table:
            print("Produto já cadastrado")
        else:
            feedback_input = choice(feedback)
            hash_table[prod_id]=[prod_id,controle_qld,feedback_input]
    
    elif option == 2:
        if len(hash_table)>0:
            for prod_id in hash_table:
                print(hash_table[prod_id].items())
        else:
            print("Hash table vazia")
    
    elif option == 3:
        print ("Qual a ID a ser verificada?")
        prod_id = int(input())
        
        if prod_id in hash_table:
            print(hash_table[prod_id])
        else:
            print("Id não encontrada")
    
    elif option == 4:
        print ("Qual a ID a ser verificada?")
        prod_id = int(input())
        
        if prod_id in hash_table:
            feedback_input = choice(feedback)
            hash_table[prod_id]=[prod_id,controle_qld,feedback_input]
        else:
            print("Id não encontrada")

    elif option == 5:
        print ("Qual a ID a ser verificada?")
        prod_id = int(input())
        
        if prod_id in hash_table:
            del hash_table[prod_id]
        else:
            print("Id não encontrada")
    
    else:
        break