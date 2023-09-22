#include <iostream>
using namespace std;

class Pessoa{
public:
    Pessoa(int idade) : idade(idade) {};
    
    void imprimeIdade(){
        cout << "Idade: " << idade << endl; 
    }

private:
    int idade;
};

int main(){

    Pessoa* ptr;

    ptr = new Pessoa(10); //Alocando dinamicamente um objeto Pessoa

    ptr->imprimeIdade();

    delete ptr;
}