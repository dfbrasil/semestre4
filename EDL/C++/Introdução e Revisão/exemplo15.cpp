#include <iostream>
using namespace std;

class Produto{
public: 

    Produto (string nome, float preco) : nome(nome), preco(preco){};

    void imprime(){
        cout << "Produto: " << nome << " Valor: " << preco << endl;
    }

private:
    float preco;
    string nome;
};

int main (){

    Produto* ptr;

    ptr = new Produto("camisa", 10.99);

    ptr->imprime();


}