
# Crie uma classe Agenda que pode armazenar dados de pessoas e que seja capaz de realizar as seguintes operações:
# void salvar_contato(nome, telefone, email);
# void remover_contato(nome);
# int buscar_pessoa(String nome); // retorna a(s) posição(ões) do(s) contato(s) com o nome pesquisado;
# void imprimir_agenda(); // exibe os dados de todas as pessoas da agenda
# void detalhar_contato(int index); // imprime os dados da pessoa que está na posição “i” da agenda.

class AppointmentBook:

    def __init__ (self):
        # self.__name = name
        # self.__phone = phone
        # self.__email = email
        self.contacts = {}
        self.contact_list = []

    def save(self):
        name = input('Name: ').strip()
        phone = input('Phone: ').strip()
        email = input('Email: ').strip()
        self.contacts[name] = {
            'name': name,
            'phone': phone,
            'email':email
        }
        self.contact_list.append(self.contacts)
        return self.contact_list

    def remove_contact(self):
        name = input('Name: ').lower()
        if name in self.contacts:
            print(f'O contato {name} será deletado!')
            self.contacts.pop(name)
            return self.contacts
        else:
            print ('That name isnt in contacts')
        
    def search_contact(self):
        name = input('Name: ').lower()
        if name in self.contacts:
            for i, name in enumerate(self.contacts):
                print (i, name)
        else:
            print('That name isnt in contacts')
    
    def print(self):
        for key, value in self.contacts.items():
            print(f'{key}: {value}')
    
    def detail_contact(self):
        id = int(input('Id: '))
        for i, name in enumerate(self.contacts):
            if i == id:
               for key, value in self.contacts.items():
                print(f"{key}: {value}")
