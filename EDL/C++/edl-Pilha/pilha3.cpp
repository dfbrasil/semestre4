#include <iostream>
using namespace std;

class Node{
public:
    char letra;
    Node* proximo;

    Node(char letra) : letra(letra), proximo(nullptr){}
};

class Pilha{
public:
    Pilha() : head(nullptr){}

    void empilhar(string palavra){
        
        for (char letra : palavra){
            Node* novoNode = new Node(letra);
            novoNode->proximo = head;
            head = novoNode;
        }
    }

    void imprimir(){
        Node* atual = head;
        while (atual != nullptr){
            cout << atual->letra << endl;
            atual = atual->proximo;
        }
    }

    void desempilhar(){
        Node* temp = head;

        if (head == nullptr){
            cout << "Pilha vazia!";
        } else{
            head = head->proximo;
            delete temp;
        }
    }

    void primeiro(){
        Node* atual = head;
        if (atual == nullptr){
            cout << "Pilha vazia \n" << endl;
        } else{
            cout << head->letra << endl;
        }
    }

    void ultimo(){
        Node* atual = head;
        while(atual->proximo != nullptr){
            atual = atual->proximo;
        }
        cout << atual->letra << endl;
    }

private:
    Node* head;
};

int main() {

    Pilha pilha;

    pilha.empilhar("Daniel");
    pilha.imprimir();
    cout << "\n\n";
    pilha.desempilhar();
    pilha.imprimir();
    cout << "\n\n";
    pilha.primeiro();
    cout << "\n\n";
    pilha.ultimo();


}