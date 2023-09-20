#include <iostream>
using namespace std;

class Tarefa{
public:

    Tarefa(string tarefa) : tarefa(tarefa), proximo(nullptr){};

    string getNome(){
        return tarefa;
    }

    Tarefa* getProximo(){
        return proximo;
    }

    void setProximo(Tarefa* node){
        proximo = node;
    }

private:
    string tarefa;
    Tarefa* proximo;

};

class ListaDeTarefas{
public:

    ListaDeTarefas() : head(nullptr), tamanho(0) {};

    void adicionarTarefa(string tarefa){
        Tarefa* novaTarefa = new Tarefa(tarefa);
        novaTarefa->setProximo(head);
        head = novaTarefa;
        tamanho++;
    }

    void exibirTarefas(){
        Tarefa* atual = head;
        while(atual != nullptr){
            cout << atual->getNome();
            atual = atual->getProximo();
        }
    }

    int imprimeTamanho(){
        return tamanho;
    }

private:

Tarefa* head;
int tamanho;

};

int main() {
    ListaDeTarefas lista;

    lista.adicionarTarefa("Estudar para a prova");
    lista.adicionarTarefa("Fazer compras");
    lista.adicionarTarefa("Lavar o carro");

    std::cout << "Tarefas na lista:" << std::endl;
    lista.exibirTarefas();

    std::cout << "Número de tarefas: " << lista.imprimeTamanho() << std::endl;

    return 0;
}