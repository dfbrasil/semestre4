
from random import choice

hash_table = {}
credenciais = ["Diretor","Gerente","Junior","Estagiário"]
niveis_acesso = ["1","2","3","4","5"]

while(True):
    
    print("1 - Incluir Credenciais e níveis de acesso:")
    print("2 - Ler todas as Credenciais e níveis de acesso:")
    print("3 - Ler Credenciais e níveis de acesso de uma ID:")
    print("4 - Excluir ID:")
    print("5 - Editar ID:")
    opcao = int(input())
    
    if opcao == 1:
        print("Qual a ID a ser credenciada?")
        id_credencial = int(input())
        
        if id_credencial not in hash_table:
            hash_table[id_credencial] = []
            
        credencial = choice(credenciais)
        nivel_acesso = choice(niveis_acesso)
        
        hash_table[id_credencial] = [id_credencial, credencial, nivel_acesso]
        
    elif opcao == 2:
        if len(hash_table)>0:
            for items_list in hash_table.items():
                print(f"Credenciais: {items_list}")
        else:
            print("Hash table vazia")
    
    elif opcao == 3:
        print("Qual a ID a ser verificada?")
        id_cred = int(input())
        
        if id_cred in hash_table:
            print(f"Credenciais: {hash_table[id_cred]}")
        else:
            print("ID não cadastrada")
    
    elif opcao == 4:
        print("Qual a ID a ser verificada?")
        id_cred = int(input())
        
        if id_cred in hash_table:
            del hash_table[id_cred]
        else:
            print("ID não cadastrada")
    
    elif opcao == 5:
        print("Digite o ID da credencial:")
        id_cred = int(input())
        if id_cred in hash_table:
            credencial = choice(credenciais)
            nivel_acesso = choice(niveis_acesso)
            hash_table[id_cred] = [id_cred, credencial, nivel_acesso]
        else:
            print("ID da credencial inválida")
    else:
        break
