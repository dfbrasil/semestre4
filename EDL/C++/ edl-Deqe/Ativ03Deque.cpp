#include <iostream>
using namespace std;

class Node{
public:
    int numero;
    Node* proximo;
    Node* anterior;

    Node(int numero) : numero(numero), proximo(nullptr), anterior(nullptr){}
};

class Deque{
public:

    Deque() : head(nullptr), tail(nullptr), cont(0){}

    void inserir_inicio(int numero){
        Node* newNode = new Node(numero);

        if (head == nullptr){
            head = tail = newNode;
        } else if (cont == 1){
            head->anterior = newNode;
            newNode->proximo = head;
            head = newNode;
            tail = head->proximo;
        } else {
            head->anterior = newNode;
            newNode->proximo = head;
            head = newNode;
        }
        cont++;
    }

    void inserir_final(int numero) {
        Node* newNode = new Node(numero);
        if (head == nullptr) {
            head = tail = newNode;
        } else {
            newNode->anterior = tail;
            tail->proximo = newNode;
            tail = newNode;
        }
        cont++;
    }

    void imprimir(){
        Node* atual = head;
        while (head != tail ){
            cout << atual->numero << endl;
            atual = atual->proximo;
            if(atual == nullptr){
                atual = tail;
                break;
            }
        }
    }

private:
    Node* head;
    Node* tail;
    int cont;
};

int main(){

    Deque deque;

    deque.inserir_inicio(10);
    deque.inserir_inicio(20);
    deque.inserir_inicio(30);
    deque.inserir_final(44);
    deque.inserir_inicio(55);

    deque.imprimir();
    cout << "\n\n";

return 0;
}