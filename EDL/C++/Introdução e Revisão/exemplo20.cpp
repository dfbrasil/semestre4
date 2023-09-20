#include <iostream>
using namespace std;

class Retangulo{
public:
    Retangulo(float comprimento, float largura) : comprimento_(comprimento), largura_(largura){};

    double calcularArea(){
        return comprimento_ * largura_;
    }

    void redimensionar (float novoComprimento, float novaLargura){
        comprimento_ = novoComprimento;
        largura_ = novaLargura;
    }

private:
    float comprimento_;
    float largura_;
};


int main() {

    Retangulo* ptrRetangulo;

    ptrRetangulo = new Retangulo( 5.0, 3.0);

    float area = ptrRetangulo->calcularArea();

    ptrRetangulo->redimensionar(6.0, 4.0);

    float novaArea = ptrRetangulo->calcularArea();

    cout << area << " ," << novaArea << endl;

    delete ptrRetangulo;
return 0;
}