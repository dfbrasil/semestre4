#include<iostream>
using namespace std;

class Node{
public:
    int numero;
    Node* proximo;

    Node(int numero) : numero(numero), proximo(nullptr){}
};

class Pilha{
public:

    Pilha() : headPar(nullptr), headImpar(nullptr), qtdPar(0), qtdImpar(0){}

    void empilhar(int numero){
        Node* nodePar = new Node(numero);
        Node* nodeImpar = new Node(numero);

        if (numero%2 == 0){
            nodePar->proximo = headPar;
            headPar = nodePar;
            qtdPar++;
        }
        else{
            nodeImpar->proximo = headImpar;
            headImpar = nodeImpar;
            qtdImpar++;
        }
    }

    void imprimir(){
        cout << "pares:" << endl;
        Node* atualPar = headPar;
        Node* atualImpar = headImpar;
        if (atualPar == nullptr){
            cout << "pilha de pares vazia";
        }
        else{
            while (atualPar != nullptr){
            cout << atualPar->numero << endl;
            atualPar = atualPar->proximo;
            } 
        }

        cout << "impares:" << endl;
       
        if (atualImpar == nullptr){
            cout << "pilha impar vazia";
        }
        else {
            while(atualImpar != nullptr){
                cout << atualImpar->numero << endl;
                atualImpar = atualImpar->proximo;
            }
        }
    }

        
private:
    int numero;
    Node* headPar;
    Node* headImpar;
    int qtdPar;
    int qtdImpar;
};


int main(){

    Pilha pilha;

    pilha.empilhar(4);
    pilha.empilhar(9);
    pilha.empilhar(6);
    pilha.empilhar(7);
    pilha.empilhar(5);
    pilha.empilhar(10);

    pilha.imprimir();

}