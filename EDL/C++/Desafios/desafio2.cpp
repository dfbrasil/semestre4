#include <iostream>
using namespace std;

int Interations(long n) {
    int iteracoes = 0;
    
    while (n != 1) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = (n * 3) + 1;
        }
        iteracoes++;
    }
    
    return iteracoes;
}

int main() {
    long long menorNumero = 1;
    int maxIteracoes = 0;

    for (long numero = 1; numero < 999999; numero++) {
        int iteracoes = Interations(numero);
        if (iteracoes > maxIteracoes) {
            maxIteracoes = iteracoes;
            menorNumero = numero;
        }
    }

    cout << "Número com mais iterações: " << menorNumero << endl;
    cout << "Número de iterações: " << maxIteracoes << endl;

    return 0;
}
