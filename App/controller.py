"""
* Copyright 2020, Departamento de sistemas y Computación,
* Universidad de Los Andes
*
*
* Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
*
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along withthis program.  If not, see <http://www.gnu.org/licenses/>.
"""


import config as cf
import model
import time
from datetime import datetime
import csv
import tracemalloc
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import quicksort as quk
from DISClib.ADT import graph as gr
csv.field_size_limit(2147483647)


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""




def new_controller():
   """
   Crea una instancia del modelo
   """
   #TODO: Llamar la función del modelo que crea las estructuras de datos
   return model.new_data_structs()




# Funciones para la carga de datos


def load_data(control):
   """
   Carga los datos del reto
   """
   # TODO: Realizar la carga de datos
   raw_data = csv.DictReader(open("Data/wolfs/BA-Grey-Wolf-tracks-utf8-large.csv", encoding = "utf-8"), delimiter= ",")
   hash_table_per_wolf=mp.newMap(numelements=45,loadfactor=1,maptype='PROBING')
   hiper_nodes=lt.newList(datastructure="ARRAY_LIST")
   array_vertex=lt.newList(datastructure='ARRAY_LIST')
  
   for line in raw_data:
       line['time_datetime']=datetime.strptime(line['timestamp'],'%Y-%m-%d %H:%M')
       line['lon_lat']=(round(float(line['location-long']),4),round(float(line['location-lat']),4))
       lt.addLast(hiper_nodes,line['lon_lat'])
       model.add_data(hash_table_per_wolf,line)
   h_n= set()
   hiper_nodes_o = [x for x in hiper_nodes['elements'] if x in h_n or (h_n.add(x) or False)]
              
   for wolf in lt.iterator(hash_table_per_wolf['table']):
       if wolf['key']!=None:
           for j in lt.iterator(quk.sort(wolf['value'],model.cmp_time)):
               lt.addLast(array_vertex,str(str(j['lon_lat'][0])+'_'+str(j['lon_lat'][1])+'_'+j['individual-local-identifier']).replace('.','p').replace('-','m'))
   v_r = set()
   array_vertex_o = [x for x in array_vertex['elements'] if x in v_r or (v_r.add(x) or False)]  
   for i in array_vertex_o:
       gr.insertVertex(control,i)


   for ver in range(0,len(array_vertex_o)-1):
       s_list_1=array_vertex_o[ver].split('_')
       s_list_2=array_vertex_o[ver+1].split('_')
       gr.addEdge(control,array_vertex_o[ver],array_vertex_o[ver+1],model.haversine_equation(float(s_list_1[0].replace('m','-').replace('p','.')),float(s_list_1[1].replace('m','-').replace('p','.')),float(s_list_2[0].replace('m','-').replace('p','.')),float(s_list_2[1].replace('m','-').replace('p','.'))))




   for key in hiper_nodes_o:
    
       hiper_n=str(key[0]).replace('.','p').replace('-','m')+'_'+str(key[1]).replace('.','p').replace('-','m')
       gr.insertVertex(control,hiper_n)
       for q in array_vertex_o:
           d_split=q.split('_')
           if d_split[0]+'_'+d_split[1]==hiper_n:
               gr.addEdge(control,q,hiper_n,0)


   return control


# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo


def get_data(control, id):
   """
   Retorna un dato por su ID.
   """
   #TODO: Llamar la función del modelo para obtener un dato
   pass




def req_1(control):
   """
   Retorna el resultado del requerimiento 1
   """
   # TODO: Modificar el requerimiento 1
   pass




def req_2(control):
   """
   Retorna el resultado del requerimiento 2
   """
   # TODO: Modificar el requerimiento 2
   pass




def req_3(control):
   """
   Retorna el resultado del requerimiento 3
   """
   # TODO: Modificar el requerimiento 3
   pass




def req_4(control):
   """
   Retorna el resultado del requerimiento 4
   """
   # TODO: Modificar el requerimiento 4
   pass




def req_5(control):
   """
   Retorna el resultado del requerimiento 5
   """
   # TODO: Modificar el requerimiento 5
   pass


def req_6(control):
   """
   Retorna el resultado del requerimiento 6
   """
   # TODO: Modificar el requerimiento 6
   pass




def req_7(control):
   """
   Retorna el resultado del requerimiento 7
   """
   # TODO: Modificar el requerimiento 7
   pass




def req_8(control):
   """
   Retorna el resultado del requerimiento 8
   """
   # TODO: Modificar el requerimiento 8
   pass




# Funciones para medir tiempos de ejecucion


def get_time():
   """
   devuelve el instante tiempo de procesamiento en milisegundos
   """
   return float(time.perf_counter()*1000)




def delta_time(start, end):
   """
   devuelve la diferencia entre tiempos de procesamiento muestreados
   """
   elapsed = float(end - start)
   return elapsed


def get_memory():
   """
   toma una muestra de la memoria alocada en instante de tiempo
   """
   return tracemalloc.take_snapshot()




def delta_memory(stop_memory, start_memory):
   """
   calcula la diferencia en memoria alocada del programa entre dos
   instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
   """
   memory_diff = stop_memory.compare_to(start_memory, "filename")
   delta_memory = 0.0


   # suma de las diferencias en uso de memoria
   for stat in memory_diff:
       delta_memory = delta_memory + stat.size_diff
   # de Byte -> kByte
   delta_memory = delta_memory/1024.0
   return delta_memory
