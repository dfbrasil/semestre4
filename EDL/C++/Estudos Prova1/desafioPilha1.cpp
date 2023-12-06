// Escreva um programa que leia um inteiro n e uma sequência de n números inteiros e positivos e imprima primeiro os números impares na ordem inversa da leitura e, depois, os números pares também na ordem inversa da leitura. (Use duas pilhas ? uma para armazenar os números impares e outra para armazenar os números pares.)

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

    Pilha() : headPar(nullptr), headImpar(nullptr), lastPar(nullptr), lastImpar(nullptr), cont(0){}

    void empilhar(int numero){
        Node* newNode = new Node(numero);

        if ( numero % 2 == 0 && headPar == nullptr ){
            headPar = lastPar = newNode;
        }

        if ( numero % 2 == 0 && headPar != nullptr ){
            lastPar->proximo = newNode;
            lastPar = newNode;
        }

        if ( numero % 2 != 0 && headImpar == nullptr ){    
            headImpar = lastImpar = newNode;
        }

        if ( numero % 2 != 0 && headImpar != nullptr){
            lastImpar->proximo = newNode;
            lastImpar = newNode;
        }      
    }

    void imprimir(){
        Node* atualImpar = headImpar;
        if (atualImpar == nullptr){
            cout << "Pilha Impar vazia" << endl;
        }
        while (atualImpar != nullptr){
            cout << atualImpar->numero << endl;
            atualImpar = atualImpar->proximo;
        }

        Node* atualPar = headPar;

        if (atualPar == nullptr){
            cout << "Pilha Par Vazia! " << endl;
        }
        else{
            while(atualPar != nullptr){
                cout << atualPar->numero << endl;
                atualPar = atualPar->proximo;
            }
        }
    }

private:
    Node* headPar;
    Node* headImpar;
    Node* lastPar;
    Node* lastImpar;
    int cont;
};

int main(){

    Pilha pilha;

    // pilha.empilhar(1);
    pilha.empilhar(2);
    // pilha.empilhar(3);
    pilha.empilhar(4);

    pilha.imprimir();
return 0;

}