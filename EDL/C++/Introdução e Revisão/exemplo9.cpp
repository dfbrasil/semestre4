#include <iostream>
using namespace std;


int main(){

    int numero = 20;
    int *ptr = &numero;

    *ptr = *ptr + 5;

    cout << numero;

}