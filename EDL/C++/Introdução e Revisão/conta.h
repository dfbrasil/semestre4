#include <iostream>
using namespace std;

class Conta{
    int numero;
    string nome;
    float saldo;
    //os atributos acima são privados por default

public:
    void inicializa (int num, string n, float s);
    void deposita (float valor);
    void consulta();
    int saque(float valor);    
};
