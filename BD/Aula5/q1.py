class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = {}

    def hash_function(self, key):
        return hash(key) % self.size

    def insert_item(self, code, quantity, latitude, longitude, supplier_info, cep, obs):
        index = self.hash_function(code)
        if index not in self.table:
            self.table[index] = []
        self.table[index].append({
            'code': code,
            'quantity': quantity,
            'latitude': latitude,
            'longitude': longitude,
            'supplier_info': supplier_info,
            'cep': cep,
            'obs': obs
        })

    def search_item(self, code):
        index = self.hash_function(code)
        if index in self.table:
            for item in self.table[index]:
                if item['code'] == code:
                    return item
        return None

    def delete_item(self, code):
        index = self.hash_function(code)
        if index in self.table:
            for item in self.table[index]:
                if item['code'] == code:
                    self.table[index].remove(item)
                    return True
        return False

def menu():
    print("1 - Inserir Item")
    print("2 - Buscar Item")
    print("3 - Excluir Item")
    print("0 - Sair")

def main():
    size = 10  # Escolha o tamanho da tabela hash
    inventory_hash = HashTable(size)

    while True:
        menu()
        option = int(input("Escolha uma opção: "))

        if option == 1:
            code = input("Digite o código do item: ")
            quantity = int(input("Digite a quantidade em estoque: "))
            latitude = float(input("Digite a latitude: "))
            longitude = float(input("Digite a longitude: "))
            supplier_info = input("Digite as informações do fornecedor: ")
            cep = input("Digite o CEP: ")
            obs = input("Digite observações: ")

            inventory_hash.insert_item(code, quantity, latitude, longitude, supplier_info, cep, obs)
            print("Item inserido com sucesso!")

        elif option == 2:
            code = input("Digite o código do item a ser buscado: ")
            item = inventory_hash.search_item(code)
            if item:
                print("Item encontrado:")
                print(item)
            else:
                print("Item não encontrado.")

        elif option == 3:
            code = input("Digite o código do item a ser excluído: ")
            if inventory_hash.delete_item(code):
                print("Item excluído com sucesso!")
            else:
                print("Item não encontrado.")

        elif option == 0:
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
