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
    return {'graph':gr.newGraph(datastructure="ADJ_LIST",directed=True),'list_individuals':None,'hash_table_ocurrence':None}


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


def req_1(data_structs,origen,destino):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    dist=0
    contador=1
    grafo=dfs.DepthFirstSearch(data_structs["graph"],origen)
    pila=dfs.pathTo(grafo,destino)
    nodo=origen
    total_seg=0
    total_enc=0
    salida=st.newStack()
    size=st.size(pila) 
    xcosa=st.pop(pila)
    st.push(salida,xcosa)
    lista_lobos=lt.newList()

    while pila is not None and not lt.isEmpty(pila):
        nodo2=st.pop(pila)
        edge=round(gr.getEdge(data_structs["graph"],nodo,nodo2)["weight"],3)
        dist+=edge
        ide=nodo
        lon=nodo[:8].replace("m","-").replace("p",".")
        lat=nodo[9:15].replace("m","-").replace("p",".")
        num_ind=gr.degree(data_structs["graph"],nodo)
        lobos_adj=gr.adjacents(data_structs["graph"],nodo)
        e=0

        for j in lt.iterator(lobos_adj):
            if e<3 or (e<= lt.size(lobos_adj) and e>=lt.size(lobos_adj)-3):
                lt.addLast(lista_lobos,j)
            e+=1


        dicci={"id":ide,"longitud":lon,"latitud":lat,"numero individuos":num_ind,"lobos":lista_lobos,"distancia al siguiente vértice":edge,"siguiente vértice":nodo2}
        if edge !=0:
            total_seg+=1
        else:
            total_enc+=1

        if contador <5 or (contador <= size and contador>=size-5):
            st.push(salida,dicci)

        nodo=nodo2
        contador+=1
    tupla=(dist,total_enc,total_seg,salida)
    return tupla

def req_2(data_structs,origen,destino):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    dist=0
    contador=1
    grafo=bf.BellmanFord(data_structs["graph"],origen)
    pila=bf.pathTo(grafo,destino)
    total_seg=0
    total_enc=0
    salida=st.newStack()
    size=st.size(pila) 
    lista_lobos=lt.newList()
    reves=st.newStack()
    for w in lt.iterator(pila):
        st.push(reves,w)
    for e in lt.iterator(reves):
        edge=round(e["weight"])
        dist+=edge
        ide=e["vertexA"]
        lon=e["vertexA"][:8].replace("m","-").replace("p",".")
        lat=e["vertexA"][9:15].replace("m","-").replace("p",".")
        num_ind=gr.degree(data_structs["graph"],e["vertexA"])
        lobos_adj=gr.adjacents(data_structs["graph"],e["vertexA"])
        i=0

        for j in lt.iterator(lobos_adj):
            if i<3 or (i<= lt.size(lobos_adj) and i>=lt.size(lobos_adj)-3):
                lt.addLast(lista_lobos,j)
            i+=1


        dicci={"id":ide,"longitud":lon,"latitud":lat,"numero individuos":num_ind,"lobos":lista_lobos,"distancia al siguiente vértice":edge,"siguiente vértice":e["vertexB"]}
        if edge !=0:
            total_seg+=1
        else:
            total_enc+=1

        if contador <5 or (contador <= size and contador>=size-5):
            st.push(salida,dicci)

        contador+=1
    for x in lt.iterator(salida):
        print(x)
    tupla=(dist,total_enc,total_seg,salida)
    return tupla

