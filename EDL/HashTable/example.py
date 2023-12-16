SIZE = 10

def hash_function(x):
    return x % SIZE

def insere(tabela, x):
    k = hash_function(x)

    # Lidando com colisões usando sondagem linear
    while tabela[k] != 0:
        k = (k + 1) % SIZE

    tabela[k] = x

def busca_hash(tabela, x):
    k = hash_function(x)

    # Procurando pela chave na tabela hash
    while tabela[k] != 0:
        if tabela[k] == x:
            return k  # Chave encontrada na posição k
        k = (k + 1) % SIZE

    return -1  # Chave não encontrada

def main():
    tabela = [0] * SIZE  # Inicializando a tabela hash com 0

    insere(tabela, 10)

    # Exemplo de busca
    chave = 8
    posicao = busca_hash(tabela, chave)

    if posicao != -1:
        print(f"Chave {chave} encontrada na posição {posicao}")
    else:
        print(f"Chave {chave} não encontrada na tabela hash.")
        
    print(tabela)

if __name__ == "__main__":
    main()
