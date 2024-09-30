import pandas as pd

tabela = pd.read_csv("cancelamentos.csv", nrows=1000)
print(tabela)