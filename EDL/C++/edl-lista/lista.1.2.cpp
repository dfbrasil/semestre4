#include <iostream>
using namespace std;

class Node{
public:
    int numero;
    Node* proximo;

    Node (int numero) : numero(numero), proximo(nullptr){};
};


class ListaEncadeada{
public:
    ListaEncadeada() : head(nullptr){};

    void inserirElemento(int numero){
        Node* novoNode = new Node(numero);
        novoNode->proximo = head;
        head = novoNode;
    }

    void imprimeLista(){
        Node* atual = head;
        while(atual != nullptr){
            cout << atual->numero;
            atual = atual->proximo;
        }
    }


 private:

 Node* head;

};

int main(){

    ListaEncadeada lista;

    lista.inserirElemento(4);
    lista.inserirElemento(3);
    lista.inserirElemento(2);

    lista.imprimeLista();

return 0;

}