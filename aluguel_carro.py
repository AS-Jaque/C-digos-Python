print('Calculadora de aluguel de carros \n')
diaria = 90
kmExtra = 12
qtdDia = int(input('Digite a quantidade total de dia(s) do aluguel do veículo: \n'))
kmPercorrido = float(input('Digite a quilometragem total percorrida(apenas números, separados por ponto): \n'))
if(kmPercorrido <= 100):
    valor = qtdDia * diaria
elif(kmPercorrido > 100):
    valor = ((kmPercorrido*kmExtra) - (100*kmExtra)) + qtdDia*diaria
print('Valor total a ser pago é: R$%.2f' %valor)
