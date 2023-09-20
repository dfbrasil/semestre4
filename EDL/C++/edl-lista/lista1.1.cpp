#include <iostream>
using namespace std;

class Node{

public:

    int numero;
    Node* proximo;

    Node(int numero) : numero(numero), proximo(nullptr){};
};

class ListaEncadeada{
public:
    ListaEncadeada() : head(nullptr){};

    void InserirNumero(int numero){
        Node* novoNode = new Node(numero);
        novoNode->proximo = head;
        head = novoNode;
    }

    void imprimirNode(){
        Node* atual = head;

        while(head != nullptr) {

            cout << atual->numero << endl;
            atual = atual->proximo;
        }
    }

private:
Node* head;
};

int main() {

    ListaEncadeada lista;

    lista.InserirNumero(3);
    lista.InserirNumero(2);
    lista.InserirNumero(1);

    lista.imprimirNode();
return 0;
}