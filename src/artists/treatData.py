import pandas
import numpy
import re

data = pandas.read_csv("artists.csv")

data = data.loc[:, data.columns.isin(['name', 'popularity'])]

data = data[data.popularity != 0]

import ipdb; ipdb.set_trace()

artistList = []
for index, row in data.iterrows():
    row["name"] = re.sub(r"([\[\]'|]+)", '', row["name"])
    artista = row["name"]
    popularidade = row["popularity"]
    artistList.append(f'{artista}|{popularidade}')

df = pandas.DataFrame(artistList)
df.to_csv("artists.txt", header=False, index=False)