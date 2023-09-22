#include <iostream>
using namespace std;

class Produto{
public:
    Produto(int codigo, string nome, float preco) : codigo(codigo), nome(nome), preco(preco) {};

    void exibeDetalhes(){
        cout << "Código: " << codigo << endl;
        cout << "Nome: " << nome << endl;
        cout << "Preço: " << preco << endl;
    }

    void aplicaDesconto(float percentual){
        preco = preco * (1-percentual/100);
    }
private:
    int codigo;
    string nome;
    float preco;
};

int main() {

    Produto* ptr;

    ptr = new Produto(101, "camisa", 150);

    ptr->aplicaDesconto(10);

    ptr->exibeDetalhes();

    delete ptr;
    
    return 0;

}