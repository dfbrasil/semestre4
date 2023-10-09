#include <iostream>
using namespace std;

class Node{
public: 
    int numero;
    Node* proximo;

    Node(int numero) : numero(numero), proximo(nullptr){}
};

class Fila{
public:

    Fila() : head(nullptr), back(nullptr), cont(0){}

    void inserir(int numero){
        Node* newNode = new Node(numero);
        if (head == nullptr){
            head = back = newNode;
            cont++;
        }
        else {
            back->proximo = newNode;
            back = newNode;
            cont++;
        }
    }

    void imprimir(){
        Node* atual = head;
        if(head==nullptr){
            cout << "A fila está vazia!" << endl;
        }
        while(atual != nullptr){
            cout << atual->numero << endl;
            atual = atual->proximo;
        }
    }

    void remover(){
        if (head == nullptr){
            cout << "Fila vazia !\n" << endl;
        } else{
            Node* temp = head;
            head = head->proximo;
            delete temp;
            cont--;
        }
    }

    void tamanho(){
        cout << "O tamanho da fila é: " << cont << endl;
    }

    void primeiro(){
        cout << "No momento o primeiro da fila é: " << head->numero << endl;
    }

    void ultimo(){
        Node* atual = head;
        while(atual->proximo != nullptr){
            atual = atual->proximo;
        }
        cout << "No momento o ultimo da fila é: " << atual->numero << endl;
    }

    void destruir(){
        head=back=nullptr;
    }

private:
    Node* head;
    Node* back;
    int cont;
};

int main() {

    Fila fila;

    fila.inserir(10);
    fila.inserir(20);
    fila.inserir(30);
    fila.inserir(40);
    fila.primeiro();
    fila.ultimo();

    fila.imprimir();
    cout << "\n\n";
    fila.remover();
    fila.imprimir();
    fila.inserir(50);
    cout << "\n\n";
    fila.imprimir();
    fila.primeiro();
    fila.ultimo();
    fila.destruir();
    cout << "\n\n";
    fila.imprimir();

    return 0;
}