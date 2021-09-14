from clases import Automovil
import re
import os
import csv
from typing import List
from operator import attrgetter
from datetime import datetime

LimpiarPantalla = lambda: os.system('cls')

lista_automoviles = []
RegexDatos = "^[A-Za-z0-9_-]*$"
RegexLetras = "^[a-zA-Z ]+$"
cargar = True

def Indice(buscar):
    contador=-1
    indice_retorno=-1
    for e in lista_automoviles:
        contador+=1
        if (e.matricula == buscar):
            indice_retorno = contador
            break
    return indice_retorno

def RegEx(_txt,_regex):
    coincidencia = re.match(_regex, _txt)
    return bool(coincidencia)

def BuscarMatricula(matricula):
    coincidencia=False
    for e in lista_automoviles:
        if (e.matricula == matricula):
            coincidencia = True
            break
    return coincidencia


def cargarInfoCSV():
    global cargar
    # Abrimos CSV y cargamos datos, usando separador |
    # Se cargan en una lista de objetos
    if cargar == True:
        try:
            with open('automoviles.csv', newline='') as archivo_csv:
                lector_csv = csv.reader(archivo_csv, delimiter='|')
                for e in lector_csv:
                    lista_automoviles.append(Automovil(e[0],e[1],e[2],e[3],e[4],e[5]))
            print("Informacion cargada con exito!")
        except:
            print("No hay informacion que cargar!.")
    else:
        print("La informacion ya fue cargada!")
    cargar = False

def registrarAutomovil():
    print("---Registrar Automovil---")
    while True:
        matricula = input("Ingrese la matrícula del automóvil que desea registrar: ")
        if matricula == "":
                break
        if BuscarMatricula(matricula):
            print("Ese automóvil ya está registrado.")
            break
        else:
            marca = input("Ingrese la marca: ")
            if re.match(RegexLetras,marca):
                modelo = input("Ingrese el nombre del modelo: ")
                if re.match(RegexLetras, modelo):
                    try:
                        año = int(input("Ingrese el año: "))
                    except:
                        print("Error: Ingresa un dato valido")
                        break
                    if año >= 1900 and año <= 2022:
                        estado = input("Ingrese el estado del auto: ")
                        if re.match(RegexLetras, estado):
                            nuevo_automovil = Automovil(matricula, marca, modelo, año, estado)
                            lista_automoviles.append(nuevo_automovil)
                            print("Automovil registrado con exito!")
                            break
                        else:
                            print("Ingrese un dato sin valores numéricos. ")
                            input("Pulsa enter para continuar...")
                            LimpiarPantalla()
                    else:
                        print("Error: Ingrese un año válido. ")
                        input("Pulsa enter para continuar...")
                        LimpiarPantalla()
                else:
                    print("Error: Ingrese un dato con solamente letras. ")
                    input("Pulsa enter para continuar...")
                    LimpiarPantalla()
            else:
                print("Error: Ingrese un dato valido")
                input("Pulsa enter para continuar...")
                LimpiarPantalla()

def buscarAutomovil():
    print("---Buscar Automóvil---")
    while True:
        matricula = input("Ingrese la matrícula del automóvil que desea buscar: ")
        if matricula == "":
                break
        if re.match(RegexDatos,matricula):
            if BuscarMatricula(matricula):
                indice = Indice(matricula)
                print("\n---Datos del automóvil---")
                print("\nMatricula: ",lista_automoviles[indice].matricula)
                print("Marca: ",lista_automoviles[indice].marca)
                print("Modelo: ",lista_automoviles[indice].modelo)
                print("Año: ",lista_automoviles[indice].año)
                print("Estado: ",lista_automoviles[indice].estado)
                break
            else:
                print("Ese automóvil no está registrado en la lista")
                break
        else:
            print("Error: Ingrese una matrícula valida")
            input("Pulsa enter para continuar...")
            LimpiarPantalla()

