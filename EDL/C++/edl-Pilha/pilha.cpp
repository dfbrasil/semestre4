#include <iostream>
using namespace std;

class Elemento{
    private:
    int valor;
    Elemento* proximo;

    public:
        Elemento(int valor) : valor(valor), proximo(nullptr){}

        int get_valor(){
            return valor;
        }

        Elemento* get_proximo(){
            return proximo;
        }
            
        void str_ptr(Elemento* proximo_node){
            this->proximo = proximo_node;
        };

};

