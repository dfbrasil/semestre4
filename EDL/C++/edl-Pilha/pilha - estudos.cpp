#include <iostream>
using namespace std;

class Elemento{ //define uma classe chamada Elemento
    private:
        int valor;
        Elemento* proximo; //proximo é do tipo ponteiro de Elemento. No código ele vai apontar para o próximo elemento da pilha.
                           //é um ponteiro para outro objeto Elemento, no caso próximo.
    public:
        Elemento(int valor) : valor(valor), proximo(nullptr){}
        // Este é o construtor da classe Elemento. Ele é usado para criar objetos Elemento. O construtor recebe um valor inteiro como argumento e inicializa os membros valor e proximo. O membro valor é inicializado com o valor passado como argumento, e o membro proximo é inicializado como nulo (nullptr).

        int get_valor(){
            return valor
        }
        // int get_valor() { return valor; }: Este é um método público que permite recuperar o valor armazenado no objeto Elemento. Ele simplesmente retorna o valor

        Elemento* get_proximo(){
            return proximo
        }
        // Elemento* get_proximo() { return proximo; }: Este é um método público que permite acessar o próximo elemento na lista encadeada. Ele retorna um ponteiro para o próximo elemento.

        void set_ptr(Elemento* objeto_do_elemento_para_apontar){// objeto_do_elemento_para_apontar é p parâmetro que vai receber o proximo ponteiro
            // referência a um objeto da classe Elemento que você deseja definir como o próximo elemento na lista encadeada
            this->proximo = objeto_do_elemento_para_apontar;
        };
        // está estabelecendo uma conexão entre o objeto atual (no qual o método set_ptr foi chamado) e o objeto objeto_do_elemento_para_apontar, tornando-o o próximo elemento na lista encadeada.

        // void set_ptr(Elemento* objeto_do_elemento_para_apontar) define o próximo elemento na lista encadeada, estabelecendo uma conexão entre o objeto atual (no qual a função é chamada) e o próximo elemento na sequência.
};

class Pilha{
    int tamanho_da_pilha;

    Elemento* elemento_topo;

    public:

        Pilha() : elemento_topo(nullptr) {}

        Pilha criar_pilha(){
            Pilha new_pilha;
            
            tamanho_da_pilha = 0;

            return new_pilha;
        }

        void empilhar_elemento(int valor){
            Elemento* novo_elemento = new Elemento(valor);

            novo_elemento->set_ptr(elemento_topo);

            elemento_topo = novo_elemento;

            tamanho_da_pilha++; 
        };

        
}
