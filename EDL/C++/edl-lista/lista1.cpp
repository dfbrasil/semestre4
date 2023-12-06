#include <iostream>
using namespace std;

class Node{
public:
    int numero;
    Node* prox;

    Node(int numero) : numero(numero), prox(nullptr) {};
};

class ListaEncadeada{
public:
    ListaEncadeada() : head(nullptr) {};

    void inserirElemento(int numero){
        Node* newNode = new Node(numero);
        newNode->prox = head;
        head = newNode;
    }

    void imprimeLista(){
        Node* atual = head;
        while (atual != nullptr){
            cout << atual->numero;
            atual = atual->prox;
        }
    }

private:
    Node* head;

};

int main(){

    ListaEncadeada lista;

    lista.inserirElemento(1);
    lista.inserirElemento(2);
    lista.inserirElemento(3);


    cout << "elementos da lista: "<< endl;
    lista.imprimeLista();

    return 0;
}