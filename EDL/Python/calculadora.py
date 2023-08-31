
capitalInicial = float(input('Digite o valor inicial: \n'))
aporteMensal = float(input('Digite o aporte mensal \n'))
anos = int(input('Digite a quantidade de anos de investimento \n'))
valorJuros = float(input('Qual o valor da taxa de juros anual? \n'))/100
jurosMensal = valorJuros/12
meses = anos*12

for i in range(1,meses+1):
    print(f'No mês {i} o valor acumulado é de R$ {round(capitalInicial*(1+jurosMensal)**i + aporteMensal*(((1+jurosMensal)**i)-1)/jurosMensal,2)}')

for i in range(anos+1):
    print(f'No ano {i} o saldo acumulado é de R$ {round(capitalInicial*(1+jurosMensal)**(i*12) + aporteMensal*(((1+jurosMensal)**(i*12))-1)/jurosMensal,2)} e o rendimento é de R$ {round(capitalInicial*(1+jurosMensal)**(i*12) + aporteMensal*(((1+jurosMensal)**(i*12))-1)/jurosMensal - capitalInicial,2)}')

valorFinal = capitalInicial*(1+jurosMensal)**meses + aporteMensal*(((1+jurosMensal)**meses)-1)/jurosMensal
print(f'O valor final é de R$ {round(valorFinal,2)}')
