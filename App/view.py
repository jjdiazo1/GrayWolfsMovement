﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
default_limit = 1000 
sys.setrecursionlimit(default_limit*100000)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    return controller.new_controller()


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    '''
    Todo esta ya hecho falta el print del view osea las palabras y eso pero la info esta alli, osea todo esta hecho solo falta mostrarlo. Esto del view 
    usualemnte lo hacemos al final del reto siempre , porque es la parte menos importante, entonces eimpre lo dejamos hasta el final, todo lo del view.
    '''
    control = controller.load_data(control)
    return control
   


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    origen = input("Ingrese el punto de origen: ")
    destino= input("Ingrese el punto de destino: ")
    final=controller.req_1(control,origen,destino)
    print(final)



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    origen = input("Ingrese el punto de origen: ")
    destino= input("Ingrese el punto de destino: ")
    final=controller.req_2(control,origen,destino)
    print(final)


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    
    dataframe = controller.req_3(control)
    
    headers = ['SCCID', 'Node IDs', 'min-lat', 'max-lat', 'min-lon', 'max-lon', 'wolf-count', 'wolf-details']
    
    print(tabulate(dataframe["elements"], headers = headers, maxheadercolwidths = [8, 17, 6, 8, 8, 8, 8, 8, 83], 
                      maxcolwidths = [8, 17, 8, 8, 8, 8, 8, 8, 83], showindex = False,
                      tablefmt = 'fancy_grid'))
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    origen= input("ingrese el punto de origen: ")
    distancia= float(input("ingrese la distancia a recorrer: "))
    numero= int(input("ingrese el número mínimo de puntos a inspeccionar: "))
    final=controller.req_5(control,origen,distancia,numero)
    print(final)


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    fecha_inicial = input("Ingrese la fecha inicial del análisis (formato YYYY-MM-DD): ")
    fecha_final = input("Ingrese la fecha final del análisis (formato YYYY-MM-DD): ")
    temperatura_minima = float(input("Ingrese la temperatura ambiente mínima (en grados centígrados): "))
    temperatura_maxima = float(input("Ingrese la temperatura ambiente máxima (en grados centígrados): "))

    headers_1_1=['individual-id','animal-taxon','animal-life-stage','animal-sex','study-name','total_distance','deployment-comments']

    x=controller.req_7(control,fecha_inicial,fecha_final,temperatura_minima,temperatura_maxima)
    print('El total de manadas reconocidas por sus movimientos y puntos de encuentro (componentes conectados) en el rango de fechas y temperatura ambiente dados.',x[0])
    headers = ["Num Puntos Encuentro","Los tres primeros y tres últimos puntos de encuentro reconocidos dentro del territorio","Num Individuos por manada","Los tres primeros y tres últimos miembros de la manada","Longitud min","Longitud max","Latitudes min","Latitudes max"]

    for i in x[1]:
        i[3]=tabulate_data_req7(i[3],headers_1_1)
    
    print(tabulate(x[1],headers,tablefmt='grid',stralign='center',maxheadercolwidths=13))

    headers_3=["Distancia Total","Total Nodos","Total Arcos","Puntos de Encuentro","Total Individuos","Individuos Distintos"]
    
    print(tabulate(x[2],headers_3,tablefmt='grid',stralign='center',maxheadercolwidths=13,maxcolwidths=13))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                data = load_data(control)
                
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
