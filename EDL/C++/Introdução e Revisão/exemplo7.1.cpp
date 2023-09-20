#include <iostream>
using namespace std;

class Elemento {
public: 
    Elemento(int valor) : valor(valor) {}

    void imprimir(){
        cout << "Elemento" << valor << endl;
    }

private:
    int valor;
};

int main(){

    Elemento* elemento_ptr = new Elemento(42);

    elemento_ptr->imprimir();

    delete elemento_ptr;

    return 0;

}

