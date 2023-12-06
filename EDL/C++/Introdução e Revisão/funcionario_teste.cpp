#include "funcionario.h"
using namespace std;

int main(){

    int num_func;

    cout << "Quantos funcionarios a empresa terá? " << endl;

    cin >> num_func;

    Funcionario Funcionarios[num_func];

    for (int i = 0; i < num_func; i++){
        string nome = "";
        float salario = 0.0;
        string data = "";
        cout << "Digite o nome do funcionário: ";
        cin >> nome;
        Funcionarios[i].add_nome_funcionario(nome);
        cout << "Digite o salario do funcionário: ";
        cin >> salario;
        Funcionarios[i].add_salario_funcionario(salario);
        cout << "Digite a data de admissão do funcionário: ";
        cin >> data;
        Funcionarios[i].add_data_funcionario(data);
    }

        for (int i = 0; i < num_func; i++){
        Funcionarios[i].consulta_nome();
        Funcionarios[i].novo_salario();
    }

return 0;
}