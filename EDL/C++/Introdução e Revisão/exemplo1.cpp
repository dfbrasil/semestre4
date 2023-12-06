#include <iostream>
using namespace std;
#define alturaMaxima 125

typedef struct{
    int teste;
    int peso;
    int altura;
    
}PesoAltura;

int main(){
    int x;
    PesoAltura pessoa1;
    pessoa1.teste = 15;
    pessoa1.peso = 80;
    pessoa1.altura = 185;
    cout << "Peso: " << pessoa1.peso << endl;
    cout << "Altura: " << pessoa1.altura << endl;

    if (pessoa1.altura > alturaMaxima){
        cout << "Altura acima da Máxima." << endl;
    }
    else
    cout << "Peso abaixo da máxima." << endl;
    cout << &x << endl;
    cout << &pessoa1 << endl;
    cout << &pessoa1.altura << endl;
    cout << &pessoa1.peso << endl;
    cout << &pessoa1.teste << endl;
    return 0;
}