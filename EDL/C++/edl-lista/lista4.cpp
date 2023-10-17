#include <iostream>
using namespace std;

class Node{
public:
    int numero;
    Node* proximo;

    Node (int value) : numero(value), proximo(nullptr){};
};

class ListaEncadeada{
public:

    ListaEncadeada() : head(nullptr){};

    void adicionarElemento(int valor){
        Node* novoNode = new Node(valor);
        novoNode->proximo = head;
        head = novoNode;
    }

    void exibirLista(){
        Node* atual = head;
        while(atual != nullptr){
            cout << atual->numero;
            atual = atual->proximo;
        }
    }

    void inverterLista(){
        Node* anterior = nullptr;
        Node* atual = head;
        Node* proximo = nullptr;

        while(atual != nullptr){
            proximo = atual->proximo;
            atual->proximo = anterior;
            anterior = atual;
            atual = proximo;
        }
        head = anterior;
    }

private:
    Node* head;
};

int main() {
    ListaEncadeada lista;

    // Adicione alguns elementos à lista
    lista.adicionarElemento(10);
    lista.adicionarElemento(20);
    lista.adicionarElemento(30);
    lista.adicionarElemento(40);
    lista.adicionarElemento(50);

    // Exiba a lista original
    cout << "Lista Original: ";
    lista.exibirLista();
    cout << endl;

    // Inverta a lista
    lista.inverterLista();

    // Exiba a lista invertida
    cout << "Lista Invertida: ";
    lista.exibirLista();
    cout << endl;

    return 0;
}