#include <iostream>
using namespace std;

class Node{
public:
    int numero;
    Node* proximo;

    Node(int numero) : numero(numero), proximo(nullptr){}
};

class Pilha{
public:

    Pilha(int tamMax) : head(nullptr), tamanhoMax(tamMax), cont(0){}


    void empilhar(int numero){
        Node* newNode = new Node(numero);
        if (cont < tamanhoMax){
            newNode->proximo = head;
            head = newNode;
            cont++;
        } else{
            cout << "Não é possivel mais empilhar, pilha no tamanho máximo \n"<< endl;
        }
    }

    void desempilhar(){
        Node* atual = head;
        if (atual == nullptr){
            cout << "Pilha vazia!\n" << endl;
        } else{
            Node* temp = head;
            head = head->proximo;
            delete temp;
            cont--;
        }
    }

    void topo(){
        Node* atual = head;
        if (atual == nullptr){
            cout << "Pilha vazia\n" << endl;
        } else{
            cout << atual->numero << endl;
        }
    }

    void vazia(){
        if (head==nullptr){
            cout << "Pilha vazia!\n" << endl;
        } else{
            cout << "Pilha não vazia! \n" << endl;
        }
    }

    void cheia(){
       if (cont < tamanhoMax){
        cout << "Pilha ainda não está cheia \n" << endl;
       } else {
        cout << "Pilha cheia \n" << endl;
       }
    }

private:
    Node* head;
    int tamanhoMax;
    int cont;
};

int main(){

    Pilha pilha(3);

    pilha.empilhar(10);
    pilha.empilhar(20);
    pilha.empilhar(30);
    pilha.empilhar(40);
    pilha.cheia();
    pilha.vazia();
    pilha.topo();
    pilha.desempilhar();
    pilha.topo();

    return 0;
}