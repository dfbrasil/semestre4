#include <iostream>
using namespace std;

int main() {

    int x=10;
    int *ptr;
    ptr = &x;
    cout << "O endereço de X é: " << ptr << endl;
    cout << "O valor de X é: " << *ptr << endl;

    return 0;
}