#include <iostream>

using namespace std;

class Node {
    public:
        char letra;
        // duplamente encadeado
        Node* proximo; // A -> B -> C
        Node* anterior; // A <- B <- C

        Node(char letra) : letra(letra), proximo(nullptr), anterior(nullptr) {}
};

class Deque {
    public:
        int tamanho_deque;
        Node* head;
        Node* tail;

        Deque() : tamanho_deque(0), head(nullptr), tail(nullptr) {}

        Deque inic_deque() {
            Deque deque;
            tamanho_deque = 0;
            return deque;
        }

        void inserir_first(char letra) {
            Node* new_node = new Node(letra);
            
            if (tamanho_deque == 0) {

                head = new_node; // A
                tail = new_node; // A

            } else {

                head->anterior = new_node; // B <- A
                new_node->proximo = head; // B -> A

                head = new_node; // B
                tail = head->proximo; // A

            } 

            tamanho_deque++;
        }

        void inserir_last(char letra) {
            Node* new_node = new Node(letra);

             if (tamanho_deque == 0) {
                
                head = new_node; // A
                tail = new_node; // A

            } 
            else if (tamanho_deque == 1) {

                head->proximo = new_node; // A -> B
                new_node->anterior = head; // A <- B

                head = new_node->anterior; // A
                tail = new_node; // B

            }  
            else {
                
                tail->proximo = new_node; // B -> C
                new_node->anterior = tail; //B <- C

                tail = new_node; // C
            }

            tamanho_deque++;
        }

        void remover_first() {
            Node* node_removido;
            node_removido = head;

            head = head->proximo;

            delete node_removido;

            tamanho_deque--;
        }

        void remover_last() {
            Node* node_removido;
            node_removido = tail;

            tail = tail->anterior;

            delete node_removido;

            tamanho_deque--;
        }

    char first() {
        return head->letra;
    }      

    char last() {
        return tail->letra;
    }  

    int size() {
        return tamanho_deque;
    }

    bool is_empty() {
        if (tamanho_deque == 0) {
            return true;
        } 
        return false;
    }

    void imprimir(){
        Node* atual = head;
        while(atual != nullptr){
            cout << atual->letra << endl;
            atual = atual->proximo;
        }
    }

};

int main() {

    // Criar deque
    Deque deque;
    deque.inic_deque();

    // Está vazia?
    cout << "deque vazio? " << deque.is_empty() << endl;

    // Inserir no começo
    deque.inserir_first('E');
    deque.inserir_first('D');
    deque.inserir_first('C');

    // Inserir no final
    deque.inserir_last('W');

    deque.imprimir();
    cout << "\n\n";

    // Está vazia?
    cout << "deque vazio? " << deque.is_empty() << endl;

    cout << "---------------------- " << endl;

    cout << "tamanho do deque: " << deque.size() << endl;
    cout << "head: " << deque.first() << endl;
    cout << "tail: " << deque.last() << endl;

    cout << "-------- Mais insercoes ----------- " << endl;

    // Inserir no começo
    deque.inserir_first('B');

    // Inserir no final
    deque.inserir_last('X');
    deque.inserir_last('Y');

    deque.imprimir();
    cout << "\n\n";

    cout << "tamanho do deque: " << deque.size() << endl;
    cout << "head: " << deque.first() << endl;
    cout << "tail: " << deque.last() << endl;

    cout << "-------- Removendo ----------- " << endl;

    // Remover no começo
    deque.remover_first();

    // Remover no final
    deque.remover_last();

    deque.imprimir();
    cout << "\n\n";

    cout << "tamanho do deque: " << deque.size() << endl;
    cout << "head: " << deque.first() << endl;
    cout << "tail: " << deque.last() << endl;

    cout << "-------- Mais insercoes ----------- " << endl;

    // Inserir no começo
    deque.inserir_first('A');

    // Inserir no final
    deque.inserir_last('Z');

    deque.imprimir();
    cout << "\n\n";

    cout << "tamanho do deque: " << deque.size() << endl;
    cout << "head: " << deque.first() << endl;
    cout << "tail: " << deque.last() << endl;

    return 0;
}