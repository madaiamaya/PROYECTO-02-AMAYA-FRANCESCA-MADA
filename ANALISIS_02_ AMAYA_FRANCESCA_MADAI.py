# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:55:10 2022

@author: pnk_wffls, Francesca Madai Amaya
"""
'''
register_id,direction,origin,destination,year,date,product,transport_mode,company_name,total_value
'''
import pandas as pd
pd.set_option('display.max_rows',200)

import seaborn as sns
import matplotlib.pyplot as plt


with open('synergy_logistics_database.csv',encoding='utf-8-sig') as synergy_database:
    syn_df=pd.read_csv(synergy_database,index_col=0,header=0,parse_dates=[4,5])

#%%
'''
Aqui voy a obstener el total de imports y exprts para poder tener un puno de comparacion
para el punto 3 en el que se debe enfocar en los paises que generan el 80% del valor total
'''


total_by_direction=syn_df.groupby(['direction']).sum()
total_by_direction['80%']=total_by_direction['total_value']*0.8
total_exports=syn_df[syn_df['direction']=='Exports'].copy()
total_imports=syn_df[syn_df['direction']=='Imports'].copy()

print(f'''
      
      Valor total de exportaciones e importaciones
      {total_by_direction}
      
      ''')


#%%
'''
En este bloque se analizara el punto 2 y nos enofcaremos en los medios de transporte
que aporten mayor valor a synergy logistics. Para eso hare un nuevo dataframe agrupado
especififcamente por medio de transporte y lo ordenare sus valores.
'''
total_por_transporte=syn_df.groupby(['direction','transport_mode']).sum()
exports_por_transporte=total_exports.groupby(['transport_mode']).sum()
imports_por_transporte=total_imports.groupby(['transport_mode']).sum()

exports_por_transporte.sort_values(by=['total_value'],inplace=True,ascending=False)
imports_por_transporte.sort_values(by=['total_value'],inplace=True,ascending=False)


print(f'''
      Lista de importaciones por medio de transporte
      {imports_por_transporte}
      
      Lista de exportaciones por medio de transporte
      {exports_por_transporte}    
      ''')

# PLOT DE MEDIO DE TRANSPORTE

g_exports_by_transport = sns.barplot(x='transport_mode',y='total_value',hue='transport_mode',data=total_exports)
plt.show()       

g_imports_by_transport= sns.barplot(x='transport_mode',y='total_value',hue='transport_mode',data=total_imports)
plt.show()       


#%%
'''
Para poder enofcarse en el top 100 de rutas se debe primero crear los nuevo datafrmes 
usando solo las categorias que necesito para el analisis, que en este caso son
'origin','destination' y 'transport_mode'
'''


exports_por_ruta=total_exports.groupby(['origin','destination','transport_mode']).sum()
imports_por_ruta=total_imports.groupby(['origin','destination','transport_mode']).sum()
# exports_por_ruta['Acumulado']=exports_por_ruta['total_value'].sumcum()
exports_por_ruta.sort_values(by=['total_value'],inplace=True,ascending=False)
imports_por_ruta.sort_values(by=['total_value'],inplace=True,ascending=False)

print(f'''
      Top 10 rutas de importacion
      {imports_por_ruta.head(10)}
      
      Top 10 rutas de exportacion
      {exports_por_ruta.head(10)}
      
      ''')
      
#%%
#analisis por pais

export_por_pais=total_exports.groupby(['origin']).sum()
import_por_pais=total_imports.groupby(['origin']).sum()
export_por_pais.sort_values(by=['total_value'],inplace=True,ascending=False)
import_por_pais.sort_values(by=['total_value'],inplace=True,ascending=False)


print(f'''
      Top 10 paises importadores
      {import_por_pais.head(10)}
      
      Top 10 paises exportadores
      {export_por_pais.head(10)}
      
      ''')







