#include <iostream>
using namespace std;

class Node{
public:
    int numero;
    Node* proximo;

    Node(int numero) : numero(numero) , proximo(nullptr){} //Constructor

    ~Node(){
        cout << " Destrutor para o nó: " << numero << endl; //Destrutor
    }
};

class Lista{
public:

    Lista() : head(nullptr), cont(0){}//Constructor

    void inserir(int numero){ //i) Inserir um elemento na lista
        Node* novoNode = new Node(numero);
        novoNode->proximo = head;
        head = novoNode;
        cont++;
    }

    void excluir(int numero){ //Excluir um elemento da lista
        if (head == nullptr){
            cout << "A lista já encontra-se vazia!" << endl;
        }

        if(head->numero == numero){
            Node* temp = head;
            head = head->proximo;
            delete temp;
            cont--;
        }

        else if (head->numero != numero){
            Node* atual = head;
                while( atual->proximo != nullptr){
                    if(atual->proximo->numero == numero){
                        Node* temp = atual->proximo;
                        atual->proximo = atual->proximo->proximo;
                        delete temp;
                        cont--;
                    }
                    atual = atual->proximo;   
                }
        }
        else{
            cout << "O número não encontra-se na lista!" << endl;
        }
    }

    void mostrarAll(){ //g) Retornar todos os elementos da lista
        Node* atual = head;
        if (head == nullptr){
            cout << "Lista vazia!";
        }
        
        while (atual != nullptr){
            cout << atual->numero << endl;
            atual = atual->proximo;
        }
    }

    void tamanho(){
        cout << "O tamanho da lista é: " << cont << endl;
    }



private:
    Node* head;
    int cont;
};

int main() {

    Lista lista;
    int numero, deletar;

    while (numero >= 0){
        cout << "Digite um número para inserir na lista: " << endl;
        cin >> numero;
        if (numero <0 ){
            break;
        }
        lista.inserir(numero);
    }
    lista.mostrarAll();

    lista.tamanho();

    cout << "Digite um número para excluir da lista: " << endl;
    cin >> deletar;
    lista.excluir(deletar);

    lista.mostrarAll();

    lista.tamanho();

return 0;
}