from random import randint

hash_table = {}

for id in range(1,31):
    valores_do_dicionario = [randint(1,300), randint(1,300)]
    hash_table[id] = valores_do_dicionario
    
id_busca = int(input("digite o id"))

print (hash_table[id_busca])

