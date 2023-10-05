#include <iostream>
using namespace std;

class Node{
public:

    int numero;
    Node* proximo;
    Node* anterior;

    Node(int numero) : numero(numero), proximo(nullptr){}
};

class Deque{
public:

    Deque() : head(nullptr), last(nullptr), cont(0){}
    
    void inserir_inicio(int numero){
        Node* newNode = new Node(numero);
        if (head == nullptr){
            head = last = newNode;
            cont++;
        }
        else{
            newNode->proximo = head;
            head->anterior = newNode;
            head = newNode;
            cont++;
        }
    }

    void inserir_fim (int numero){
        Node* newNode = new Node(numero);
        if (head == nullptr){
            head = last = newNode;
            cont++;
        }
        else{
            newNode->anterior = last;
            last->proximo = newNode;
            last = newNode;
            cont++;
        }
    }

    void remover_inicio(){
        Node* temp = head;
        head->proximo->anterior = nullptr;
        delete temp;
        cont--;
    }

    void remover_final(){
        Node* atual = last;
        last->anterior->proximo = nullptr;
        delete atual;
        cont--;
    }

    void imprimir(){
        Node* atual = head;
        while (atual != nullptr){
            cout << atual->numero << endl;
            atual = atual->proximo;
        }
    }

private:
    Node* head;
    Node* last;
    int cont;
};

int main(){

    Deque deque;

    deque.inserir_inicio(1);
    deque.inserir_inicio(2);
    deque.inserir_inicio(3);
    deque.inserir_inicio(4);
    deque.inserir_fim(5);
    deque.inserir_fim(6);
    deque.inserir_fim(7);

    deque.imprimir();


    // deque.remover_inicio();

    cout << endl;

    deque.imprimir();

    deque.remover_final();

    cout << endl;

    deque.imprimir();



return 0;
}