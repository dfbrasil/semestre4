# Considere a seguinte classe, cujo método resposta_questao recebe como parâmetro o número de uma questão e retorna a sua resposta correta, proveniente de um gabarito.

class Gabarito:
    
    def resposta_questao(self, numero_questao):
        gabarito = ['a','b','c','d','e']
        for i, resposta in enumerate(gabarito, start=1):
            if i == numero_questao:
                print(f'A resposta correta da questão de número {numero_questao} é {resposta.capitalize()}')
                break
        else:
            print("Número de questão fora do intervalo")