def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    
    sccmap, sc = kosaraju(data_structs) #Aca ya tenemos el sccmap en el que estan los IDCC con sus respectivas componentes
    oficial = top_5_scc(sccmap) #Y aca el top 5 de los IDCC que mas componentes tienen.
    
    llaves = mp.keySet(oficial)
    dataframe = lt.newList("ARRAY_LIST")
    
    #Este ciclo solo se hara 5 veces, por el top 5
    for key2 in lt.iterator(llaves): #Aca vamos a recorrer la lista de codigos en los 5 casos. Para extraer la info de cada uno.
        longitudes = lt.newList("ARRAY_LIST")
        latitudes = lt.newList("ARRAY_LIST")
        wolfs_id = lt.newList("ARRAY_LIST")
        entry = mp.get(oficial, key2)
        lista = me.getValue(entry)
        
        for node in lt.iterator(lista):
            longitude, latitude, id_animal = extract_info(node) #Extraccion de latitudes, codigos de lobo y longitudes.
            lt.addLast(latitudes, float(latitude))
            lt.addLast(longitudes, float(longitude))
            if id_animal not in wolfs_id["elements"] and id_animal != '':
                lt.addLast(wolfs_id, id_animal)        
        
        wolf_count = lt.size(wolfs_id)
        top3_nodes = lt.subList(lista, 0, 3)
        bot3_nodes = lt.subList(lista, lt.size(lista)-2, 3)
        
        #Para evitar tener que recorrer todas las listas buscando por el max y el min.
        #QUise utilizar minpq pero no encontre maxpq asi q no lo implemente.
        max_lat = max(latitudes["elements"])
        max_long = max(longitudes["elements"])
        min_lat = min(latitudes["elements"])
        min_long = min(longitudes["elements"])
    
        if wolf_count <= 5:
            top3 = wolfs_id
            bot3 = top3
        #Esto es mera cortesia por si acaso hay mas de 5 lobos en la lista. pero no pasa.
        else:
            top3 = lt.subList(wolfs_id, 0, 3)
            bot3 = lt.subList(wolfs_id, (wolf_count)-2, 3)
                                        
        lista_final = lt.newList("ARRAY_LIST")
        ids_finales = lt.newList("ARRAY_LIST")
        for wolf in lt.iterator(data_structs["list_individuals"]):
            for t3 in lt.iterator(top3):
                #Comprobamos que el del top sea el mismo que el de la lista final 
                #y si lo es le quitamos el id a la lista y lo metemos en la lista final de lobos.
                if wolf["animal-id"] in t3 and wolf["animal-id"] not in ids_finales["elements"]: #Para que no se repitan los lobos
                    lt.addLast(lista_final, wolf)
                    lt.addLast(ids_finales, wolf["animal-id"])
                
        #Esto ya es para el view
        lista_lobos = lt.newList("ARRAY_LIST")
        
        for wolf in lt.iterator(lista_final):
            w_id = wolf["animal-id"]
            w_sex = wolf["animal-sex"]
            w_life = wolf["animal-life-stage"]
            w_study = wolf["study-site"]
            w_comments = wolf["deployment-comments"]
            lt.addLast(lista_lobos, [w_id, w_sex, w_life, w_study, w_comments])
            
        lista_lobos_def = lista_lobos_fix(lista_lobos)
        headers=["individual-id", "animal-sex", "animal-life-stage", "study-site", "deployment-comments"]
        #Empaquetamos la lista ya tabulada para no tener que hacer mas ciclos en el view.
        lista_lobos_tabulada = tb.tabulate(lista_lobos_def["elements"], headers=headers, maxheadercolwidths= [12, 12, 12, 12, 15], maxcolwidths= [12, 12, 12, 12, 15], tablefmt="fancy_grid")
        #Sacamos las demas variables que necesitamos para el view.
        nodes = get_nodes(top3_nodes, bot3_nodes) 
        entry_idsc = mp.get(sc["idscc"], lt.firstElement(top3_nodes))
        idscc = me.getValue(entry_idsc)
        lt.addLast(dataframe, [idscc, nodes, key2, min_lat, max_lat, \
            min_long, max_long, wolf_count, lista_lobos_tabulada])
    return dataframe

def kosaraju(data_structs):
    
    """Genera el mapa de componentes fuertemente conectadas
    utilizando el algoritmo de kosaraju."""
    
    sc = scc.KosarajuSCC(data_structs["graph"])
    scmarked = sc["marked"]
    marks = lt.newList("ARRAY_LIST")
    componentes = sc["idscc"]
    sccmap = mp.newMap(maptype="PROBING")
    for key in lt.iterator(mp.keySet(componentes)):
        entry = mp.get(componentes, key)
        valor = me.getValue(entry)
        if lt.isPresent(marks, valor) == 0:
            lt.addLast(marks, valor)
            comp_list = lt.newList("ARRAY_LIST")
            lt.addLast(comp_list, key)
            mp.put(sccmap, valor, comp_list)
        else: 
            entry1 = mp.get(sccmap, valor)
            value1 = me.getValue(entry1)
            lt.addLast(value1, key)
            
    return sccmap, sc

