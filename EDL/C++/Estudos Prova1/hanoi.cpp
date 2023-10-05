#include <iostream>

class Disco {
public:
    int tamanho;
    Disco* proximo;

    Disco(int tamanho) : tamanho(tamanho), proximo(nullptr) {}
};

class Torre {
public:
    Torre() : topo(nullptr) {}

    void empilhar(int tamanho) {
        Disco* novoDisco = new Disco(tamanho);
        if (!topo || tamanho < topo->tamanho) {
            novoDisco->proximo = topo;
            topo = novoDisco;
        } else {
            std::cout << "Movimento inválido. Disco maior não pode ser colocado em cima de um menor." << std::endl;
            delete novoDisco;
        }
    }

    int desempilhar() {
        if (topo) {
            Disco* discoRemovido = topo;
            topo = topo->proximo;
            int tamanho = discoRemovido->tamanho;
            delete discoRemovido;
            return tamanho;
        }
        return -1;
    }

    void imprimir() {
        Disco* atual = topo;
        while (atual) {
            std::cout << atual->tamanho << " ";
            atual = atual->proximo;
        }
        std::cout << std::endl;
    }

private:
    Disco* topo;
};

void torreDeHanoi(int n, Torre& origem, Torre& destino, Torre& auxiliar) {
    if (n == 1) {
        int disco = origem.desempilhar();
        destino.empilhar(disco);
        std::cout << "Mova o disco " << disco << " de Torre " << &origem << " para Torre " << &destino << std::endl;
    } else {
        torreDeHanoi(n - 1, origem, auxiliar, destino);
        torreDeHanoi(1, origem, destino, auxiliar);
        torreDeHanoi(n - 1, auxiliar, destino, origem);
    }
}

int main() {
    int numDiscos = 3;

    Torre torreA, torreB, torreC;

    for (int i = numDiscos; i >= 1; i--) {
        torreA.empilhar(i);
    }

    std::cout << "Estado inicial das torres:" << std::endl;
    std::cout << "Torre A: ";
    torreA.imprimir();
    std::cout << "Torre B: ";
    torreB.imprimir();
    std::cout << "Torre C: ";
    torreC.imprimir();

    torreDeHanoi(numDiscos, torreA, torreC, torreB);

    std::cout << "Estado final das torres:" << std::endl;
    std::cout << "Torre A: ";
    torreA.imprimir();
    std::cout << "Torre B: ";
    torreB.imprimir();
    std::cout << "Torre C: ";
    torreC.imprimir();

    return 0;
}
