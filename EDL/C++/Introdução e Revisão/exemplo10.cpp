#include <iostream>
using namespace std;

int main() {

    float preco = 99.99;
    float* ptr = &preco;

    cout << *ptr/2 << endl;

    return 0;
}