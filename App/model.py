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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from math import radians, cos, sin, asin, sqrt
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import bellmanford as bf
from DISClib.Algorithms.Graphs import bfs
from DISClib.Algorithms.Graphs import dfs
from DISClib.Algorithms.Graphs import prim
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
import tabulate as tb

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos
'''
"ADJ_LIST"
"ADJ_MTX": ".adjlist"
'''
def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    return gr.newGraph(datastructure="ADJ_MTX",directed=True)


# Funciones para agregar informacion al modelo

def add_data(hash_table_per_wolf,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista

    if mp.contains(hash_table_per_wolf,data['individual-id']):
        lt.addLast(mp.get(hash_table_per_wolf,data['individual-id'])['value'],data)
    else:
        value=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(value,data)
        mp.put(hash_table_per_wolf,data['individual-id'],value)
    return hash_table_per_wolf

def add_data_hiper_nodes(hash_table_per_wolf,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista

    if mp.contains(hash_table_per_wolf,data['individual-id']):
        lt.addLast(mp.get(hash_table_per_wolf,data['individual-id'])['value'],data['lon_lat'])
    else:
        value=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(value,data['lon_lat'])
        mp.put(hash_table_per_wolf,data['individual-id'],value)
    return hash_table_per_wolf

def add_data_special(hash_table_per_wolf,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista

    if mp.contains(hash_table_per_wolf,data):
        mp.get(hash_table_per_wolf,data)['value']['size']+=1
    else:
        value=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(value,0)
        mp.put(hash_table_per_wolf,data,value)
    return hash_table_per_wolf

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    hola= bfs.BreadhtFisrtSearch(data_structs,"m111p862_57p449")
    
    return bfs.hasPathTo(hola,"m111p908_57p427")
    #return djk.pathTo(data_structs,'m111p439_56p912_13792_13792')

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass

#& CHECKLIST

#*SCID
#*SCC size
#TODO latitudes (Solo falta hacer el for para que recorra los codigos y arme una lista con ellos, ya con lista ez)
#^wolf count EZ
#!INTERPRETAR LOS DATOS DE CODIGOS con _
#TODO Con la lista de codigos y cosas verificar que lobos estan ahi y agregarlos a la lista de lobos.
#? DICCIONARIO PARA EMPAQUETAR LOS TOP WOLFS
#TODO Node ids (Mostrar top 3 y bot 3 en view)
#? TABULAR

def req_3(data_structs, wolf_list):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    
    #&KOSARAJU
    #&___________________________.....___________________________
    
    sc = scc.KosarajuSCC(data_structs)
    scmarked = sc["marked"]
    marcas = lt.newList("ARRAY_LIST")
    componentes = sc["idscc"]
    sccmap = mp.newMap(maptype="PROBING")
    
    for llave in lt.iterator(mp.keySet(componentes)):
        entry = mp.get(componentes, llave)
        valor = me.getValue(entry)
        if lt.isPresent(marcas, valor) == 0:
            lt.addLast(marcas, valor)
            comp_list = lt.newList("ARRAY_LIST")
            lt.addLast(comp_list, llave)
            mp.put(sccmap, valor, comp_list)
        else: 
            entry1 = mp.get(sccmap, valor)
            lst = me.getValue(entry1)
            lt.addLast(lst, llave)
            
    #Aca ya tenemos el sccmap en el que estan los IDCC con sus respectivas componentes
    #&TOP 5
    #&___________________________.....___________________________
    
    lista_cc = lt.newList("ARRAY_LIST")
    size_list = lt.newList("ARRAY_LIST")
    ofcval = mp.newMap(maptype="PROBING")
    oficial = mp.newMap(maptype="PROBING")
    for llave in lt.iterator(mp.keySet(sccmap)):
        lt.addLast(lista_cc, llave)
        entry = mp.get(sccmap, llave)
        lst = me.getValue(entry)
        size = lt.size(lst)
        lt.addLast(size_list, size)
        mp.put(ofcval, size, lst)
    size_list = sorted(size_list["elements"], reverse=True)
    for i in range(0, 5):
        mp.put(oficial, size_list[i], me.getValue(mp.get(ofcval, size_list[i])))
    #Aca ya tenemos el top 5 de las componentes con mayor cantidad de individuos en la var oficial.
    
    #&EXTRACCION DE INFO DE LOS NODOS
    #&___________________________.....___________________________
    
    i = 0
    llaves = mp.keySet(oficial)
    dataframe = lt.newList("ARRAY_LIST")
    
    #Este ciclo solo se hara 5 veces
    for llave in lt.iterator(llaves):
        longitudes = lt.newList("ARRAY_LIST")
        latitudes = lt.newList("ARRAY_LIST")
        wolfs_id = lt.newList("ARRAY_LIST")
        entry = mp.get(oficial, llave)
        lista = me.getValue(entry)
        
        #Aca vamos a recorrer la lista de codigos en los 5 casos. Para extraer
        #Latitudes, codigos de lobo y longitudes.
        for node in lt.iterator(lista):
            
            longitude, latitude, id_animal = extract_info(node)
            
            lt.addLast(latitudes, float(latitude))
            lt.addLast(longitudes, float(longitude))
            
            if id_animal not in wolfs_id["elements"] and id_animal != '':
                lt.addLast(wolfs_id, id_animal)
            
    #&Variables para el view
    #&___________________________.....___________________________
        
        wolf_count = lt.size(wolfs_id)
                
        top3_nodes = lt.subList(lista, 0, 3)
        bot3_nodes = lt.subList(lista, lt.size(lista)-2, 3)
        
        max_lat = max(latitudes["elements"])
        max_long = max(longitudes["elements"])
        min_lat = min(latitudes["elements"])
        min_long = min(longitudes["elements"])
                
    #&Top 3 y bot 3 lobos
    #&___________________________.....___________________________
    
        if wolf_count <= 5:
            
            top3 = wolfs_id
            bot3 = top3
            
        #Esto es mera cortesia por si acaso hay mas de 5 lobos en la lista. pero no pasa.
        else:
            
            top3 = lt.subList(wolfs_id, 0, 3)
            bot3 = lt.subList(wolfs_id, (wolf_count)-2, 3)
                                        
        lista_final = lt.newList("ARRAY_LIST")
        for wolf in lt.iterator(wolf_list):
            
            for t3 in lt.iterator(top3):
                
                if wolf["animal-id"] in t3:
                    
                    lt.addLast(lista_final, wolf)
                
        #&Organizar lista lobos
        #&___________________________.....___________________________
        #Como esto ya es para el view usamos lista de python para facilizar el proceso.
        lista_lobos = []
        
        #Basicamente comprobamos que el del top sea el mismo que el de la lista final 
        # y si lo es le quitamos el id a la lista y lo metemos en el diccionario completo.
        
        for wolf in lt.iterator(lista_final):
            
            w_id = wolf["animal-id"]
            w_sex = wolf["animal-sex"]
            w_life = wolf["animal-life-stage"]
            w_study = wolf["study-site"]
            w_comments = wolf["deployment-comments"]
            
            lista_lobos.append([w_id, w_sex, w_life, w_study, w_comments])
            
        lista_lobos_def = lista_lobos_fix(lista_lobos)
        lista_lobos_tabulada = tb.tabulate(lista_lobos_def, headers=["individual-id", "animal-sex", "animal-life-stage", "study-site", "deployment-comments"],
                                           maxheadercolwidths= [12, 12, 12, 12, 15], maxcolwidths= [12, 12, 12, 12, 15], tablefmt="fancy_grid")
                    
        #Variables finales para el view
        nodes = get_nodes(top3_nodes, bot3_nodes)
        entry_idsc = mp.get(sc["idscc"], lt.firstElement(top3_nodes))
        idscc = me.getValue(entry_idsc)#Cualquier nodo su valor asignado en scc.
        lt.addLast(dataframe, [idscc, nodes, llave, min_lat, max_lat, \
            min_long, max_long, wolf_count, lista_lobos_tabulada])
        
    return dataframe
            
def extract_info(code):
    
    """Esta funcion va a extraer la informacion de los codigos de los lobos
    que estan en este formato: m111p439_56p912_1372_1379 o m111p496_57p353"""
    
    longitud = ''
    latitud = ''
    wolf_id = ''
    
    first_m = False
    first_p = False
    is_latitud = False
    is_wolf = False
    
    first_p_lat = False
    skip_first_underscore = False
    
    for letra in code:
        
        if not first_m or not first_p:
            
            if letra == 'm':
                
                longitud += '-'
                first_m = True
                
            
            
            elif letra == 'p':
                
                longitud += '.'
                first_p = True
                
            elif letra != 'p' and letra != 'm':
                
                longitud += letra
                
        #Aca comprobamos si ya se cumplio el primer if osea 
        #Ya se recorrio el m111p pero luego siguen los 3 digitos despues del .
        elif first_m and first_p and not is_latitud:
            
            if letra == '_':
                
                is_latitud = True
                
            else: 
                
                longitud += letra
            
        #Aca ya estamos en la siguiente iteracion que seria cuando 
        #Va despues del _ osea 57p474
        elif is_latitud and letra != '_' and not is_wolf:
            
            if not first_p_lat:
                    
                if letra == 'p':
                    
                    latitud += '.'
                    first_p_lat = True
                    
                else: 
                
                    latitud += letra
                    
            else: 
                
                latitud += letra
                    
        elif first_p_lat and not is_wolf:
            
            if letra == '_':
                
                is_wolf = True
                
            else: 
                
                latitud += letra
                
        if is_wolf and letra != '_' and skip_first_underscore == False:
            
            wolf_id += letra
            skip_first_underscore = True
            
        if is_wolf and skip_first_underscore:
            
            wolf_id += letra

    return longitud, latitud, wolf_id
    
def get_nodes(top3, bot3):
    
    "Recibe los top 3 y bot 3 de los nodos y devuelve el formato deseado para el view"
    
    final_string = ''
    
    first = True
    for node in lt.iterator(top3):
        
        if first:
            
          final_string += node
          
        else:
            
            final_string += ', ' + node
            
        first = False
        
    final_string += ','
    final_string += '...,'
        
    firstt = True
    for nodo in lt.iterator(bot3):
        
        if firstt:
            
          final_string += nodo
          
        else:
            
            final_string += ', ' + nodo
            
        firstt = False

    return final_string
    
def lista_lobos_fix(lista_lobos):
    
    """Recibe una lista de lobos y con esa lista cambia
    Los '' por unknown."""
    
    for element in lista_lobos:
        
        for i in range(len(element)):
            
            if element[i] == '':
                
                element[i] = 'Unknown'
                
    return lista_lobos
    
def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def cmp_Num(n1, n2):
    """
    Compara dos numeors
    """
    n1, n2 = int(n1), int(n2)
    if (n1 == n2):
        return 0
    elif (n1 > n2):
        return -1
    else:
        return 1
    
def cmpIDSSS(dato1,dato2):
    dato1 = dato1.split('-')
    dato2 = dato2.split('-')

    if  ('T' in dato1[0])and ('T' in dato2[0]):
       
        if (int(dato1[1]) > int(dato2[1])):
            
            return -1
        
        elif (int(dato1[1]) < int(dato2[1])):
            
            return 1
        
    elif ('T' in dato1[0]):
        
        return 1
    
    elif ('T' in dato2[0]):
        
        return -1
    
    elif (int(dato1[0]) == int(dato2[0])):
        
        if (dato1[1] > dato2[1]):
            
            return -1
        
        elif (dato1[1] < dato2[1]):
            
            return 1
        else:
            return 0
        
    elif (int(dato1[0]) > int(dato2[0])):

        return -1
    
    elif (int(dato1[0]) < int(dato2[0])):

        return 1
    
def cmp_time(data_1,data_2):
    return data_1['time_datetime']<=data_2['time_datetime']

def haversine_equation(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = radians(float(lon1)),radians(float(lat1)),radians(float(lon2)),radians(float(lat2))
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return c * r
