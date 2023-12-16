from random import randint
from random_word import RandomWords
from utils import print_hash_table

random_words = RandomWords()
hash_table = {}

for id in range(1, 10):
    status_atual = random_words.get_random_word()
    localizacao = randint(20, 30)

    hash_table[id] = {
        "status_atual": status_atual,
        "localizacao": localizacao
    }

print_hash_table(hash_table)

while True:
    id_produto = int(input("Informe o id do componente a ser rastreado: "))
    if id_produto in hash_table:
        print(f"Status atual: {hash_table[id_produto]["status_atual"]}")
        print(f"Localização: {hash_table[id_produto]["localizacao"]}\n")

        print("Quer rastrear outro componente?")
        print("[1] Sim \n[2] Não")
        opcao = int(input())

        if opcao == 2:
            break
    else:
        print("Este componente não está sendo rastreado")