def modificarAutomovil():
    print("---Modificar Automóvil---")
    while True:
        matricula = input("Ingrese la matrícula del auto que desea modificar: ")
        if matricula == "":
                break
        if re.match(RegexDatos,matricula):
            if BuscarMatricula(matricula):
                indice = Indice(matricula)
                print("\n---Datos del automóvil---")
                print("\nMatricula: ",lista_automoviles[indice].matricula)
                print("Marca: ",lista_automoviles[indice].marca)
                print("Modelo: ",lista_automoviles[indice].modelo)
                print("Año: ",lista_automoviles[indice].año)
                print("Estado: ",lista_automoviles[indice].estado)
                while True:
                    marca = input("\nIngrese la marca del automóvil: ")
                    if re.match(RegexLetras,marca):
                        modelo = input("\nIngrese el modelo del automóvil: ")
                        if re.match(RegexLetras, modelo):
                            try:
                                año = int(input("\nIngrese el año del automóvil: "))
                            except:
                                print("Error: Ingresa un dato valido")
                                break
                            if año >= 1900 and año <= 2022:
                                estado = input("\nIngrese el estado del automóvil: ")
                                lista_automoviles[indice].marca = marca
                                lista_automoviles[indice].modelo = modelo
                                lista_automoviles[indice].año = año
                                lista_automoviles[indice].estado = estado
                                print("Informacion actualizada con exito!")
                                break
                            else:
                                print("Error: Ingrese una fecha válida. ")
                                input("Pulsa enter para continuar...")
                                LimpiarPantalla()
                        else:
                            print("Error: Ingrese un dato sin valores numéricos. ")
                            input("Pulsa enter para continuar...")
                            LimpiarPantalla()
                    else:
                        print("Error: Ingrese un dato sin valores numéricos. ")
                        input("Pulsa enter para continuar...")
                        LimpiarPantalla()
                break
            else:
                print("Ese automóvil no está registrado en la lista")
                break
        else:
            print("Error: Ingrese una matrícula válida")
            input("Pulsa enter para continuar...")
            LimpiarPantalla()

def eliminarAutomovil():
    print("---Eliminar Automóvil---")
    while True:
        matricula = input("Ingrese la matrícula del auto que desea eliminar: ")
        if matricula == "":
                break
        if re.match(RegexDatos,matricula):
            if BuscarMatricula(matricula):
                indice = Indice(matricula)
                print("Matricula: ",lista_automoviles[indice].matricula)
                print("Marca: ",lista_automoviles[indice].marca)
                print("Modelo: ",lista_automoviles[indice].modelo)
                print("Año: ",lista_automoviles[indice].año)
                print("Estado: ",lista_automoviles[indice].estado)
                respuesta = input("¿Desea eliminar el automovil? [S/N]")
                if respuesta.upper() == "S":
                    lista_automoviles.pop(indice)
                    print("Eliminacion exitosa!")
                else:
                    print("No se elimino ningun elemento")
                break
            else:
                print("Ese automóvil no está registrado en la lista")
                break
        else:
            print("Error: Ingrese una matrícula valida")
            input("Pulsa enter para continuar...")
            LimpiarPantalla()

def verListaAutomoviles():
    for elemento in lista_automoviles:
        print("{:>10} {:>10} {:>10} {:>10} {:>10} {:>10}".format(
        elemento.matricula, elemento.marca, elemento.modelo, elemento.año, elemento.estado, elemento.momento))

def actualizarCSV():
    ruta = os.path.abspath(os.getcwd())
    archivo_trabajo = ruta + "\\automoviles.csv"
    archivo_respaldo = ruta + "\\automoviles.bak"

    # Determinar si el archivo de trabajo ya existe.
    if os.path.exists(archivo_trabajo):
        # Si el archivo existe, entonces verifico si hay respaldo y lo borro.
        if os.path.exists(archivo_respaldo):
            os.remove(archivo_respaldo)

        # Establezco el achivo de datos, como respaldo
        os.rename(archivo_trabajo,archivo_respaldo)

        # Genera el archivo CSV
        f = open(archivo_trabajo,"w+")
        
    else:
        # Genera el archivo CSV
        f = open(archivo_trabajo,"w+")

        # Escribo los encabezados de mi CSV
        f.write("MATRICULA|MARCA|MODELO|AÑO|ESTADO|MOMENTO\n")

    # Escribimos en el CSV, a partir de la lista de objetos.
    for elemento in lista_automoviles:
        f.write(f'{elemento.matricula}|{elemento.marca}|{elemento.modelo}|{elemento.año}|{elemento.estado}|{elemento.momento}\n')

    # Cierro el archivo
    f.close()
    print("Archivo CSV actualizado correctamente!")

def menu_consola():
    while (True):
        LimpiarPantalla()
        print("[1] Cargar información guardada.")
        print("[2] Agregar Automóvil.")
        print("[3] Buscar Automóvil.")
        print("[4] Modificar datos de Automóvil.")
        print("[5] Eliminar Automóvil.")
        print("[6] Ver lista de automóviles.")
        print("[7] Guardar información.")
        print("[X] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[12345678Xx]{1}$"):
            if opcion_elegida.upper() == "X":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                cargarInfoCSV()
            if opcion_elegida=="2":
                registrarAutomovil()
            if opcion_elegida=="3":
                buscarAutomovil()
            if opcion_elegida=="4":
                modificarAutomovil()
            if opcion_elegida=="5":
                eliminarAutomovil()
            if opcion_elegida=="6":
                verListaAutomoviles()
            if opcion_elegida=="7":
                actualizarCSV()

            input("Pulsa enter para contunuar...")
        else:
            print("RESPUESTA NO VÁLIDA.")
            input("Pulsa enter para contunuar...")
def main():
    menu_consola()

main()