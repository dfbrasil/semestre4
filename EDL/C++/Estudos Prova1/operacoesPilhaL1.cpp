// • Operações com Pilha:
// • criação da pilha;
// • empilhar (push) - o elemento é o parâmetro nesta operação;
// • desempilhar (pop);
// • mostrar o topo;
// • verificar se a pilha está vazia (isEmpty);
// • verificar se a pilha está cheia (isFull).

#include <iostream>
using namespace std;

class Node{
public:
    int numero;
    Node* proximo;

    Node (int numero) : numero(numero) , proximo(nullptr){}
};

class Pilha{
public:

    Pilha() : head(nullptr), cont(0){}

    void empilhar(int numero){
        Node* newNode = new Node(numero);
        newNode->proximo = head;
        head = newNode;
        cont++;
    }

    void desempilhar(){
        if (head == nullptr){
            cout << "Pilha vazia" << endl;
        }
        if (head != nullptr){
            Node* temp = head;
            cout << "deletando o nó com elemento: " << head->numero << endl;
            head =head->proximo;
            delete temp;
            cont--;
        }
    }

private:
    Node* head;
    int cont;
};

int main(){

    Pilha pilha;

    pilha.empilhar(1);
    pilha.empilhar(2);
    pilha.empilhar(3);

    pilha.desempilhar();
    pilha.desempilhar();
    pilha.desempilhar();
    pilha.desempilhar();
    pilha.desempilhar();



    return 0;
}
