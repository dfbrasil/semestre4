
#include <iostream>
using namespace std;

class Node{
public:

    char letra;
    Node* proximo;

    Node(char letra) : letra(letra) , proximo(nullptr){}
};

class Pilha{
public:

    Pilha() : head(nullptr){}

    void inverte(string palavra){

        string expression = palavra;

        for (char caractere : expression){
            Node* newNode = new Node(caractere); 
            newNode->proximo = head;
            head = newNode;
        }
    }

    void imprime(){
        Node* atual = head;
        while (atual != nullptr){
            cout << atual->letra << endl;
            atual = atual->proximo;
        }
    }

private:
    Node* head;
};


int main(){

    string expression = "Daniel";

    Pilha pilha;

    pilha.inverte(expression);

    pilha.imprime();

    return 0;
}