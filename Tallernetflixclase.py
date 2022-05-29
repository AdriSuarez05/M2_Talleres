# -*- coding: utf-8 -*-
"""
Created on Sat May 28 11:52:17 2022

@author: Adriana Suarez
"""

"""
email: adriana.suarezb@upb.edu.co
ID: 502197

"""

import pandas as pd

# 1. Lea la base de datos netflix_titles usando la librería “pandas”
my_data = pd.read_csv('netflix_titles.csv')

# 2. Imprima por consola las primeras y últimas 5 filas del arreglo.
print(my_data.head())
print(my_data.tail())


# 3. Imprima cada uno de los tipos de dato asociado a las etiquetas.
print(my_data.dtypes)


# 4.  Guarde un archivo .xlsx, en el cual el nombre del archivo sea “Netflix_list” y el nombre de la 
# hoja sea “títulos”
my_data.to_excel("Netflix_list.xlsx", sheet_name = "títulos", index=False)


# 5. Cree una nueva data frame en el cual segmente únicamente: el tipo, la duración,  
# la descripción y el país.

nuevadata = my_data[['type', 'duration', 'description', 'country']]


# 6. Haga un filtro para las películas que tienen una duración superior a 100 min

my_data["duracion"] = pd.to_numeric(my_data['duration'].replace('([^0-9]*)','', regex=True), errors='coerce')
dum = my_data[my_data['duracion'] > 100  ]
print(dum)

# 7. Haga un filtro para los “TV Shows” que tienen más de 3 temporadas.

#filtv = my_data[my_data[['type'] == 'TV Show' | ['duration'] >= '3 Seasons']]
filtv = my_data[(my_data['type'] == 'TV Show') & (my_data['duration'] > '3 Seasons' )]


# 8. Haga un filtro en el cual solo tenga en cuenta 2 categorías/etiquetas 
#(libre elección)

newopeli = my_data[['title', 'description']]


#9. Recuerde usar casos con indexación numérica y con texto (loc / iloc)
my_data.iloc[:6, 8] = 'none'
print(my_data.head())

my_data.loc[:2, 'country'] = 'nan'
print(my_data.head())


# 10. Modifique los valores del ID de las 5 primeras y las 5 últimas “shows” 
#y de cualquier otra etiqueta de su elección (solo un valor). 
my_data.iloc[:5, 0] = 's5'
my_data.loc[:8801, 'show id'] = 'nan'
my_data.iloc[:1, 9] = '1 Hour 30 min'


# 11. Añada una nueva columna “Visto”, en la cual debe colocar 1/0 
#(aleatorio) si vio o no el show (simulación). 

                
import numpy as np

my_data["Visto"] = np.random.randint(0, 2, my_data.shape[0])
                
                
                