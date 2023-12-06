#include <iostream>
using namespace std;

class Tarefa{
public:

    Tarefa (string tarefa) : tarefa(tarefa), proximaTarefa(nullptr){};

    string getTarefa(){
        return tarefa;
    }

    Tarefa* getProxima(){
        return proximaTarefa;
    }

    void setProxima(Tarefa* node){
        proximaTarefa = node;
    }

private:
    string tarefa;
    Tarefa* proximaTarefa;
};

class ListaDeTarefas{
public:
    ListaDeTarefas() : head(nullptr) , tamanho(0){};

    void adicionarTarefa(string tarefa){
        Tarefa* novaTarefa = new Tarefa(tarefa);
        novaTarefa->setProxima(head);
        head = novaTarefa;
        tamanho++;
    }

    void listaTarefa(){
        Tarefa* atual = head;
        while(atual != nullptr){
            cout << atual->getTarefa();
            atual = atual->getProxima();
        }
    }

    int imprimeTamanho(){
        return tamanho;
    }
private:
    Tarefa* head;
    int tamanho;
};

int main(){
    ListaDeTarefas lista;

    lista.adicionarTarefa("primeira");
    lista.adicionarTarefa("segunda");
    lista.adicionarTarefa("tereceira");

    lista.listaTarefa();

    cout << lista.imprimeTamanho();

    return 0;
}