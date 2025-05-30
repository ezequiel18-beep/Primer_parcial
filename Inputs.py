import os
from Funciones import *



array_participantes = crear_array(5,"")
matriz_votos = crear_matriz(5,3,0)

bandera_carga_nombres = False
bandera_carga_puntuacion = False

while True:
    print("1.Cargar participantes\n2.Cargar puntuaciones\n3.Mostrar puntuaciones\n4.Participantes con promedio menor a 4 \n5.Participantes con promedio menor a 8 \n6.Promedio de cada jurado" \
    "\n7.jurado mas estricto\n8.Jurado mas generoso\n9.Participantes con puntuaciones iguales\n10.Buscar participante por nombre\n11.Top 3 mejores promedios\n12.Participantes ordenados alfabeticamente")

    opcion = input("Su opcion: ")
    while  es_entero(opcion) == False or validar_maximo_minimo(opcion, 12 ,1, "Error tiene que ser un numero entre 1 y 12") ==  False:
        opcion = input("Reingrese su opcion (1-12): ")
    opcion = int(opcion)
    if opcion == 1:
            cargar_nombres_partipantes(array_participantes)
            print("Nombres cargados correctamente...")
            mostrar_array(array_participantes)
            bandera_carga_nombres = True
        
    elif opcion == 2 and bandera_carga_nombres == True:
        if cargar_puntuacion(matriz_votos) == True:
            print("Carga exitosa de votos!")
            bandera_carga_puntuacion = True
        else:
            print("Error al realizar la carga")
    elif opcion == 3 and (bandera_carga_puntuacion == True and bandera_carga_nombres == True):
        if mostrar_puntuacion_participantes(array_participantes,matriz_votos) == False:
            print("No se pueden mostrar las puntuaciones")
    elif opcion == 4 and (bandera_carga_puntuacion == True and bandera_carga_nombres == True):
        if calcular_menor_cuatro(matriz_votos,array_participantes) == False:
            print(f"No hay ningun participante con menos del 44% de promedio")
    elif opcion == 5 and (bandera_carga_puntuacion == True and bandera_carga_nombres == True):
        if calcular_menor_ocho(matriz_votos,array_participantes) == False:
            print(f"No hay ningun participante con menos del 8% de promedio")
    elif opcion == 6 and (bandera_carga_puntuacion == True and bandera_carga_nombres == True):
        promediar_jurados(matriz_votos)
    elif opcion == 7 and (bandera_carga_puntuacion == True and bandera_carga_nombres == True):
        calcular_jurado_estricto(matriz_votos)
    elif opcion == 8 and (bandera_carga_puntuacion == True and bandera_carga_nombres == True):
        calcular_jurado_generoso(matriz_votos)
    elif opcion == 9 and (bandera_carga_puntuacion == True and bandera_carga_nombres == True):
        if mostrar_participantes_iguales(matriz_votos,array_participantes) == False:
            print("Error, no se encontro ningun participante con puntuaciones iguales.")
    elif opcion == 10 and (bandera_carga_puntuacion == True and bandera_carga_nombres == True):
        if buscar_participante(matriz_votos, array_participantes) == False:
            print("Error el participante no existe")
    elif opcion == 11 and (bandera_carga_puntuacion == True and bandera_carga_nombres == True):
        mostrar_top_tres(matriz_votos,array_participantes)
    elif opcion == 12 and (bandera_carga_puntuacion == True and bandera_carga_nombres == True):
        mostrar_participante_ordenados(array_participantes,matriz_votos)
    else:
        print("Acceso invalido!")
    input("Toque cualquier boton para continuar...")
    os.system("cls")