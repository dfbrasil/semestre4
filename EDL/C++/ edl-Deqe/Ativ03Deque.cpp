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
        } else {
            head->anterior = newNode;
            newNode->proximo = head;
            head = newNode;
        }
        cont++;
    }

    void inserir_final(int numero){
        Node* newNode = new Node(numero);
        if (head == nullptr){
            head = tail = newNode;
        } else {
            tail->proximo = newNode;
            newNode->anterior = tail;
            tail = newNode;
        }
        cont ++;
    }

    void remover_inicio(){
        if (cont == 1){
            head=tail=nullptr;
        } else {
             Node* temp = head;
            head = head->proximo;
            head->anterior=nullptr;
            delete temp;
            cont--;
        }
       
    }

    void remover_final(){
        if (cont == 1){
            head=tail=nullptr;
        } else if(tail != nullptr){
            Node* temp = tail;
            tail = tail->anterior;
            tail->proximo = nullptr;
            delete temp;
        }
        cont--;
    }

    void imprimir(){
        Node* atual = head;
        while (atual != nullptr ){
            cout << atual->numero << endl;
            atual = atual->proximo;
        }
    }

    int first(){
        return head->numero;
    }

    int last(){
        return tail->numero;
    }

    int tamanho(){
        return cont;
    }

    bool isEmpty(){
        if (cont == 0){
            return true;
        }
        else {
            return false;
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
    deque.inserir_final(66);
    deque.imprimir();
    cout << "\n\n";

    deque.remover_inicio();
    deque.imprimir();
    cout << "\n\n";

    deque.remover_final();
    deque.imprimir();
    cout << "\n\n";

    cout << deque.first();
    cout << "\n";

    cout << deque.last() << endl;

    cout << deque.tamanho() << endl;

    cout << deque.isEmpty() << endl;

return 0;
}