def top_5_scc(sccmap):
    
    """Genera el top 5 de las componentes fuertemente conectadas.
    Recorriendo el mapa de componentes fuertemente conectadas y extrayendo las que
    mas tienen nodos adentro."""
    
    lista_cc = lt.newList("ARRAY_LIST")
    size_list = lt.newList("ARRAY_LIST")
    ofcval = mp.newMap(maptype="PROBING")
    oficial = mp.newMap(maptype="PROBING")
    for key1 in lt.iterator(mp.keySet(sccmap)):
        lt.addLast(lista_cc, key1)
        entry = mp.get(sccmap, key1)
        lst = me.getValue(entry)
        size = lt.size(lst)
        lt.addLast(size_list, size)
        mp.put(ofcval, size, lst)
    size_list = sorted(size_list["elements"], reverse=True)
    for i in range(0, 5):
        mp.put(oficial, size_list[i], me.getValue(mp.get(ofcval, size_list[i])))
    
    return oficial

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
    
    """Recibe los top 3 y bot 3 de los nodos 
    y devuelve el formato deseado para el view"""
    
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
    
    for element in lt.iterator(lista_lobos):
        for i in range(len(element)):#Aca tenemos el individual-id, animal sex etc. 
            if element[i] == '':#Osea se chequea por cada atributo que tenga el lobo
                element[i] = 'Unknown'

    return lista_lobos
    
def req_4(data_structs,lon_lat_1,lon_lat_2):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4

    lon_lat_1_list=lt.newList(datastructure='ARRAY_LIST')
    lon_lat_2_list=lt.newList(datastructure='ARRAY_LIST')

    for i in lt.iterator(data_structs['list_hiper_nodes']):
        lt.addLast(lon_lat_1_list,(i,haversine_equation(i[0],i[1],lon_lat_1[0],lon_lat_1[1])))
        lt.addLast(lon_lat_2_list,(i,haversine_equation(i[0],i[1],lon_lat_2[0],lon_lat_2[1])))

    lon_lat_1_nearest=lt.firstElement(quk.sort(lon_lat_1_list,cmp_harvesine))
    lon_lat_2_nearest=lt.firstElement(quk.sort(lon_lat_2_list,cmp_harvesine))
    
    lon_lat_1_nearest_converted=str(str(lon_lat_1_nearest[0][0])+'_'+str(lon_lat_1_nearest[0][1])).replace('.','p').replace('-','m')
    lon_lat_2_nearest_converted=str(str(lon_lat_2_nearest[0][0])+'_'+str(lon_lat_2_nearest[0][1])).replace('.','p').replace('-','m')
  
    graph_search=djk.Dijkstra(data_structs['graph'],lon_lat_1_nearest_converted)
    total_weight=djk.distTo(graph_search,lon_lat_2_nearest_converted)
    list_vertices_path=lt.newList(datastructure='ARRAY_LIST')
    
    for j in lt.iterator(djk.pathTo(graph_search,lon_lat_2_nearest_converted)):
        lt.addLast(list_vertices_path,j)

    hiper_nodes_route=lt.newList(datastructure='ARRAY_LIST')
    number_nodes_individuals=lt.newList(datastructure='ARRAY_LIST')
    for k in lt.iterator(list_vertices_path):
        vertex_A=k['vertexA'].split('_')
        vertex_B=k['vertexB'].split('_')

        if k['weight']==0 and len(vertex_A)==2:
                lt.addLast(hiper_nodes_route,k['vertexA'])
        else:
            if len(vertex_A)==6:
                lt.addLast(number_nodes_individuals,vertex_A[2]+'_'+vertex_A[3]+'_'+vertex_A[4]+'_'+vertex_A[5])
            elif len(vertex_A)==5:
                lt.addLast(number_nodes_individuals,vertex_A[2]+'_'+vertex_A[3]+'_'+vertex_A[4])
            else:
                lt.addLast(number_nodes_individuals,vertex_A[2]+'_'+vertex_A[3])    

        if k['weight']==0 and len(vertex_B)==2:
                lt.addLast(hiper_nodes_route,k['vertexB'])      
        else:
            if len(vertex_B)==6:
                lt.addLast(number_nodes_individuals,vertex_B[2]+'_'+vertex_B[3]+'_'+vertex_B[4]+'_'+vertex_B[5])
            elif len(vertex_B)==5:
                lt.addLast(number_nodes_individuals,vertex_B[2]+'_'+vertex_B[3]+'_'+vertex_B[4])
            else:
                lt.addLast(number_nodes_individuals,vertex_B[2]+'_'+vertex_B[3])    

           
    hiper_nodes_route=list(set(hiper_nodes_route['elements']))
    number_nodes_individuals=len(set(number_nodes_individuals['elements']))
    total_segments=(list_vertices_path['size'])-1
    
    list_3_first_last=lt.newList(datastructure='ARRAY_LIST')

    for i in set(hiper_nodes_route[:3]+hiper_nodes_route[-3:]):
        row=lt.newList(datastructure='ARRAY_LIST')
        list_adjacents_size=gr.adjacents(data_structs['graph'],i)
        adjacents_array=lt.newList(datastructure='ARRAY_LIST')
        coordinates=i.split('_')
        lon=float(coordinates[0].replace('m','-').replace('p','.'))
        lati=float(coordinates[1].replace('m','-').replace('p','.'))

        for j in lt.iterator(list_adjacents_size):
            lt.addLast(adjacents_array,j)
        lt.addLast(row,i)
        lt.addLast(row,lon)
        lt.addLast(row,lati)
        lt.addLast(row,list_adjacents_size['size'])
        lt.addLast(row,adjacents_array['elements'])
        
        list_hiper_node_nearest=lt.newList(datastructure='ARRAY_LIST')
        for o in lt.iterator(data_structs['list_hiper_nodes']):
            lt.addLast(list_hiper_node_nearest,(o,haversine_equation(o[0],o[1],lon,lati)))

        list_hiper_node_nearest=quk.sort(list_hiper_node_nearest,cmp_harvesine)['elements'][1]
        lt.addLast(row,list_hiper_node_nearest[1])
        lt.addLast(list_3_first_last,row['elements'])
    
    return lon_lat_1_nearest[1], lon_lat_2_nearest[1], total_weight, len(hiper_nodes_route), number_nodes_individuals,total_segments,list_3_first_last['elements']


