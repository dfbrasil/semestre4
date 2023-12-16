from random import randint
from random_word import RandomWords
from utils import print_hash_table

random_words = RandomWords()
hash_table = {}

for id in range(1, 11):
    quantidade_em_estoque = randint(0, 100)
    localizacao = random_words.get_random_word()
    informacoes_fornecedor = random_words.get_random_word() + " " + \
        random_words.get_random_word()

    hash_table[id] = {
        "qtde_estoque": quantidade_em_estoque,
        "localizacao": localizacao,
        "informacoes_fornecedor": informacoes_fornecedor
    }


while True:
    id_item = int(input("Informe o id do item no inventário: "))
    if id_item in hash_table:
        print(f"Status atual: {hash_table[id_item]["qtde_estoque"]}")
        print(f"Localização: {hash_table[id_item]["localizacao"]}")
        print(f"Localização: {
              hash_table[id_item]["informacoes_fornecedor"]}\n")

        print("Quer rastrear outro item?")
        print("[1] Sim \n[2] Não")
        opcao = int(input())

        if opcao == 2:
            break
    else:
        print("Este item não está no inventário")
