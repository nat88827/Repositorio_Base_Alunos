# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado


# 1 - (dias) Pedir a quantidade de dias
# 2 - (km) Pedir a quantidade de km percorridos

# 3 - (valor_dias) Calcular o valor total dos dias (dias * 60)
# 4 - (valor_km) Calcular o valor total da quilometragem (km * 0.15)


# 5 - (valor_total) Calcular o valor total somando o valor dos dias + o valor dos km

# 6 - Mostrar na tela a frase formatad

dias=int(input('Quantos dias o carro foi usado?'))
Km=int(input('Quantos Km foi rodado?'))
valor_do_dia=0



modelo=input('qual o modelo do carro?')

if modelo=='civic':
    valor_do_dia=60


elif modelo=='porsche':
    valor_do_dia=100

else:
    valor_do_dia=25
  
valor_dias=(dias*valor_do_dia)
Valor_Km=(Km*0.15)
print(f'você andou {Km} Kilometros por {dias} dias, então o preço a pagar é R${valor_dias+Valor_Km}')