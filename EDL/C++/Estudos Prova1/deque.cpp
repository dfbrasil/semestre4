#include <iostream>
using namespace std;

class Node{
public:
    int numero;
    Node* proximo;

    Node(int numero) : numero(numero), proximo(nullptr){}
};

class Deque{
public:
    Deque() : head(nullptr), last(nullptr), cont(0){}

    void inserir_first(int numero){
        Node* newNode = new Node(numero);
        if (head == nullptr){
            head = last = newNode;
            cont++;
        } else {
            newNode->proximo = head;
            head = newNode;
            cont++;
        }
    }

    void inserir_last(int numero){
        Node* newNode = new Node(numero);
        if (head == nullptr){
            head = last = newNode;
            cont++;
        } else {
            last->proximo = newNode;
            last = newNode;
            cont++;
        }
    }

    void remover_first(){
        Node *temp = head;
        head = head->proximo;
        delete temp;
        cont--;
    }   

    void remover_last(){
        Node* atual = head;
        while(atual->proximo != nullptr){
            atual = atual->proximo;
        }
        delete atual;
        cont--;
    }   

    void primeiro(){
        Node* atual = head;
        cout << atual->numero << endl;
    }

    void ultimo(){
        Node* atual = head;
        while(atual->proximo != nullptr){
            atual = atual->proximo;
        }
        cout << "O último elemento da fila é: " << atual->numero << endl;
    }

    void destruir(){
        Node* atual = head;
        while (atual != nullptr){
            Node* next = atual->proximo;
            delete atual;
            atual = next;
        }
        head = nullptr;
        last = nullptr;
        cont = 0;
    }

    void imprimir(){
        Node* atual = head;
        while(atual != nullptr){
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

    deque.inserir_first(1);
    deque.inserir_first(2);
    deque.inserir_first(3);
    deque.inserir_first(4);
    deque.inserir_last(5);
    deque.inserir_last(6);
    deque.inserir_last(7);

    deque.imprimir();

return 0;
}