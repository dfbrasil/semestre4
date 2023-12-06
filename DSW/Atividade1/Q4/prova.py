# Escreva uma classe classe Prova em que cada objeto representa uma prova feita por um aluno. Esta prova possui 15 questões de múltipla escolha (letras A a E). As 10 primeiras questões valem 0,5 ponto e as 5 últimas questões valem 1 ponto. Esta classe deverá controlar as questões respondidas pelo aluno. Para isto, a classe deve implementar os métodos:

# Construtor: recebe como parâmetro um objeto da classe Gabarito contendo o gabarito da prova;
# resposta_aluno: recebe como parâmetro a resposta dada pelo aluno a uma questão; este método não recebe entre os parâmetros o número da questão, ele mesmo deve estabelecer um controle interno de modo que as questões sejam inseridas sequencialmente, ou seja, a primeira vez que o método é chamado, insere a primeira questão, a segunda, insere a segunda questão, e assim por diante.
# acertos: retorna a quantidade de questões que o aluno acertou 
# nota: retorna a nota que o aluno tirou na prova
# maior: recebe como parâmetro um outro objeto da classe Prova e retorna a nota do aluno que acertou mais questões;
from gabarito import Gabarito

class Prova:
    
    def __init__(self, gabarito = Gabarito()):
        self.gabarito = gabarito
        self.respostas = []
        self.contador = 0
        self.corretas = []
        self.nota_final = 0
        
    def resposta_aluno(self,resposta):
        self.respostas.append(resposta)
        return self.respostas
    
    def print(self):
        print(self.respostas)
    
    def acertos(self):
        gabarito_real = self.gabarito.resposta_questao()
        for i in range(len(self.respostas)):
            if self.respostas[i] == gabarito_real[i]:
                self.corretas.append('v')
                self.contador += 1
            else:
                self.corretas.append('f')
        print(f'acertos {self.contador}')
        return self.corretas
        
    def nota(self):
        self.nota_final = 0.0

        for resposta in self.corretas[:9]:
            if resposta == 'v':
                self.nota_final += 0.5

        for resposta in self.corretas[10:14]:
            if resposta == 'v':
                self.nota_final += 1.0

        print(f'A nota é {self.nota_final}')
        return self.nota_final
    
    def maior(self, outra_prova):
        self_acertos = self.corretas.count('v')
        outra_acertos = outra_prova.corretas.count('v')
        if self_acertos > outra_acertos:
            return self.nota()
        elif outra_acertos > self_acertos:
            return outra_prova.nota()
        else:
            return "Empate"