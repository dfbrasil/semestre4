#include <iostream>
using namespace std;

int main(){

    int x = 5;
    int *ptr;
    ptr = &x;
    cout << "O valor da variável X é: " << *ptr << endl;
    *ptr = 10;
    cout << "Agora, X vale: " << *ptr << endl;
    return 0;
}