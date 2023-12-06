#include <iostream>

using namespace std;

class Elemento{
    private:
        int valor;
        Elemento* proximo; // vai apontar para o elemento de baixo ( (topo)A -> B -> C)

    public:
        Elemento(int valor) : valor(valor), proximo(nullptr) {}

        int get_valor() { 
            return valor;
        }

        Elemento* get_proximo(){
            return proximo;
        }

        void set_ptr(Elemento* objeto_do_elemento_para_apontar) {
            this->proximo = objeto_do_elemento_para_apontar;
        };
};

class Pilha {
    int tamanho_da_pilha;

    /* ponteiro que pega o endereço do novo_elemento criado
   ao criar um novo elemento, aponto esse ponteiro para o novo endereço */
   Elemento* elemento_topo;

    public:
        
        Pilha() : elemento_topo(nullptr) {}

        Pilha criar_pilha() {
            Pilha new_pilha;

            tamanho_da_pilha = 0;
            
            return new_pilha;
        }

        void empilhar_elemento(int valor) {

            // alocando dinamicamente um novo elemento
            Elemento* novo_elemento = new Elemento(valor);

            // aponto o ponteiro do novo_elemento para o elemento_topo aponta
            // logo, em novo_elemento, vou ter acesso ao objeto que elemento_topo aponta 
            novo_elemento->set_ptr(elemento_topo);

            // atualizando, agora o elemento_topo será o objeto que novo_elemento aponta
            elemento_topo = novo_elemento;

            tamanho_da_pilha += 1;
        };

        void desempilhar_pilha() {
            if (elemento_topo != nullptr) {
                Elemento* elemento_removido;
                // aponto o ponteiro do elemento_removido para o elemento_topo aponta
                // logo, em elem_removido, vou ter acesso ao objeto que elemento_topo aponta 
                elemento_removido = elemento_topo;

                // atualizando, agora o elemento_topo apontará para o objeto proximo dele
                elemento_topo = elemento_topo->get_proximo();

                delete elemento_removido;

                tamanho_da_pilha -= 1;
            }
        }

        int recuperar_tamanho_da_pilha() {
            if (elemento_topo != nullptr) {
                return tamanho_da_pilha; 
            } else {
                return 0; // pilha vazia
            }
        }

        void deletar_pilha() {
            while (tamanho_da_pilha > 0) {
                desempilhar_pilha();
            }
        }

        int recuperar_elemento_topo_da_pilha() {
            if (elemento_topo != nullptr) {
                return elemento_topo->get_valor();
            }
        }
};

int main()
{

    Pilha pilha;
    // Cria a pilha
    pilha.criar_pilha();

    // Empilha alguns elementos
    pilha.empilhar_elemento(12);
    pilha.empilhar_elemento(14);
    pilha.empilhar_elemento(16);

    // Recupera o valor do topo
    cout << "Topo: " << pilha.recuperar_elemento_topo_da_pilha() << endl;

    // Desempilha um elemento
    pilha.desempilhar_pilha();

    // Recupera o tamanho da pilha e o valor do topo novamente
    cout << "Tamanho da pilha: " << pilha.recuperar_tamanho_da_pilha() << endl;
    cout << "Topo: " << pilha.recuperar_elemento_topo_da_pilha() << endl;

    // Empilha mais elementos
    pilha.empilhar_elemento(18);
    pilha.empilhar_elemento(20);

    // Desempilha novamente
    pilha.desempilhar_pilha();

    // Recupera o tamanho e o valor do topo
    cout << "Tamanho da pilha: " << pilha.recuperar_tamanho_da_pilha() << endl;
    cout << "Topo: " << pilha.recuperar_elemento_topo_da_pilha() << endl;

    cout << "\n-------Empilhando mais alguns-------\n " << endl;

    // Empilha mais elementos
    pilha.empilhar_elemento(22);
    pilha.empilhar_elemento(24);
    pilha.empilhar_elemento(26);

    // Desempilha um elemento
    pilha.desempilhar_pilha();

    // Recupera o tamanho e o valor do topo
    cout << "Tamanho da pilha: " << pilha.recuperar_tamanho_da_pilha() << endl;
    cout << "Topo: " << pilha.recuperar_elemento_topo_da_pilha() << endl;

    cout << "\n-------Destruindo pilha-------\n " << endl;

    // Destruindo a pilha
    pilha.deletar_pilha();

    cout << "Tamanho da pilha: " << pilha.recuperar_tamanho_da_pilha() << endl;

    return 0;
}