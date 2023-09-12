#include <iostream>
using namespace std;

int main (){

    int i;
    int j = 10;
    int *v;
    v = new int[10];
    //v é um ponteiro para uma área que tem 10 inteiros
    //v funciona como um vetor

    for (i = 0; i < 10; i++){
        v[i] = j;
        j++;
    }

    for (i = 0; i < 10 ; i++){
        cout << "v[" << i << "]: " << v[i] << endl;
    }

    cout << "Endereço de 'v': " << v << endl; 
    //imprime o endereço da área alocada para 'v'
    delete[] v;

return 0;

}