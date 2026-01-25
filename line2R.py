import pandas as pd
df = pd.read_csv("Rainsford.txt", sep="|", header=None, names=["line"])
print(df.loc[2, "line"])

