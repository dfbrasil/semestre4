#include "conta.h"

void Conta::inicializa(int num, string n, float s){
    numero = num;
    nome = n;
    saldo = s;
    if (saldo < 0)
        cout << "Erro na criação da Conta" << endl;
}

void Conta::deposita(float valor){
    saldo = saldo + valor;
}

void Conta::consulta(){
    cout << "Cliente: " << nome << endl;
    cout << "Saldo Atual: " << saldo << endl;
    cout << "Número da Conta: " << numero << endl;
}

int Conta::saque(float valor){
    if (saldo < valor){
        return 0;
    }
    else {
        saldo = saldo - valor;
        return 1;
    }
}