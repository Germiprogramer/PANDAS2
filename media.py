import pandas as pd

pokemon = pd.read_csv("pokemon_stats (1).csv")


class Media:
    def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna

    def calculo(self):
        media = self.csv[self.columna].mean()
        print("La media es:")
        print(media)



