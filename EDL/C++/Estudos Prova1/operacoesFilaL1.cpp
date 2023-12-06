// • Criar uma Fila
// • Inserir elemento (push)
// • Retirar elemento (pop)
// • Tamanho da fila(size)
// • head da Fila (front)
// • Último da Fila (back)
// • Destruir a fila.

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

    Fila() : head(nullptr), last(nullptr), cont(0){}

    void inserir(int numero){
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

    void imprimir(){
        Node* atual = head;
        while(atual != nullptr){
            cout << atual->numero << endl;
            atual = atual->proximo;
        }
    }

    void remover(){
        Node *temp = head;
        head = head->proximo;
        delete temp;
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
    }

    void removerRepetidos() {
    if (head == nullptr || head->proximo == nullptr) {
        return;
    }

    Node* atual = head;

    while (atual != nullptr) {
        Node* comparador = atual;
        while (comparador->proximo != nullptr) {
            if (comparador->proximo->numero == atual->numero) {
                // Elemento repetido encontrado, remova-o.
                Node* temp = comparador->proximo;
                comparador->proximo = temp->proximo;
                delete temp;
                cont--;
            } else {
                comparador = comparador->proximo;
            }
        }
        atual = atual->proximo;
    }
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
    fila.inserir(4);

    fila.imprimir();

    fila.remover();

    fila.imprimir();

    fila.primeiro();

    fila.ultimo();

    fila.removerRepetidos();
    fila.imprimir();


    return 0;
}