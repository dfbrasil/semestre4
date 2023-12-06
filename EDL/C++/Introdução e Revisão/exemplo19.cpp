#include <iostream>
using namespace std;

class Circulo
{
public:
    Circulo(float raio) : raio_(raio){};

    float areaCirculo()
    {
        return 3.14 * raio_ * raio_;
    }

    float set_raio(float raio)
    {
        raio_ = raio;
    }

private:
    float raio_;
};

int main()
{

    Circulo *ptrCirculo;

    ptrCirculo = new Circulo(5.0);

    float area = ptrCirculo->areaCirculo();

    ptrCirculo->set_raio(7.5);

    float novaArea = ptrCirculo->areaCirculo();

    cout << area << endl;

    cout << novaArea << endl;

    return 0;
}
