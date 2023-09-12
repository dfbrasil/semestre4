#include <iostream>
using namespace std;

class Funcionario{
    string nome_funcionario;
    float salario;
    string admissao;
public:
    void add_nome_funcionario (string nome_funcionario);
    void add_salario_funcionario (float salario);
    void add_data_funcionario (string admissao);
    void novo_salario();
    void consulta_nome();
};

class Empresa{
    string nome_empresa;
    string cnpj;

public:
    void cria_empresa( string nome_empresa, string cnpj);
};
