#include "funcionario.h" // Inclua o arquivo de cabeçalho da classe Funcionario

void Funcionario::add_nome_funcionario(string nome) {
    nome_funcionario = nome;
}

void Funcionario::add_salario_funcionario(float salario) {
    this->salario = salario;
}

void Funcionario::add_data_funcionario(string admissao) {
    this->admissao = admissao;
}

void Funcionario::novo_salario(){
    float aumento;
    aumento = salario + (salario*0.1);
    cout << "Salário com aumento: " << aumento << endl;
}

void Funcionario::consulta_nome(){
    cout << "Nome do Funcionário:" << nome_funcionario << endl;
}