# -*- coding: utf-8 -*-
"""Randu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yNYOcwRBCfsygji3j8zEgYwS4W4eKmWq
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

frec = [0,0,0,0,0,0,0,0,0,0]
lista = np.array([])
lista_prom = np.array([])

def randu(seed, n):
    global frec
    x = seed
    global lista
    global lista_prom
    lista = np.append(lista, (x % (pow(2, 31))) / (pow(2, 31) - 1))
    for i in range(0,n):
        x = (pow(2,16) + 3) * x % (pow(2, 31))
        y = x / (pow(2, 31) - 1)
        if y >=0 and y < 0.1:
            frec[0] = frec[0] + 1
        elif y >=0.1 and y < 0.2:
            frec[1] = frec[1] + 1
        elif y >=0.2 and y < 0.3:
            frec[2] = frec[2] + 1
        elif y >=0.3 and y < 0.4:
            frec[3] = frec[3] + 1
        elif y >=0.3 and y < 0.5:
            frec[4] = frec[4] + 1
        elif y >=0.5 and y < 0.6:
            frec[5] = frec[5] + 1
        elif y >=0.6 and y < 0.7:
            frec[6] = frec[6] + 1
        elif y >=0.7 and y < 0.8:
            frec[7] = frec[7] + 1
        elif y >=0.8 and y < 0.9:
            frec[8] = frec[8] + 1
        elif y >=0.9 and y <= 1:
            frec[9] = frec[9] + 1
        lista = np.append(lista, y)
        if i == 0:
            lista_prom = np.append(lista_prom, lista[i])
        else:
            lista_prom = np.append(lista_prom, sum(lista)/i)
    return lista

tamaño = 9000
randu( 65539, tamaño)
x = []

for i in range(0,10):
  x.append(i/10)

a_frec = np.array(frec)
plt.bar(x, a_frec/tamaño, align='center', width=0.09)
plt.xticks(x)
plt.show()

#plt.plot(lista[0:tamaño:2], lista[1:tamaño:2], 'o')
#plt.xlim(0,1)
#plt.ylim(0,1)
#plt.show()


figura = plt.figure()
grafica = figura.add_subplot(111,projection = '3d')

lista1 = lista[0:tamaño:3]
lista2 = lista[1:tamaño:3]
lista3 = lista[2:tamaño:3]


puntos = np.array([lista1, lista2, lista3])


  # xi = [:,0] ; yi = [:,1], zi = [:,2]
  # selecciona columnas, use la transpuesta de puntos
  #[xi, yi , zi] = np.transpose(puntos)

grafica.scatter(lista1,lista2,lista3, c = 'blue', marker='o', s = 0.1)
grafica.set_title('puntos, dispersión-scatter')
grafica.set_xlabel('eje x')
grafica.set_ylabel('eje y')
grafica.set_zlabel('eje z')
grafica.legend()
plt.show()

frec_poker = [0,0,0,0,0,0]

def prueba_poker():
  global lista
  global tamaño
  for i in range(0, tamaño):
    x = str(lista[i])[2:7]
    if cinco(x):
      frec_poker[0] += 1
    elif full(x):
      frec_poker[1] += 1
    elif pierna(x):
      frec_poker[2] += 1
    elif doble_par(x):
      frec_poker[3] += 1
    elif par(x):
      frec_poker[4] += 1
    else:
      frec_poker[5] += 1
       

def par(x):
  y = False
  for i in range(0,5):
    for j in range(0,5):
      if x[i] == x[j] and i != j:
        y = True
  return y

def pierna(x):
  y = False
  if x[0] == x[1] and x[0] == x[2]:
    y = True
  if x[0] == x[1] and x[0] == x[3]:
    y = True
  if x[0] == x[1] and x[0] == x[4]:
    y = True
  if x[0] == x[2] and x[0] == x[3]:
    y = True
  if x[0] == x[2] and x[0] == x[4]:
    y = True
  if x[0] == x[3] and x[0] == x[4]:
    y = True
  if x[1] == x[2] and x[1] == x[3]:
    y = True
  if x[1] == x[2] and x[1] == x[4]:
    y = True
  if x[1] == x[3] and x[1] == x[4]:
    y = True
  if x[2] == x[3] and x[2] == x[4]:
    y = True
  return y 

def doble_par(x):
  y = False
  if x[0] == x[1] and x[2] == x[3]:
    y = True
  elif x[0] == x[1] and x[2] == x[4]:
    y = True
  elif x[0] == x[1] and x[3] == x[4]:
    y = True
  elif x[0] == x[2] and x[1] == x[3]:
    y = True
  elif x[0] == x[2] and x[1] == x[4]:
    y = True
  elif x[0] == x[2] and x[3] == x[4]:
    y = True
  elif x[0] == x[3] and x[1] == x[2]:
    y = True
  elif x[0] == x[3] and x[1] == x[4]:
    y = True
  elif x[0] == x[3] and x[2] == x[4]:
    y = True
  elif x[0] == x[4] and x[1] == x[2]:
    y = True
  elif x[0] == x[4] and x[1] == x[3]:
    y = True
  elif x[0] == x[4] and x[2] == x[3]:
    y = True
  elif x[1] == x[2] and x[3] == x[4]:
    y = True
  elif x[1] == x[3] and x[2] == x[4]:
    y = True
  elif x[1] == x[4] and x[2] == x[3]:
    y = True
  return y

def full(x):
  y = False
  if x[0] == x[1] and x[0] == x[2] and x[3] == x[4]:
    y = True
  elif x[0] == x[1] and x[0] == x[3] and x[2] == x[4]:
    y = True
  elif x[0] == x[1] and x[0] == x[4] and x[2] == x[3]:
    y = True
  elif x[0] == x[2] and x[0] == x[3] and x[1] == x[4]:
    y = True
  elif x[0] == x[2] and x[0] == x[4] and x[1] == x[3]:
    y = True
  elif x[0] == x[3] and x[0] == x[4] and x[1] == x[2]:
    y = True
  elif x[1] == x[2] and x[1] == x[3] and x[1] == x[4]:
    y = True 
  elif x[1] == x[2] and x[1] == x[4] and x[0] == x[3]:
    y = True 
  elif x[1] == x[3] and x[1] == x[4] and x[0] == x[2]:
    y = True 
  elif x[2] == x[3] and x[2] == x[4] and x[0] == x[1]:
    y = True
  return y   

def cinco(x):
  y = False
  for i in range(1,5):
    if x[i-1] == x[i]:
      y = True
    else:
      y = False
      break
  return y

prueba_poker()
for i in range(0,6):
  frec_poker[i] = frec_poker[i] / tamaño


frec_esperada_poker = [0.0001, 0.009, 0.072, 0.108, 0.504, 0.3024]

labels = ['Quintilla', 'Full', 'Pierna', 'Doble Par', 'Par', 'Todos Distintos']
x = np.arange(len(labels))

fig, ax = plt.subplots()
rects1 = ax.bar(x - 0.35/2, frec_poker, 0.35, label='Obtenido')
ax.set_ylabel('')
ax.set_title('')
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.plot([0], [0.0001], label='Esperado', color="black")
plt.plot([0.5, 1.15], [0.009] * 2, color="black")
plt.plot([1.5, 2.15], [0.072] * 2, color="black")
plt.plot([2.5, 3.15], [0.108] * 2, color="black")
plt.plot([3.5, 4.15], [0.504] * 2, color="black")
plt.plot([4.5, 5.15], [0.3024] * 2, color="black")
plt.legend()
plt.show()



plt.plot(np.arange(tamaño), [0.5] * tamaño, label="Prom. esperado")
plt.plot( np.arange(tamaño), lista_prom, label="Prom. obtenido")
plt.ylim(0.4,0.6)
plt.xlabel("Números generados")
plt.ylabel("Promedio")
plt.legend()
plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

frec = [0,0,0,0,0,0,0,0,0,0]
lista = np.array([])
lista_prom = np.array([])

def randu(seed, n):
    x = seed
    global lista
    global lista_prom
    lista = np.append(lista, (x / (pow(2, 31) - 1)))
    for i in range(0,n):
        x = pow(7,5) * x % (pow(2, 31) - 1)
        y = x / (pow(2, 31) - 1)
        if y >=0 and y < 0.1:
            frec[0] = frec[0] + 1
        elif y >=0.1 and y < 0.2:
            frec[1] = frec[1] + 1
        elif y >=0.2 and y < 0.3:
            frec[2] = frec[2] + 1
        elif y >=0.3 and y < 0.4:
            frec[3] = frec[3] + 1
        elif y >=0.3 and y < 0.5:
            frec[4] = frec[4] + 1
        elif y >=0.5 and y < 0.6:
            frec[5] = frec[5] + 1
        elif y >=0.6 and y < 0.7:
            frec[6] = frec[6] + 1
        elif y >=0.7 and y < 0.8:
            frec[7] = frec[7] + 1
        elif y >=0.8 and y < 0.9:
            frec[8] = frec[8] + 1
        elif y >=0.9 and y <= 1:
            frec[9] = frec[9] + 1
        lista = np.append(lista, y)
        if(i == 0):
            lista_prom = np.append(lista_prom, lista[i])
        else:
            lista_prom = np.append(lista_prom, sum(lista)/i)
    return lista

tamaño = 10000
randu(41097334, tamaño)
x = []

for i in range(0,10):
  x.append(i/10)

a_frec = np.array(frec)
plt.bar(x, a_frec/tamaño, align='center', width=0.09)
plt.xticks(x)
plt.show()

plt.plot(lista[0:tamaño:2], lista[1:tamaño:2], 'o')
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

frec_poker = [0,0,0,0,0,0]

def prueba_poker():
  global lista
  global tamaño
  for i in range(0, tamaño):
    x = str(lista[i])[2:7]
    if cinco(x):
      frec_poker[0] += 1
    elif full(x):
      frec_poker[1] += 1
    elif pierna(x):
      frec_poker[2] += 1
    elif doble_par(x):
      frec_poker[3] += 1
    elif par(x):
      frec_poker[4] += 1
    else:
      frec_poker[5] += 1
       

def par(x):
  y = False
  for i in range(0,5):
    for j in range(0,5):
      if x[i] == x[j] and i != j:
        y = True
  return y

def pierna(x):
  y = False
  if x[0] == x[1] and x[0] == x[2]:
    y = True
  if x[0] == x[1] and x[0] == x[3]:
    y = True
  if x[0] == x[1] and x[0] == x[4]:
    y = True
  if x[0] == x[2] and x[0] == x[3]:
    y = True
  if x[0] == x[2] and x[0] == x[4]:
    y = True
  if x[0] == x[3] and x[0] == x[4]:
    y = True
  if x[1] == x[2] and x[1] == x[3]:
    y = True
  if x[1] == x[2] and x[1] == x[4]:
    y = True
  if x[1] == x[3] and x[1] == x[4]:
    y = True
  if x[2] == x[3] and x[2] == x[4]:
    y = True
  return y 

def doble_par(x):
  y = False
  if x[0] == x[1] and x[2] == x[3]:
    y = True
  elif x[0] == x[1] and x[2] == x[4]:
    y = True
  elif x[0] == x[1] and x[3] == x[4]:
    y = True
  elif x[0] == x[2] and x[1] == x[3]:
    y = True
  elif x[0] == x[2] and x[1] == x[4]:
    y = True
  elif x[0] == x[2] and x[3] == x[4]:
    y = True
  elif x[0] == x[3] and x[1] == x[2]:
    y = True
  elif x[0] == x[3] and x[1] == x[4]:
    y = True
  elif x[0] == x[3] and x[2] == x[4]:
    y = True
  elif x[0] == x[4] and x[1] == x[2]:
    y = True
  elif x[0] == x[4] and x[1] == x[3]:
    y = True
  elif x[0] == x[4] and x[2] == x[3]:
    y = True
  elif x[1] == x[2] and x[3] == x[4]:
    y = True
  elif x[1] == x[3] and x[2] == x[4]:
    y = True
  elif x[1] == x[4] and x[2] == x[3]:
    y = True
  return y

def full(x):
  y = False
  if x[0] == x[1] and x[0] == x[2] and x[3] == x[4]:
    y = True
  elif x[0] == x[1] and x[0] == x[3] and x[2] == x[4]:
    y = True
  elif x[0] == x[1] and x[0] == x[4] and x[2] == x[3]:
    y = True
  elif x[0] == x[2] and x[0] == x[3] and x[1] == x[4]:
    y = True
  elif x[0] == x[2] and x[0] == x[4] and x[1] == x[3]:
    y = True
  elif x[0] == x[3] and x[0] == x[4] and x[1] == x[2]:
    y = True
  elif x[1] == x[2] and x[1] == x[3] and x[1] == x[4]:
    y = True 
  elif x[1] == x[2] and x[1] == x[4] and x[0] == x[3]:
    y = True 
  elif x[1] == x[3] and x[1] == x[4] and x[0] == x[2]:
    y = True 
  elif x[2] == x[3] and x[2] == x[4] and x[0] == x[1]:
    y = True
  return y   

def cinco(x):
  y = False
  for i in range(1,5):
    if x[i-1] == x[i]:
      y = True
    else:
      y = False
      break
  return y

prueba_poker()
for i in range(0,6):
  frec_poker[i] = frec_poker[i] / tamaño


frec_esperada_poker = [0.0001, 0.009, 0.072, 0.108, 0.504, 0.3024]

labels = ['Quintilla', 'Full', 'Pierna', 'Doble Par', 'Par', 'Todos Distintos']
x = np.arange(len(labels))

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, frec_poker, width, label='Obtenido')
ax.set_ylabel('')
ax.set_title('')
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.plot([0], [0.0001], label='Esperado', color="black")
plt.plot([0.5, 1.15], [0.009] * 2, color="black")
plt.plot([1.5, 2.15], [0.072] * 2, color="black")
plt.plot([2.5, 3.15], [0.108] * 2, color="black")
plt.plot([3.5, 4.15], [0.504] * 2, color="black")
plt.plot([4.5, 5.15], [0.3024] * 2, color="black")
plt.legend()
plt.show()



plt.plot(np.arange(tamaño), [0.5] * tamaño, label="Prom. esperado")
plt.plot( np.arange(tamaño), lista_prom, label="Prom. obtenido")
plt.ylim(0.4,0.6)
plt.xlabel("Números generados")
plt.ylabel("Promedio")
plt.legend()
plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random

frec = [0,0,0,0,0,0,0,0,0,0]
lista = np.array([])
lista_prom = np.array([])

def randu(seed, n):
    x = seed
    global lista
    global lista_prom
    #lista = np.append(lista, (x / (pow(2, 31) - 1)))
    for i in range(0,n):
        #x = pow(7,5) * x % (pow(2, 31) - 1)
        y = np.random.rand()
        if y >=0 and y < 0.1:
            frec[0] = frec[0] + 1
        elif y >=0.1 and y < 0.2:
            frec[1] = frec[1] + 1
        elif y >=0.2 and y < 0.3:
            frec[2] = frec[2] + 1
        elif y >=0.3 and y < 0.4:
            frec[3] = frec[3] + 1
        elif y >=0.3 and y < 0.5:
            frec[4] = frec[4] + 1
        elif y >=0.5 and y < 0.6:
            frec[5] = frec[5] + 1
        elif y >=0.6 and y < 0.7:
            frec[6] = frec[6] + 1
        elif y >=0.7 and y < 0.8:
            frec[7] = frec[7] + 1
        elif y >=0.8 and y < 0.9:
            frec[8] = frec[8] + 1
        elif y >=0.9 and y <= 1:
            frec[9] = frec[9] + 1
        lista = np.append(lista, y)
        if(i == 0):
            lista_prom = np.append(lista_prom, lista[i])
        else:
            lista_prom = np.append(lista_prom, sum(lista)/i)
    return lista

tamaño = 10000
randu(1537827, tamaño)
x = []

for i in range(0,10):
  x.append(i/10)

a_frec = np.array(frec)
plt.bar(x, a_frec/tamaño, align='center', width=0.09)
plt.xticks(x)
plt.show()

plt.plot(lista[0:tamaño:2], lista[1:tamaño:2], 'o')
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

frec_poker = [0,0,0,0,0,0]

def prueba_poker():
  global lista
  global tamaño
  for i in range(0, tamaño):
    x = str(lista[i])[2:7]
    if cinco(x):
      frec_poker[0] += 1
    elif full(x):
      frec_poker[1] += 1
    elif pierna(x):
      frec_poker[2] += 1
    elif doble_par(x):
      frec_poker[3] += 1
    elif par(x):
      frec_poker[4] += 1
    else:
      frec_poker[5] += 1
       

def par(x):
  y = False
  for i in range(0,5):
    for j in range(0,5):
      if x[i] == x[j] and i != j:
        y = True
  return y

def pierna(x):
  y = False
  if x[0] == x[1] and x[0] == x[2]:
    y = True
  if x[0] == x[1] and x[0] == x[3]:
    y = True
  if x[0] == x[1] and x[0] == x[4]:
    y = True
  if x[0] == x[2] and x[0] == x[3]:
    y = True
  if x[0] == x[2] and x[0] == x[4]:
    y = True
  if x[0] == x[3] and x[0] == x[4]:
    y = True
  if x[1] == x[2] and x[1] == x[3]:
    y = True
  if x[1] == x[2] and x[1] == x[4]:
    y = True
  if x[1] == x[3] and x[1] == x[4]:
    y = True
  if x[2] == x[3] and x[2] == x[4]:
    y = True
  return y 

def doble_par(x):
  y = False
  if x[0] == x[1] and x[2] == x[3]:
    y = True
  elif x[0] == x[1] and x[2] == x[4]:
    y = True
  elif x[0] == x[1] and x[3] == x[4]:
    y = True
  elif x[0] == x[2] and x[1] == x[3]:
    y = True
  elif x[0] == x[2] and x[1] == x[4]:
    y = True
  elif x[0] == x[2] and x[3] == x[4]:
    y = True
  elif x[0] == x[3] and x[1] == x[2]:
    y = True
  elif x[0] == x[3] and x[1] == x[4]:
    y = True
  elif x[0] == x[3] and x[2] == x[4]:
    y = True
  elif x[0] == x[4] and x[1] == x[2]:
    y = True
  elif x[0] == x[4] and x[1] == x[3]:
    y = True
  elif x[0] == x[4] and x[2] == x[3]:
    y = True
  elif x[1] == x[2] and x[3] == x[4]:
    y = True
  elif x[1] == x[3] and x[2] == x[4]:
    y = True
  elif x[1] == x[4] and x[2] == x[3]:
    y = True
  return y

def full(x):
  y = False
  if x[0] == x[1] and x[0] == x[2] and x[3] == x[4]:
    y = True
  elif x[0] == x[1] and x[0] == x[3] and x[2] == x[4]:
    y = True
  elif x[0] == x[1] and x[0] == x[4] and x[2] == x[3]:
    y = True
  elif x[0] == x[2] and x[0] == x[3] and x[1] == x[4]:
    y = True
  elif x[0] == x[2] and x[0] == x[4] and x[1] == x[3]:
    y = True
  elif x[0] == x[3] and x[0] == x[4] and x[1] == x[2]:
    y = True
  elif x[1] == x[2] and x[1] == x[3] and x[1] == x[4]:
    y = True 
  elif x[1] == x[2] and x[1] == x[4] and x[0] == x[3]:
    y = True 
  elif x[1] == x[3] and x[1] == x[4] and x[0] == x[2]:
    y = True 
  elif x[2] == x[3] and x[2] == x[4] and x[0] == x[1]:
    y = True
  return y   

def cinco(x):
  y = False
  for i in range(1,5):
    if x[i-1] == x[i]:
      y = True
    else:
      y = False
      break
  return y

prueba_poker()
for i in range(0,6):
  frec_poker[i] = frec_poker[i] / tamaño


frec_esperada_poker = [0.0001, 0.009, 0.072, 0.108, 0.504, 0.3024]

labels = ['Quintilla', 'Full', 'Pierna', 'Doble Par', 'Par', 'Todos Distintos']
x = np.arange(len(labels))

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, frec_poker, width, label='Obtenido')
ax.set_ylabel('')
ax.set_title('')
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.plot([0], [0.0001], label='Esperado', color="black")
plt.plot([0.5, 1.15], [0.009] * 2, color="black")
plt.plot([1.5, 2.15], [0.072] * 2, color="black")
plt.plot([2.5, 3.15], [0.108] * 2, color="black")
plt.plot([3.5, 4.15], [0.504] * 2, color="black")
plt.plot([4.5, 5.15], [0.3024] * 2, color="black")
plt.legend()
plt.show()



plt.plot(np.arange(tamaño), [0.5] * tamaño, label="Prom. esperado")
plt.plot( np.arange(tamaño), lista_prom, label="Prom. obtenido")
plt.ylim(0.4,0.6)
plt.xlabel("Números generados")
plt.ylabel("Promedio")
plt.legend()
plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as rand

frec = [0,0,0,0,0,0,0,0,0,0]


def randu(seed, n):
    x = seed
    lista = []
    lista_prom = []
    lista.append(x / (pow(2, 31) - 1))
    for i in range(0,n):
        x = pow(7,5) * x % (pow(2, 31) - 1)
        y = x / (pow(2, 31) - 1)
        if y >=0 and y < 0.1:
            frec[0] = frec[0] + 1
        elif y >=0.1 and y < 0.2:
            frec[1] = frec[1] + 1
        elif y >=0.2 and y < 0.3:
            frec[2] = frec[2] + 1
        elif y >=0.3 and y < 0.4:
            frec[3] = frec[3] + 1
        elif y >=0.3 and y < 0.5:
            frec[4] = frec[4] + 1
        elif y >=0.5 and y < 0.6:
            frec[5] = frec[5] + 1
        elif y >=0.6 and y < 0.7:
            frec[6] = frec[6] + 1
        elif y >=0.7 and y < 0.8:
            frec[7] = frec[7] + 1
        elif y >=0.8 and y < 0.9:
            frec[8] = frec[8] + 1
        elif y >=0.9 and y <= 1:
            frec[9] = frec[9] + 1
        lista.append(y)
        if(i == 0):
            lista_prom.append(y)
        else:
            lista_prom.append(sum(lista)/i)
    return lista_prom

tamaño = 10000

for i in range(10): 
  lista_prom = []
  lista_prom = randu(rand.randint(1,10000), tamaño)
  print(lista_prom)
  plt.plot(np.arange(tamaño), lista_prom)

plt.plot(np.arange(tamaño), [0.5] * tamaño, label="Prom. esperado")
plt.ylim(0.4,0.6)
plt.xlabel("Números generados")
plt.ylabel("Promedio")
plt.legend()
plt.show()

