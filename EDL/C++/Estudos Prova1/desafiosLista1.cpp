// Crie duas classes denominadas nó e Lista. Na classe nó deverá ter dois atributos do tipo
// inteiro e mais um ponteiro para o próximo nó. A classe Lista deverá ter os seguintes métodos
// públicos: (A lista deverá ser ordenada pelo primeiro atributo do nó)
// (a) Construtor - Inicializa a classe
// (b) ObterProximo - Recebe como argumento um nó e retorna o próximo
// (c) ObterValor - Recebe como argumento um nó e retorna os valores armazenados dentro
// dele
// (d) AlterarNo - Recebe como argumento um nó e dois interios para alterar as informações
// do nó referenciado
// (e) Tamanho - Retorna o tamanho da lista OK
// (f) Existe - Retorna se um nó existe na lista
// (g) mostrarALL - Retorna todos os elementos da lista
// (h) Buscar - Retorna se o nó contém na lista
// (i) Inserir - Insere um elemento na lista
// (j) Excluir - Exclui um elemento da lista
// (k) Destrutor - Destrói um nó

#include <iostream>
using namespace std;

class Node{
public:

    int numero;
    Node* proximo;

    Node(int numero) : numero(numero), proximo(nullptr){}
};

class Lista{
public:

    Lista() : head(nullptr), last(nullptr), cont(0){}

    void inserir(int numero){
        Node* newNode = new Node(numero);
        if (head == nullptr){
            head = last = newNode;
            cont++;
        }
        else{
            last->proximo = newNode;
            last = newNode;
            cont++;
        }
    }

    void imprimir(){
        Node* atual = head;
        if (head == nullptr){
            cout << "Lista vazia! " << endl;
        }
        while(atual != nullptr){
            cout << atual->numero << endl;
            atual = atual->proximo;
        }
    }

    void tamanho(){
        cout << "A lista possui " << cont << " elementos." << endl;
    }

    void existe(int numero){
        bool achou = false;
        Node* atual = head;
        while(atual != nullptr){
            if (atual->numero == numero){
                cout << "O número encontra-se na lista." << endl;
                achou = true;
            }
            atual = atual->proximo;
        }
        if (achou == false){
            cout << "Não achou !" << endl;
        }
    }

    void alterar(int posicao, int novoValor){
        Node* atual = head;
 
        if( posicao > cont){
            cout << "posição solicitada inválida!" << endl;
        }
        else{
            for (int i = 0; i < posicao; i++){
            atual = atual->proximo;
            }
            atual->numero = novoValor;
        }
    }

private:
    Node* head;
    Node* last;
    int cont;
};

int main(){

    Lista lista;

    lista.inserir(10);
    lista.inserir(20);
    lista.inserir(30);

    lista.imprimir();

    lista.tamanho();

    lista.existe(40);

    lista.alterar(2,50);

     lista.imprimir();

return 0;
}