#include "conta.h"
using namespace std;

int main(){

    Conta MinhaConta;
    Conta *OutraConta = new Conta;

    //MinhaConta.saldo = 10; //ERRO

    MinhaConta.inicializa(1234, "Daniel", 100.00);
    OutraConta->inicializa(5678, "Brasil", 200);

    MinhaConta.deposita(15.55);
    MinhaConta.consulta();
    MinhaConta.saque(10);
    MinhaConta.consulta();

    OutraConta->consulta();

    delete OutraConta;
return 0;
}