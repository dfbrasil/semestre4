class SimpleHashMap:
    def __init__(self):
        # Inicializa a estrutura de dados (uma lista) para armazenar os pares chave-valor
        self.data = []

    def add(self, key, value):
        # Adiciona um par chave-valor à lista
        self.data.append((key, value))

    def get(self, key):
        # Procura o valor associado à chave na lista
        for k, v in self.data:
            if k == key:
                return v
        # Retorna None se a chave não for encontrada
        return None

    def remove(self, key):
        # Remove o primeiro par chave-valor com a chave especificada
        for item in self.data:
            if item[0] == key:
                self.data.remove(item)
                return

# Exemplo de uso
simple_map = SimpleHashMap()

# Adiciona pares chave-valor
simple_map.add(5,"apple")
simple_map.add(3,"banana")
simple_map.add(8,"cherry")

# Obtém valores usando as chaves
print("Get apple:", simple_map.get(5))  # Output: 5
print("Get banana:", simple_map.get(3))  # Output: 3
print("Get cherry:", simple_map.get(8))  # Output: 8

# Remove um par chave-valor
simple_map.remove(3)

# Tenta obter o valor associado à chave removida
print("Get banana:", simple_map.get(3))  # Output: None
print(simple_map.get(8))