#include <iostream>
using namespace std;

const int SIZE = 10;

int hash(int x) {
    return x % SIZE;
}

void insere(int a[], int x) {
    int k = hash(x);

    while (a[k] != 0) {
        k = (k + 1) % SIZE;
    }

    a[k] = x;
}

int busca_hash(int a[], int x) {
    int k = hash(x);

    // Procurando pela chave na tabela hash
    while (a[k] != 0) {
        if (a[k] == x) {
            return k; // Chave encontrada na posição k
        }
        k = (k + 1) % SIZE;
    }

    return -1; // Chave não encontrada
}

int main() {
    int a[SIZE] = {0}; // Inicializando a tabela hash com 0

    insere(a, 10);

    // Exemplo de busca
    int chave = 10;
    int posicao = busca_hash(a, chave);

    if (posicao != -1) {
        cout << "Chave " << chave << " encontrada na posição " << posicao << endl;
    } else {
        cout << "Chave " << chave << " não encontrada na tabela hash." << endl;
    }

    return 0;
}
