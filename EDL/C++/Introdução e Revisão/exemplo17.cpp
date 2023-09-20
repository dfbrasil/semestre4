#include <iostream>
using namespace std;

class Ponto{
public:

    Ponto (int x, int y) : x(x), y(y) {};

    int get_x() {
        return x;
    }

    int get_y(){
        return y;
    }

private:
    int x;
    int y;
};

int main() {

    Ponto* pontos[3];

    Ponto ponto1(1,2);
    Ponto ponto2(3,4);
    Ponto ponto3(5,6);

    pontos[0] = &ponto1;
    pontos[1] = &ponto2;
    pontos[2] = &ponto3;

    for (int i = 0; i < 3; i++){
        cout << pontos[i]->get_x() << pontos[i]->get_y() << endl;
    }
return 0;

}

