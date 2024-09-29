import json 


caminho_json = 'dates.json'

with open(caminho_json, 'r') as file:
    dados = json.load(file)

faturamento_diario = [dia['valor'] for dia in dados['faturamento']]

print("Faturamento Diário:")
for dia in dados['faturamento']:
    print(f"Dia {dia['dia']}: R$ {dia['valor']:.2f}")
