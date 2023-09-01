
from prova import Prova
    
prova1 = Prova()
prova2 = Prova()

for i in range(15):
    resposta = input(f'Digite a resposta da questao {i+1}: ')
    prova1.resposta_aluno(resposta)

prova1.acertos()
prova1.nota()

for i in range(15):
    resposta = input(f'Digite a resposta da questao {i+1}: ')
    prova2.resposta_aluno(resposta)

prova2.acertos()
prova2.nota()

nota_maior = prova1.maior(prova2)
print(f'A nota do aluno com mais acertos é: {nota_maior}')