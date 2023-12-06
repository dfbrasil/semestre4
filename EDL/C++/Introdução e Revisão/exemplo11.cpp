#include <iostream>
using namespace std;

class Pessoa {
public:
    Pessoa(const string& nome, int idade) : nome(nome), idade(idade) {}

    void ImprimirDados() {
        cout << "Nome: " << nome << ", Idade: " << idade << " anos" << endl;
    }

private:
    string nome;
    int idade;
};

int main(){

   
    Pessoa pessoa1("daniel" , 10);
    
    Pessoa* ptr = &pessoa1;

    ptr->ImprimirDados();
}
