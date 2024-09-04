import json

with open('exercicio3.json', 'r') as file:
    dados = json.load(file)

valoresdes = list(dados.values())

print(valoresdes)

print("Maior faturamento: ", max(valoresdes))
print("Menor faturamento: ", min(valoresdes))

qntd = 0
total = 0

for valor in valoresdes:
    if valor != 0:
        qntd += 1
        total += valor

print("Media: ", total / qntd)

