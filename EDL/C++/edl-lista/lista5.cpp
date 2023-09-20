#include <iostream>
using namespace std;

class Node {
public:
    int numero;
    Node* proximo;

    Node(int numero) : numero(numero), proximo(nullptr) {};
};

class ListaEncadeada {
public:
    ListaEncadeada() : head(nullptr), tamanho(0) {};

    void adicionarElemento(int numero) {
        Node* novoNode = new Node(numero);
        novoNode->proximo = head;
        head = novoNode;
        tamanho++;
    }
    
    void exibirLista() {
        Node* atual = head;
        while(atual != nullptr) {
            cout << atual->numero << " ";
            atual = atual->proximo;
        }
        cout << endl;
    }

    void mostrarTamanho() {
        cout << "Tamanho da lista: " << tamanho << endl;
    }

    bool removerElemento(int valor) {
        if (head == nullptr) {
            cout << "A lista está vazia, não há o que remover" << endl;
            return false;
        }

        if (head->numero == valor) {
            Node* temp = head;
            head = head->proximo;
            delete temp;
            tamanho--;
            return true;
        } 
        
        Node* atual = head;
        while(atual->proximo != nullptr) {
            if (atual->proximo->numero == valor) {
                Node* temp = atual->proximo;
                atual->proximo = atual->proximo->proximo;
                delete temp;
                tamanho--;
                return true;
            }
            atual = atual->proximo;
        }
        cout << "Elemento não encontrado na lista" << endl;
        return false;
    }

    void inserirElemento(int valor, int posicao) {
        if (posicao < 0 || posicao > tamanho) {
            cout << "Posição inválida!" << endl;
            return;
        }

        Node* novoNode = new Node(valor);

        if (posicao == 0) {
            novoNode->proximo = head;
            head = novoNode;
            tamanho++;
            return;
        }

        Node* anterior = head;

        for (int i = 0; i < posicao - 1; i++) {
            anterior = anterior->proximo;
        }

        novoNode->proximo = anterior->proximo;
        anterior->proximo = novoNode;
        tamanho++;
    }
    
    int obterElemento(int posicao) {
        if (posicao >= tamanho || head == nullptr || posicao < 0) {
            cout << "Posição inválida!" << endl;
            return -1;
        }

        Node* atual = head;

        for (int i = 0; i < posicao; i++) {
            atual = atual->proximo;
        }
        return atual->numero;
    }

private:
    Node* head;
    int tamanho;
};

int main() {
    ListaEncadeada lista;

    lista.adicionarElemento(10);
    lista.adicionarElemento(20);
    lista.adicionarElemento(30);

    // Exiba a lista
    cout << "Lista: ";
    lista.exibirLista();
    cout << endl;
    lista.mostrarTamanho();
    cout << endl;
    lista.inserirElemento(12, 9); // Teste com posição inválida
    cout << endl;
    lista.exibirLista();
    cout << endl;
    lista.removerElemento(15); // Teste com elemento não encontrado
    cout << endl;
    lista.exibirLista();
    cout << endl;
    cout << lista.obterElemento(8); // Teste com posição inválida
    cout << endl;

    return 0;
}
