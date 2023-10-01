#include <iostream>
using namespace std;

class Node{
public:

 int numero;
 Node* proximo;

 Node(int numero) : numero(numero), proximo(nullptr){}
};

class Pilha{
public: 

    Pilha() : head(nullptr), cont(0){}

    void empilhar(int numero){
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

  void inverter() {
    if (head == nullptr || head->proximo == nullptr) {
        // Lista vazia ou com apenas um elemento, nada a inverter
        return;
    }

    Node* prevNode = nullptr;
    Node* currentNode = head;
    Node* nextNode = nullptr;

    while (currentNode != nullptr) {
        nextNode = currentNode->proximo;
        currentNode->proximo = prevNode;
        prevNode = currentNode;
        currentNode = nextNode;
    }

    head = prevNode;
}

    void imprimeInvert(){
        Node* newNode = head;
        while (newNode != nullptr){
            cout << newNode->numero << endl;
            newNode = newNode->proximo;
        }
    }

private:
    Node* head;
    int cont;
};

int main() {

    Pilha pilha;

    pilha.empilhar(3);
    pilha.empilhar(2);
    pilha.empilhar(1);

    pilha.imprimir();

    pilha.inverter();

    pilha.imprimeInvert();

return 0;

}