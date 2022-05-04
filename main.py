from media import Media
from desviacion_tipica import Desviacion_tipica
from classes import Filas, Columnas, Maximos, Minimos, Mediana, Moda, Q1, Q3
import pandas as pd

import matplotlib.pyplot as plt

pokemon = pd.read_csv("pokemon_stats (1).csv")

#Crear csv
from random import randint

file = open("Naranjas.csv", "w")
file.write("Peso Naranjas, Tamano")

for i in range(100):
  num = randint(100,200)
  tam = randint(20,30)
  file.write("\n{}, {}".format(num, tam))

file.close()

naranjas = pd.read_csv("Naranjas.csv")


#Numero de filas
filas = Filas(naranjas)
filas.calculo()
#Numero de columnas
columnas = Columnas(naranjas)
columnas.calculo()

#Valores maximos
max = Maximos(naranjas, "Peso Naranjas")
max.calculo()
#Valores minimos
min = Minimos(naranjas, "Peso Naranjas")
min.calculo()

#Media
media_HP = Media(naranjas, "Peso Naranjas")
media_HP.calculo()

#Mediana
mediana_HP = Mediana(naranjas, "Peso Naranjas")
mediana_HP.calculo()

#Moda
moda_HP = Moda(naranjas, "Peso Naranjas")
moda_HP.calculo()

#Rango
#rango = Rango(naranjas, "Peso Naranjas")
#rango.calculo()
#print("El rango es {}".format(max.calculo() - min.calculo() ))

#Desviación típica
desv_HP = Desviacion_tipica(naranjas, "Peso Naranjas")
desv_HP.calculo()

#q1
q1 = Q1(naranjas, "Peso Naranjas")
q1.calculo()


#q3
q3 = Q3(naranjas, "Peso Naranjas")
q3.calculo()

#rango intercuartilico
a = naranjas["Peso Naranjas"].quantile(0.25)
b = naranjas["Peso Naranjas"].quantile(0.75)
rango_int = b - a
print("El rango intercuartilico es {}".format(rango_int))

#grafico histograma

#grafico = Grafico_histograma(naranjas, "Peso Naranjas")
#grafico.crear_grafico()

def grafico(dataset, tipo_grafico):
  fig, ax = plt.subplots()
  if tipo_grafico=="dispersion":
    ax.scatter(naranjas["id"], naranjas["Pesas"])
  else:
    dataset.plot(kind=tipo_grafico, ax = ax)
  ax.set_title('Grafico muy solido', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
  ax.set_ylabel('')
  plt.show()

  plt.savefig('graficos/grafico' + '.png', bbox_inches='tight')

grafico(naranjas["Peso Naranjas"], "pie")
grafico(naranjas["Peso Naranjas"], "bar")
grafico(naranjas["Peso Naranjas"], "hist")

