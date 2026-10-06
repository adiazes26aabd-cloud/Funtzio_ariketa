import pandas as pd


df = pd.read_csv("ikasleak.csv")

class ikaslea:
    def __init__(self,izena,adina,ikasgela,nota):
        self.izena = izena
        self.adina = adina
        self.ikasgela = ikasgela
        self.nota = nota



notaren_arabera_ordenatuta = df.sort_values( by="nota", key=lambda x: x, ascending=False)
   

print(notaren_arabera_ordenatuta)