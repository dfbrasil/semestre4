#include <iostream>
using namespace std;

class Node{

public:  
    int numero;
    Node* proximo;

    Node(int numero) : numero(numero), proximo(nullptr){};
};

class Pilha{
public:
    Pilha() : head(nullptr), qtd(0){};

    void empilharNode(int numero){
        Node* novoNode = new Node(numero);
        novoNode->proximo = head;
        head = novoNode;
        qtd++;
    }

    int quantidadeNode(){
        return qtd;
    }

    void imprimirPilha(){
        Node* atual = head;
        if (atual == nullptr){
            cout << "Pilha vazia" << endl;
        }
        while (atual != nullptr){
            cout << atual->numero << endl;
            atual = atual->proximo;
        }
    }

    void desempilharNode(){

        if (head == nullptr){
            cout << "pilha já está vazia" << endl;
        }

        Node* temp = head;
        head = head->proximo;
        delete temp;
        qtd--;
    }

private:
    Node* head;
    int qtd;
};

int main() {

    Pilha pilha;

    pilha.empilharNode(44);
    pilha.empilharNode(55);
    pilha.empilharNode(66);

    pilha.imprimirPilha();

    cout << endl;

    cout << pilha.quantidadeNode() << endl;

    pilha.desempilharNode();

    pilha.imprimirPilha();

    cout << endl;

    cout << pilha.quantidadeNode() << endl;

    return 0;
}