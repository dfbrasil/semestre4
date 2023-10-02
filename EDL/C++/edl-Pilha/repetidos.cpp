#include <iostream>
using namespace std;

class Node{
public:

    int numero;
    Node* proximo;

    Node(int numero) : numero(numero) , proximo (nullptr){}
};

class Pilha{
public:

    Pilha() : head(nullptr), cont(0){}

    void inserir(int numero){
        Node* novoNode = new Node(numero);
        novoNode->proximo = head;
        head = novoNode;
        cont++;
    }

    void imprimir(){
        Node* atual = head;
        while(atual != nullptr){
            cout << atual->numero << endl;
            atual = atual->proximo;
        }
    }

    void repetidos(){
        Node* atual = head;
        int numtemp = atual->numero;

        while (atual != nullptr){
            if (numtemp == atual->proximo->numero){
                cout << "igual" << endl;
            }
            atual = atual->proximo;
            numtemp = atual->proximo->numero;
        }

        cout << atual->numero << endl;

    }

private:
    Node* head;
    int cont;
    
};

int main() {

    Pilha pilha;

    pilha.inserir(3);
    pilha.inserir(2);
    pilha.inserir(2);
    pilha.inserir(1);

    pilha.imprimir();

    pilha.repetidos();

return 0;

}