# Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o térreo), capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também disponibilizar os seguintes métodos:
# construtor : que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);
# Entrar : para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
# Sair : para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
# Subir : para subir um andar (não deve subir se já estiver no último andar);
# Descer : para descer um andar (não deve descer se já estiver no térreo);
# Encapsular todos os atributos da classe (criar os métodos set e get).

class Elevator:
    def __init__(self, actual_floor, number_of_floors, capacity, number_of_persons):
        self.__actual_floor = actual_floor
        self.__number_of_floors = number_of_floors
        self.__capacity = capacity
        self.__number_of_persons = number_of_persons

    def get_actual_floor(self):
        print(f' You are on {self.__actual_floor} floor')
        return self.__actual_floor
    
    def set_actual_floor(self,actual_floor):
        self.__actual_floor = actual_floor
    
    def get_number_of_floors(self):
        print (f'The building have {self.__number_of_floors} floors')
        return self.__number_of_floors
    
    def set_number_of_floors(self, number_of_floors):
        self.__number_of_floors = number_of_floors

    def get_capacity(self):
        print (f'The capacity of the elevator its {self.__capacity} persons')
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_number_of_persons(self):
        return self.__number_of_persons

    def set_number_of_persons(self, number_of_persons):
        self.__number_of_persons = number_of_persons

    def get_in(self, capacity):
        if self.__number_of_persons >= capacity:
            print(f'Maximum capacity reached of {self.__capacity} person')
        else:
            self.__number_of_persons += 1
            print (f'Now the elevator have {self.__number_of_persons} persons')
    
    def get_out(self):
        if self.__number_of_persons == 0:
            print(f'Elevator is empty and maximum capacity is available of {self.__capacity} persons')
        else:
            self.__number_of_persons -= 1
            print (f'Now the elevator have {self.__number_of_persons} persons')

    def go_up(self):
        if self.__actual_floor == self.__number_of_floors:
            print(f'You are already in the penthouse at, {self.__number_of_floors} floor')
        else:
            self.__actual_floor += 1
            print (f'Now we are on {self.__actual_floor} floor')

    def go_down(self):
        if self.__actual_floor == 0:
            print(f'You are already on the ground floor')
        else:
            self.__actual_floor -= 1
            print(f'Now we are on {self.__actual_floor} floor')