def req_5(data_structs,origen,distancia,numero):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    distancia=distancia/2
    estructura=prim.PrimMST(data_structs["graph"],origen)
    algo=prim.scan(data_structs["graph"],estructura,origen)
    dist=0
    puntos=0
    ind=0
    mapa=mp.newMap()
    lista_ind=lt.newList()
    lista_puntos=lt.newList()
    #print(estructura)
    for a in lt.iterator(algo["keys"]): 
        lt.addLast(lista_puntos,a)
        puntos+=1
        ind=gr.degree(data_structs["graph"],a)
        lt.addLast(ind)
        for j in lt.iterator(algo["values"]):
            dist+=j["index"]


        mp.put(mapa,"número de puntos",puntos)
        mp.put(mapa,"distancia recorrida",dist)
        mp.put(mapa,"listado de puntos",lista_puntos)
        mp.put(mapa,"número de individuos",lista_ind)
        if (dist<=distancia or dist>distancia-5) and (puntos>numero):
            return mapa


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
def first_3_last_3(data_structs,lista):
    list_=lt.newList(datastructure='ARRAY_LIST')
    for p in set(lista[:3]+lista[-3:]):
        row=lt.newList(datastructure='ARRAY_LIST')
        list_adjacents_size=gr.adjacents(data_structs['graph'],p)
        adjacents_array=lt.newList(datastructure='ARRAY_LIST')
        coordinates=p.split('_')
        lon=float(coordinates[0].replace('m','-').replace('p','.'))
        lati=float(coordinates[1].replace('m','-').replace('p','.'))

        for j in lt.iterator(list_adjacents_size):
            lt.addLast(adjacents_array,j)
        
        lt.addLast(row,p)
        lt.addLast(row,lon)
        lt.addLast(row,lati)
        lt.addLast(row,list_adjacents_size['size'])
        lt.addLast(row,adjacents_array['elements'])
        lt.addLast(list_,row['elements'])
    return list_['elements']

def cmp_hash_table(data_1,data_2):
    return data_1['value']['size']>=data_2['value']['size']

def cmp_lon_lat(data_1,data_2):
    return data_1<=data_2

def cmp_harvesine(data_1,data_2):
    return data_1[1]<=data_2[1]
