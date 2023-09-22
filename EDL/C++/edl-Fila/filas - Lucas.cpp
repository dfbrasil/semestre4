#include <iostream>

using namespace std;

class Elemento {
    private:
        string nome;
        Elemento* proximo; // vai apontar para o elemento de trás( A -> B -> C)
    public:
        Elemento(string nome) : nome(nome), proximo(nullptr) {}

        string get_nome() {
            return nome;
        }

        Elemento* get_proximo() {
            return proximo;
        }

        void set_proximo(Elemento* novo_proximo) {
            this->proximo = novo_proximo;
        }
};

class Fila {
    int tamanho_da_fila;

    Elemento* elemento_head_fila;
    Elemento* elemento_tail_fila;

    public: 
        Fila() : elemento_head_fila(nullptr), elemento_tail_fila(nullptr){}

        Fila criar_fila() {
            Fila new_fila;

            tamanho_da_fila = 0;
            
            return new_fila;
        }

        void enfileirar_um_elemento(string nome) {
            Elemento* novo_elemento = new Elemento(nome);

            if (tamanho_da_fila == 0) {

                elemento_head_fila = novo_elemento;
                elemento_tail_fila = novo_elemento;

            }  else {
                // aponta o ponteiro do último para o que está chegando
                elemento_tail_fila->set_proximo(novo_elemento);

                //atualiza o ponteiro para o último da fila
                elemento_tail_fila = novo_elemento;
            }

            tamanho_da_fila += 1;
        }

        void desenfileirar_o_primeiro_elemento() {
            if (tamanho_da_fila > 0) {
                Elemento* elemento_removido;
                 // aponto o ponteiro do elemento_removido para o ponteiro elemento_head_fila 
                // logo, em elem_removido, vou ter acesso ao objeto q elemento_head_fila aponta 
                elemento_removido =  elemento_head_fila;

                // atualizando, agora o elemento_head apontará para o objeto anterior dele
                elemento_head_fila = elemento_head_fila->get_proximo();

                delete elemento_removido;

                tamanho_da_fila -= 1;
            }
        }

        int recuperar_tamanho_da_fila() {
            return tamanho_da_fila;
        }

        string recuperar_primeiro_elemento_da_fila() {
            if (elemento_head_fila != nullptr) {
                return elemento_head_fila->get_nome();
            } 
        }

        string recuperar_ultimo_elemento_da_fila() {
            if (elemento_tail_fila != nullptr) {
                return elemento_tail_fila->get_nome();
            } 
        }

        void destruir_fila() {
            while (tamanho_da_fila > 0) {
                desenfileirar_o_primeiro_elemento();
            }   
        }
};

int main() {

    Fila fila;
    // Cria a fila
    fila.criar_fila();

    // Empilha alguns elementos
    fila.enfileirar_um_elemento("ana");
    fila.enfileirar_um_elemento("bruno");
    fila.enfileirar_um_elemento("caio");

    cout << "primeiro da fila:" <<  fila.recuperar_primeiro_elemento_da_fila() << endl;
    cout << "ultimo da fila: " << fila.recuperar_ultimo_elemento_da_fila() << endl;
    cout << "tamanho da fila: " << fila.recuperar_tamanho_da_fila() << endl;

    // Desinfilera o primeiro da fila
    fila.desenfileirar_o_primeiro_elemento();

    cout << "primeiro da fila:" <<  fila.recuperar_primeiro_elemento_da_fila() << endl;
    cout << "tamanho da fila: " << fila.recuperar_tamanho_da_fila() << endl;

    cout << "\n-------Adicionando mais alguns-------\n " << endl;

    // Empilha alguns elementos
    fila.enfileirar_um_elemento("daniel");
    fila.enfileirar_um_elemento("everton");
    fila.enfileirar_um_elemento("felipe");

    cout << "primeiro da fila:" <<  fila.recuperar_primeiro_elemento_da_fila() << endl;
    cout << "ultimo da fila: " << fila.recuperar_ultimo_elemento_da_fila() << endl;
    cout << "tamanho da fila: " << fila.recuperar_tamanho_da_fila() << endl;

    // Desinfilera o primeiro da fila
    fila.desenfileirar_o_primeiro_elemento();

    cout << "primeiro da fila:" <<  fila.recuperar_primeiro_elemento_da_fila() << endl;
    cout << "tamanho da fila: " << fila.recuperar_tamanho_da_fila() << endl;

    cout << "\n-------Destruindo fila-------\n " << endl;

    // Deletar fila
    fila.destruir_fila();

    cout << "tamanho da fila: " << fila.recuperar_tamanho_da_fila() << endl;

}