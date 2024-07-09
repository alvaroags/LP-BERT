import pandas as pd
import json

# Caminho para o arquivo JSON
caminho_arquivo = '2024_07_01_20_54_28.json'

# Carregar o arquivo JSON
with open(caminho_arquivo, 'r') as arquivo_json:
    dados_json = json.load(arquivo_json)

# Agora você pode acessar os dados do arquivo JSON
# print(dados_json)

df_generated = pd.DataFrame(dados_json["generated"])
df_reference = pd.DataFrame(dados_json["reference"])

df_generated.to_csv("generated.csv", index=False)
df_reference.to_csv("reference.csv", index=False)

df = pd.read_csv('train_checkins_Alaska.csv')
df.drop['uid']
print(df)