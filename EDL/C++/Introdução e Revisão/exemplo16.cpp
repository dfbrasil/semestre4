#include <iostream>
using namespace std;

class Aluno{
public:
    Aluno(string nome, int matricula) : nome(nome), matricula(matricula){};

    void exibirDados(){
        cout << "Nome: " << nome << " Matrícula: " << matricula << endl;
    }

private:
    string nome;
    int matricula;

};

int main() {

    Aluno* alunos[3];
    
    Aluno aluno1("aluno01", 01);
    Aluno aluno2("aluno02", 02);
    Aluno aluno3("aluno03", 03);

    alunos[0] = &aluno1;
    alunos[1] = &aluno2;
    alunos[2] = &aluno3;

    for (int i = 0; i < 3; i++){
        alunos[i]->exibirDados();
    }
}