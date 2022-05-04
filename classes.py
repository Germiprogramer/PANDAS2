class Filas:
  def __init__(self, csv):
    self.csv = csv

  def calculo(self):
    print('El numero de filas es:',self.csv.shape[0])

class Columnas:
  def __init__(self, csv):
    self.csv = csv

  def calculo(self):
    print('El numero de columnas es:',self.csv.shape[1])

class Maximos:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      max = self.csv[self.columna].max()
      print("El valor máximo es:")
      print(max)

class Minimos:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      min = self.csv[self.columna].min()
      print("El valor mínimo es:")
      print(min)

class Mediana:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      median = self.csv[self.columna].median()
      print("La mediana es:")
      print(median)

class Moda:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      moda = self.csv[self.columna].mode()
      print("La moda es:")
      print(moda)

class Rango:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      rango = self.csv[self.columna].range()
      print("La moda es:")
      print(rango)

class Q1:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      q1 = self.csv[self.columna].quantile(0.25)
      print("El primer cuartil es:")
      print(q1)

class Q3:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      q3 = self.csv[self.columna].quantile(0.75)
      print("El tercer cuartil es:")
      print(q3)