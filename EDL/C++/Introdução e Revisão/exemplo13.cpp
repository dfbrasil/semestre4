#include <iostream>
using namespace std;

class Aluno {
public:
    Aluno(string nome, int idade) : nome(nome), idade(idade) {}

    void Apresentar() {
        cout << "Meu nome é " << nome << " e tenho " << idade << " anos." << endl;
    }

private:
    string nome;
    int idade;
};

int main() {

    Aluno aluno1("Daniel" ,12);
    Aluno* ptr = &aluno1;

    ptr->Apresentar();



    return 0;
}