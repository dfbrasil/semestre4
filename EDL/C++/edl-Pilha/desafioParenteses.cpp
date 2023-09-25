#include <iostream>
using namespace std;


class Node{
public:
    char caractere;
    Node* proximo;

    Node(char caractere) : caractere(caractere) , proximo(nullptr) {}
};

class Expressao{
public:

    Expressao() : head(nullptr){}
    
    void empilhar(char caractere){
        Node* novoNode = new Node(caractere);
        if(caractere == '('){
            novoNode->proximo = head;
            head = novoNode;
        } else if (caractere == ')') {
            if (head && head->caractere == '(') {
                desempilhar();
            } else {
                cout << "expressão errada" << endl;
                return;
            }
        }
    }

    void desempilhar() {
        if (head) {
            Node* temp = head;
            head = head->proximo;
            delete temp;
        } else {
            cout << "expressão errada" << endl;
        }
    }

    void verifica(){
        if (head == nullptr){
            cout << "expressão correta" << endl;
        }
        else{
            cout << "expressão errada" << endl;
        }
    }

private:
    Node* head;
};

int main() {

    Expressao exp;

    char caractere;

    while(caractere != 'q'){
        cout << "digite um caractere" << endl;
        cin >> caractere;
        exp.empilhar(caractere);
    }

    exp.verifica();
}
