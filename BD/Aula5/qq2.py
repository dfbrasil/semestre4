class ProductionOrder:
    def __init__(self, order_number, status, product_details, expiration_date, manufacture_date):
        self.order_number = order_number
        self.status = status
        self.product_details = product_details
        self.expiration_date = expiration_date
        self.manufacture_date = manufacture_date

    def __str__(self):
        return f"Order Number: {self.order_number}\nStatus: {self.status}\nProduct Details: {self.product_details}\nExpiration Date: {self.expiration_date}\nManufacture Date: {self.manufacture_date}"

class ProductionOrderManager:
    def __init__(self, size):
        self.size = size
        self.table = {}

    def hash_function(self, order_number):
        return hash(order_number) % self.size

    def add_production_order(self, order_number, status, product_details, expiration_date, manufacture_date):
        index = self.hash_function(order_number)
        if index not in self.table:
            self.table[index] = []
        order = ProductionOrder(order_number, status, product_details, expiration_date, manufacture_date)
        self.table[index].append(order)

    def find_production_order(self, order_number):
        index = self.hash_function(order_number)
        if index in self.table:
            for order in self.table[index]:
                if order.order_number == order_number:
                    return order
        return None

    def remove_production_order(self, order_number):
        index = self.hash_function(order_number)
        if index in self.table:
            for order in self.table[index]:
                if order.order_number == order_number:
                    self.table[index].remove(order)
                    return True
        return False

def menu():
    print("1 - Adicionar Ordem de Produção")
    print("2 - Buscar Ordem de Produção")
    print("3 - Remover Ordem de Produção")
    print("0 - Sair")

def main():
    size = 10  # Escolha o tamanho da tabela hash
    order_manager = ProductionOrderManager(size)

    while True:
        menu()
        option = int(input("Escolha uma opção: "))

        if option == 1:
            order_number = input("Digite o número da ordem de produção: ")
            status = input("Digite o status da ordem (Atrasado, Em dia, Adiantado): ")
            product_details = input("Digite os detalhes do produto: ")
            expiration_date = input("Digite o prazo de validade: ")
            manufacture_date = input("Digite a data de fabricação: ")

            order_manager.add_production_order(order_number, status, product_details, expiration_date, manufacture_date)
            print("Ordem de Produção adicionada com sucesso!")

        elif option == 2:
            order_number = input("Digite o número da ordem de produção a ser buscada: ")
            order = order_manager.find_production_order(order_number)
            if order:
                print("Ordem de Produção encontrada:")
                print(order)
            else:
                print("Ordem de Produção não encontrada.")

        elif option == 3:
            order_number = input("Digite o número da ordem de produção a ser removida: ")
            if order_manager.remove_production_order(order_number):
                print("Ordem de Produção removida com sucesso!")
            else:
                print("Ordem de Produção não encontrada.")

        elif option == 0:
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
