#include <iostream>
using namespace std;

class Node{
public: 

    int numero;
    Node* proximo;

    Node(int numero) : numero(numero) , proximo(nullptr){}
};

class Fila{
public:

    Fila() : head(nullptr), last(nullptr), cont(0){}

    void inserir(int numero){
        Node* novoNode  = new Node(numero);
        if (head == nullptr){
            head = last = novoNode;
            cont++;
        }
        else{
            last->proximo = novoNode;
            last = novoNode;
            cont++;
        }
    }

    void imprimir(){
        Node* atual = head;
        if (atual == nullptr){
            cout << "Fila vazia" << endl;
        }
        else{
            while (atual != nullptr){
                cout << atual->numero << endl;
                atual = atual->proximo;
            }
        }
    }

    void excluir(){
        Node* temp = head;
        temp = head;
        head = head->proximo;
        delete temp;
        cont--;
    }

    void ultimo(){
        Node* atual = head;
        while (atual->proximo != nullptr){
            atual = atual->proximo;
        }
        cout << "ultimo: " << atual->numero << endl;
    }

private:
    Node* head;
    Node* last;
    int cont;
};

int main(){

    Fila fila;


    fila.inserir(1);
    fila.inserir(2);
    fila.inserir(3);
    fila.inserir(4);

    fila.imprimir();

    fila.excluir();

    fila.imprimir();

    fila.excluir();

    fila.imprimir();

    fila.ultimo();

    return 0;
}