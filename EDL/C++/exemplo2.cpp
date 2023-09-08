#include <iostream>
using namespace std;

int main() {

    int x = 25;
    int *y = &x;
    *y = 30;

    cout << "valor atual de x é :" << x << endl;
    cout << "valor atual de y é :" << *y << endl;

    return 0;
}