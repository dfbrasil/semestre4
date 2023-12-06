#include <iostream>
using namespace std;

class Node{
public:
    int numero;
    Node* proximo;

    Node(int numero) : numero(numero) , proximo(nullptr){} //a) Constructor

    ~Node(){
        cout << " Destrutor para o nó: " << numero << endl; // k) Destrutor
    }
};

class Lista{
public:

    Lista() : head(nullptr), cont(0){}// a) Constructor

    void obterProximo(){ //b) Recebe como argumento um nó e retorna o próximo
        Node* atual = head;
        cout << "O próximo número após o head é: " << endl;
        cout << atual->proximo->numero << endl;
    }

    void obterValor(int posicao){ //c) Recebe como argumento um nó e retorna os valores armazenados dentro dele
        if ((posicao < 0) || (posicao > cont)){
            cout << "Posição de nó inválida!" << endl;
        }

        if (posicao == 0){
            cout << "O valor armazenado nessa posição é: " << head->numero << endl;
        }

        Node* atual = head;
        for (int i = 0; i < posicao - 1; i++){
            atual = atual->proximo;
        }
        cout << "O elemento na posição " << posicao << " é: " << atual->numero << endl;
    }

    void alterarNo (int numero, int posicao){ //d) Recebe como argumento um nó e dois interios para alterar as informações do nó referenciado
        if ((posicao < 0) || (posicao > cont)){
            cout << "Posição de nó inválido!";
        }

        if (posicao == 0){
            head->numero = numero;
            cout << "Novo valor de head é: " << head->numero << endl;
        }

        Node* atual = head;

        for (int i = 0; i < posicao -1; i++){
            atual = atual->proximo;
        }
        atual->numero = numero;

        cout << "O novo valor do nó na posição " << posicao << " é " << atual->numero << endl;
    }

    void tamanho(){ //e) Retorna o tamanho da lista
        cout << "O tamanho da lista é: " << cont << endl;
    }

    void existe(int numero){ //f) Retorna se um n ́o existe na lista

        if (head->numero == numero){
            cout << "O número está no head!";
        }
        else if (head->numero != numero){
            Node* atual = head;
            while(head->numero != numero){
                head = head->proximo;
                break;
            }
            if (head->numero == numero){
                cout << "O valor encontra-se na lista!" << endl;
            }
            else{
                cout << "O valor não encontra-se na lista!" << endl;
            }
        }
    }

    void inserir(int numero){ //i) Inserir um elemento na lista
        Node* novoNode = new Node(numero);
        novoNode->proximo = head;
        head = novoNode;
        cont++;
    }

    void excluir(int numero){ //j) Excluir um elemento da lista
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

    lista.obterProximo();

    lista.obterValor(2);

    lista.alterarNo(10, 2);

    lista.mostrarAll();

    lista.existe(11);

return 0;
}
