#include <iostream>
using namespace std;

class Ponto {
public:
    int x;
    int y;

    Ponto(int x, int y) : x(x), y(y) {}
};

int main() {

    Ponto ponto1 (3, 5);

    Ponto* ptr = &ponto1;

    cout << ptr->x << ptr->y << endl;

    return 0;
}