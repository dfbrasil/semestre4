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
    Pilha() : head(nullptr), cont(0){};

    void empilhar(int numero){
        Node* novoNode = new Node(numero);
        novoNode->proximo = head;
        head = novoNode;
        cont++;
    }

    void desempilhar(){
        if (head == nullptr){
            cout << "A pilha já está vazia!" << endl;
        }
        Node* temp = head;
        head = head->proximo;
        delete temp;
        cont--;
    }

    int topo(){
        if (head == nullptr){
            cout << "Pilha vazia! " << endl;
        }
        Node* top = head;
        return top->numero;
    }

private:
    Node* head;
    int cont;

};

int main() {
    Pilha pilha;

    pilha.empilhar(10);
    pilha.empilhar(20);
    pilha.empilhar(30);

    cout << "Topo da pilha: " << pilha.topo() << endl; // Deve imprimir "Topo da pilha: 30"

    pilha.desempilhar();

    cout << "Topo da pilha após desempilhar: " << pilha.topo() << endl; // Deve imprimir "Topo da pilha após desempilhar: 20"

    pilha.desempilhar();
    pilha.desempilhar();

    cout << "Topo da pilha após desempilhar tudo: " << pilha.topo() << endl; // Deve imprimir "Topo da pilha após desempilhar tudo: 0"

    return 0;
}