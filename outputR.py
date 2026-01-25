import pandas as pd
df = pd.read_csv("Rainsford.txt", header=None, sep="|")
df.columns = ["text"]
print(df.head())