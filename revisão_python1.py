# -*- coding: utf-8 -*-
"""Revisão Python1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JsYbM9L-HO6A8M36ULM65di5AZow9EHt
"""

numeroa = int(input("Digite o primeiro número: "))
numerob = int(input("Digite o segundo número: "))

soma = numeroa + numerob 

print(soma)

valor_metros = int(input("Digite a medida em metros: "))
calculo = valor_metros * 1000

print("O valor dessa medida é de", calculo, "mm")

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total_em_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print("O total disso é de", total_em_segundos, "segundos")

salario_atual = int(input("Qual é seu salário atual? "))
percentual_aumento = int(input("Qual o percentual de aumento? "))
salario_novo = (salario_atual * (100 + percentual_aumento) / 100)

print("Seu novo salário será de: R$",round(salario_novo))

preco_mercadoria = float(input("Diga o preço da mercadoria: "))
percentual_desconto = float(input("Diga o percentual de desconto: "))
preco_novo = (preco_mercadoria * 100) / (100 + percentual_aumento)
valor_economizado = preco_mercadoria - preco_novo

print("Você economizou R$", round(valor_economizado, 2))
print("O Valor do Produto será de: R$", round(preco_novo, 2))

distancia = int(input("Quantos quilometros serão percorridos? "))
velocidade_media = int(input("Qual a velocidade média que será atingida na viagem? "))
tempo_viagem_horas = distancia / velocidade_media
tempo_viagem_minutos = tempo_viagem_horas * 60

print("O tempo gasto na viajem será em média de: ", round(tempo_viagem_horas, 1), "h ou ", round(tempo_viagem_minutos), "m")

temperatura_celsius = int(input("Digite uma temperatura em graus celsius: "))
temperatura_fahrenheit = (9 * temperatura_celsius / 5) + 32 

print("A temperatura em fahrenheit é de: ", round(temperatura_fahrenheit, 1), "°F")

temperatura_fahrenheit = float(input("Digite uma temperatura em graus fahrenheit: "))
temperatura_celsius = (temperatura_fahrenheit - 32) * (5 / 9)

print("A temperatura em celsius é de: ", round(temperatura_celsius), "°C")

distancia_percorrida = int(input("Distância percorrida em quilômetros: "))
dias_usados = int(input("Quantidade de dias desde que o carro foi alugado: "))
preco_rodagem = distancia_percorrida * 0.15
preco_dias = dias_usados * 60
preco_aluguel = preco_rodagem + preco_dias 

print("O valor do aluguel sairá: R$", round(preco_aluguel, 2))

cigarros_dia = int(input("Quantos cigarros fumados por dia? "))
anos_fumante = int(input("Quantos anos fumando? "))

cigarros = (anos_fumante * 365)*cigarros_dia
dias_perdidos = (cigarros * 10)/24

print ("Provavelmente você terá", round(dias_perdidos), "dias a menos de vida..." )

print ("2 elevado a 1 milhão tem", len(str(2**1000000)),"digitos")