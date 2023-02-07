import pandas as pd

data = pd.read_csv("tracks_features.csv")
df = data[['name', 'artists', 'release_date']]
feat = df[df['artists'].str.contains(",") & (df['release_date'] > '2010')]
feat.to_csv("src\data\filtered.csv", index=False)