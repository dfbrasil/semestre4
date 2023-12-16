# 1. Definindo a classe HashMap
class HashMap:
    # 2. O método __init__ é chamado quando criamos uma nova instância da classe
    def __init__(self):
        # 3. Inicializando o hashmap como um dicionário vazio
        self.map = {}

    # 4. Método para adicionar um par chave-valor ao hashmap
    def add(self, key, value):
        # 5. Armazenando o valor associado à chave no dicionário
        self.map[key] = value

    # 6. Método para obter o valor associado a uma chave no hashmap
    def get(self, key):
        # 7. Retornando o valor associado à chave (ou None se a chave não existir)
        return self.map.get(key)

    # 8. Método para remover um par chave-valor do hashmap
    def remove(self, key):
        # 9. Usando a função pop para remover a chave (se existir) e retornar o valor associado
        return self.map.pop(key, None)

# 10. Exemplo de uso
# Criando uma instância do hashmap
my_hashmap = HashMap()

# Adicionando pares chave-valor
my_hashmap.add("a", 1)
my_hashmap.add("b", 2)
my_hashmap.add("c", 3)
my_hashmap.add("a", 4)


# Obtendo valores associados às chaves
print("Valor associado à chave 'b':", my_hashmap.get("b"))  # Output: 2

# Removendo um par chave-valor
removed_value = my_hashmap.remove("a")
print("Valor removido:", removed_value)  # Output: 1

# Tentando obter o valor associado a uma chave removida
print("Valor associado à chave 'a' após remoção:", my_hashmap.get("a"))  # Output: None
print ( my_hashmap.get("c"))