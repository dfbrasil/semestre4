#include <iostream>
using namespace std;

class Node{
public:

    int numero;
    Node* proximo;

    Node(int value) : numero(value), proximo(nullptr){};

};

class ListaNumerica{
public:

    ListaNumerica() : head(nullptr){};

    void adicionaNumero(int numero){
        Node* novoNode = new Node(numero);
        novoNode->proximo = head;
        head = novoNode;
    }

    void exibirNumeros(){
        Node* atual = head;
        while(atual != nullptr){
            cout << atual->numero;
            atual = atual->proximo;
        }
    }
private:
    Node* head;
};

int main() {
    ListaNumerica lista;

    lista.adicionaNumero(10);
    lista.adicionaNumero(20);
    lista.adicionaNumero(30);

    cout << "Números na lista: ";
    lista.exibirNumeros();

    return 0;
}