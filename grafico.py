import matplotlib.pyplot as plt

class Grafico():
    def __init__(self, lista, media, mediana, cuartil_1, cuartil_2, cuartil_3):
        self.lista = lista
        self.media = media
        self.mediana = mediana
        self.cuartil_1 = cuartil_1
        self.cuartil_2 = cuartil_2
        self.cuartil_3 = cuartil_3

    def visualizacion(self):  
  
        plt.subplot(2, 2, 1)  
        plt.hist(self.lista)  
        plt.title("Histograma y media")  
        plt.axvline(self.media, color='red', linestyle='dashed',  
        linewidth=1,label = str(self.media))  
        plt.legend(loc='upper right')  
        
        plt.subplot(2, 2, 2)  
        plt.hist(self.lista)  
        plt.title("Histograma y mediana")  
        plt.axvline(self.mediana, color='green', linestyle='dashed',  
        linewidth=1,label = str(self.mediana))  
        plt.legend(loc='upper right')  
        
        plt.subplot(2, 2, 3)  
        plt.hist(self.lista)  
        plt.title("Histograma y cuartiles")  
        plt.axvline(self.cuartil_1, color='orange', linestyle='dashed',  
        linewidth=1,label = "Q1: "+str(self.cuartil_1))  
        plt.axvline(self.cuartil_2, color='orange', linestyle='dashed',  
        linewidth=1,label = "Q2: "+str(self.cuartil_2))  
        plt.axvline(self.cuartil_3, color='orange', linestyle='dashed',  
        linewidth=1,label = "Q3: "+str(self.cuartil_3))  
        plt.legend(loc='upper right')  
        
        plt.subplot(2, 2, 4)  
        plt.boxplot(self.lista)  
        plt.title("Diagrama de caja y bigotes")  
        plt.show() 

fig, ax = plt.subplots()

    

#pie = sectores
#bar = barras
#hist = histograma

class Grafico_barras:
  def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna
  
  def crear_grafico(self):
    fig, ax = plt.subplots()
    self.csv[self.columna].plot(kind="hist", ax=ax)
    ax.set_title("histograma", loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel('')
    plt.savefig('img/histograma-' + '-'.join(self.columna) + '.png', bbox_inches='tight')
    return

class Grafico_sectores:
  def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna
  
  def crear_grafico(self):
    fig, ax = plt.subplots()
    self.csv[self.columna].plot(kind="hist", ax=ax)
    ax.set_title("histograma", loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel('')
    plt.savefig('img/histograma-' + '-'.join(self.columna) + '.png', bbox_inches='tight')
    return

class Grafico_histograma:
  def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna
  
  def crear_grafico(self):
    fig, ax = plt.subplots()
    self.csv[self.columna].plot(kind="hist", ax=ax)
    ax.set_title("histograma", loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel('')
    plt.savefig('img/histograma-', bbox_inches='tight')
    return
    