#include <iostream>
using namespace std;

class Livro{
public:
    Livro(string titulo, string autor, int anoPublicacao) : titulo_(titulo), autor_(autor), anoPublicacao_(anoPublicacao){};

    void exibirDetalhes(){
        cout << titulo_ << endl;
        cout << autor_ << endl;
        cout << anoPublicacao_ << endl;
    }

private:
    string titulo_;
    string autor_;
    int anoPublicacao_;
};

class Biblioteca{
public:
    Biblioteca(int tamanhoMaximo) : tamanhoMaximo_(tamanhoMaximo), numLivros_(0), livros_(new Livro*[tamanhoMaximo]){};

    ~Biblioteca(){
        for (int i = 0; i < numLivros_; i++){
            delete livros_[i];
        }
        delete livros_;
    }

    void adicionarLivro(string titulo, string autor, int anoPublicacao ){
        if (numLivros_ < tamanhoMaximo_){
            livros_[numLivros_] = new Livro( titulo, autor, anoPublicacao);
            numLivros_++;
        } else {
            cout << "Biblioteca Cheia";
        }
    }

    void listaLivros(){
        cout << "Livros na biblioteca";

        for (int i = 0; i < numLivros_; i++){
            cout << "Livro #" << i+1 << endl;
            livros_[i]->exibirDetalhes();
            cout << endl;
        }
    }

private:

int tamanhoMaximo_;
int numLivros_;
Livro** livros_;

};

int main(){
    Biblioteca biblioteca(5);

    biblioteca.adicionarLivro("l1", "a1", 123);
    biblioteca.adicionarLivro("l2", "a2", 345);

    biblioteca.listaLivros();

    return 0;
}