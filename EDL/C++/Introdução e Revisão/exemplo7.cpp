#include <iostream>
using namespace std;

// Definição da classe Elemento
class Elemento {
public:
    Elemento(int valor) : valor(valor) {}

    // Função para imprimir o valor do elemento
    void imprimir() {
        cout << "Valor do elemento: " << valor << endl;
    }

private:
    int valor;
};

int main() {
    // Criar um objeto da classe Elemento usando um ponteiro
    Elemento* elemento_ptr = new Elemento(42);

    // Chamar a função 'imprimir' do objeto usando o ponteiro
    elemento_ptr->imprimir();

    // Liberar a memória alocada pelo ponteiro
    delete elemento_ptr;

    return 0;
}




