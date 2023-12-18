# Crie um algoritmo que gere uma tabela de hash resultante da introdução das chaves 12, 44, 13, 88, 23, 94, 11, 39, 20, 16 e 5, usando a função de hash igual h(k) = (2k + 5)%11 e supondo que as colisões sejam tratadas por encadeamento separado (uma lista na posição da colisão).

def funcao_hash(key, size):
    return (2 * key + 5) % 11

def inserir_chave(table, key):
    id = funcao_hash(key, len(table))
    if table[id] is None:
        table[id] = [key]
    else:
        table[id].append(key)

def exibir_tabela(table):
    for i, chain in enumerate(table):
        print(f"Índice {i}: {chain}")

keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
hash_table = [None] * 11

for key in keys:
    inserir_chave(hash_table, key)

exibir_tabela(hash_table)
