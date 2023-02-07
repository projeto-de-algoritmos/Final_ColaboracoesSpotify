import pandas
import re

data = pandas.read_csv("filtered.csv")
data = data.loc[:, data.columns.isin(['name', 'artists'])]

for index, row in data.iterrows():
    row["artists"] = re.sub("( [\[\]'\|]+)|([\[\]']+)", '', row["artists"])

musicas = []
for index, row in data.iterrows():
    artista = row["artists"]
    musica = row["name"]
    musicas.append(f'{musica}|{artista}')

df = pandas.DataFrame(musicas)
df.to_csv("grafos.txt", header=False, index=False)
