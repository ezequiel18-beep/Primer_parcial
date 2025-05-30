def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        #matriz.append(fila)
        matriz += [fila]
        
    return matriz

def crear_array(cantidad_elementos:int,valor_inicial:any) -> list:
    array = [valor_inicial] * cantidad_elementos
    return array

def validar_participante(nombre: str) -> bool:
    """Valida cada nombre del participante, que tenga almenos 3
    caracteres y solo que contenga letras y espacios

    Args:
        nombre (str): Nombre del participante

    Returns:
        bool: Devuelve verdadero o falso
    """
    resultado = True
    if len(nombre) >= 3:
        for j in range(len(nombre)):
            valor_ascii = ord(nombre[j])
            if (valor_ascii < 65 or valor_ascii > 90) and (valor_ascii < 97 or valor_ascii > 122) and valor_ascii != 32:
                resultado = False
    else:
        resultado = False  
    return resultado

def cargar_nombres_partipantes(array_nombres:list) -> bool:
    """Se cargan los nombres de los participantes

    Args:
        array_nombres (list): Se pasa como argumento el array de nombres

    Returns:
        bool:Devuelve verdadero o falso
    """
    if type(array_nombres) == list and len(array_nombres) > 0:
        retorno = True
        for i in range(len(array_nombres)):
            nombre = input(f"Ingrese el nombre del participante {i + 1}: ")
            while validar_participante(nombre) == False:
                print("Nombre invalido")
                nombre = input(f"Reingrese el nombre del participante {i + 1}: ")
            array_nombres[i] = nombre

    else:
        retorno = False
        
    return retorno

def sumar_fila(matriz_numerica:list,indice_fila:int) -> int | float:
    """Suma cada fila de la matriz de votos
    Args:
        matriz_numerica (list): Se ingresa matriz de votos
        indice_fila (int): Se ingresa el indice de la fila

    Returns:
        int | float: Retorna la suma de la fila
    """
    suma_fila = 0
    
    for col in range(len(matriz_numerica[indice_fila])):
        if type(matriz_numerica[indice_fila][col]) == int or type(matriz_numerica[indice_fila][col]) == float :
            suma_fila += matriz_numerica[indice_fila][col]
    
    return suma_fila

def calcular_promedio(total_linea: int|float, cantidad_votos : int) -> float | None:
    """Calcula el promedio de la linea

    Args:
        total_linea (int | float): Se ingrea la suma total de la linea
        cantidad_votos (int): Se ingresa la cantidad de votos que hubo en esa linea

    Returns:
        float | None: Retorna el promedio de los votos
    """
    if total_linea != 0:
        promedio = total_linea / cantidad_votos
    else:
        promedio = 0
        
    return promedio

def mostrar_array(array:list) -> None:
    """Se encarga de mostar la lista

    Args:
        array (list):Le pasamos la lista
    """
    for i in range(len(array)):
        print(f"Participante N {i +1} : {array[i]}")

def es_entero(cadena: str) -> bool:
    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if (valor_ascii < 48 or valor_ascii > 57) and valor_ascii != 45 :
                print("Error no es un numero")
                retorno = False
                break
    else: 
        retorno = False
    return retorno

def validar_maximo_minimo(voto: str,maximo: int , minimo: int, mensaje: int) -> bool:
    voto = int(voto)
    if voto > maximo or voto < minimo:
        resultado = False
        print(mensaje)
    else:
        resultado = True
    
    return resultado

def cargar_puntuacion(matriz_votos:list) -> bool:
    """Verifica y carga los datos en la matriz

    Args:
        matriz_votos (list): Le pasamos la matriz de votos con valor 0

    Returns:
        bool: Retornamos verdadero o falso
    """
    if type(matriz_votos) == list and len(matriz_votos) > 0:
        retorno = True
    
        for fil in range(len(matriz_votos)):
            for col in range(len(matriz_votos[fil])):
                voto = input(f"Ingrese puntuacion del jurado N {col + 1} para el participante N {fil + 1}: ")
                while es_entero(voto) == False or validar_maximo_minimo(voto, 10 ,1, "Error tiene que ser un numero entre 1 y 10") == False:
                    voto = input(f"Reingrese puntuacion del jurado N {col + 1} para el participante N {fil + 1}: ")    
                voto = int(voto)
                matriz_votos[fil][col] += voto

    else:
        retorno = False
                

        
    return retorno

def mostrar_por_participante(array_nombre: list, matriz_votos: list, indice)-> bool:
    """Muestra todos los puntaje de un partipante

    Args:
        array_nombre (list): la lista de los nombres
        matriz_votos (list): La lista de los puntajes
        indice (_type_): El numero de participante

    Returns:
        bool: _description_
    """
    print(f"NOMBRE PARTICIPANTE: {array_nombre[indice]}")
    total_puntaje = sumar_fila(matriz_votos,indice)
    promedio = calcular_promedio(total_puntaje,len(matriz_votos[indice]))
    for col in range(len(matriz_votos[indice])):
        print(f"PUNTAJE JURADO {col+1}: {matriz_votos[indice][col]}")
    print(f"PUNTAJE PROMEDIO: {round(promedio,2)}/10")
    
def mostrar_puntuacion_participantes(array_nombres: list, matriz_votos: list) -> bool:
    """Muestra la puntuacion de todos los participantes

    Args:
        array_nombres (list): Recibe la lista de nombres
        matriz_votos (list): Recibe la lista de votos

    Returns:
        bool: Retorna un bool
    """
    if type(matriz_votos) == list and type(array_nombres) == list and len(matriz_votos) > 0 and len(array_nombres) > 0 :
       
        for fil in range(len(matriz_votos)):
            retorno = True  
            mostrar_por_participante(array_nombres,matriz_votos,fil)

    else:
        retorno = False
        
    return retorno

def mostrar_promedio_participante(array_nombres: list, matriz_votos: list) -> bool:
    for fil in range(len(matriz_votos)):
        total_puntaje = sumar_fila(matriz_votos,fil)
        promedio = calcular_promedio(total_puntaje,len(matriz_votos[fil]))
        print(f"PUNTAJE PARTICIPANTE {array_nombres[fil]} PROMEDIO: {round(promedio,2)}/10")
        
def calcular_menor_cuatro(matriz_votos:list,array_nombres: list) -> float | bool:
    """Calcula el promedio menor a 4 de todos los participantes

    Args:
        matriz_votos (list): Se ingresa la matriz de votos
        array_nombres (list): Se ingresa la lista de nombres

    Returns:
        float: Retorna un print si es verdadero , si no solo false.
    """
    resultado = False
    for fil in range(len(matriz_votos)):
        total_puntaje = sumar_fila(matriz_votos,fil)
        promedio = calcular_promedio(total_puntaje,len(matriz_votos))
        if promedio < 4:
            resultado = True
            print(f"Participante {array_nombres[fil]} tiene un promedio de: {round(promedio,2)}")
       
        
        
    return resultado

def calcular_menor_ocho(matriz_votos:list,array_nombres: list) -> float | bool:
    """Calcula el promedio menor a 8 de todos los participantes

    Args:
        matriz_votos (list): Se ingresa la matriz de votos
        array_nombres (list): Se ingresa la lista de nombres

    Returns:
        float: Retorna un print si es verdadero , si no solo false.
    """
    for fil in range(len(matriz_votos)):
        total_puntaje = sumar_fila(matriz_votos,fil)
        promedio = calcular_promedio(total_puntaje,len(matriz_votos))
        if promedio < 8:
            resultado = True
            print(f"Participante {array_nombres[fil]} tiene un promedio de: {round(promedio,2)}")
        else:
            resultado = False
        
        
    return resultado

def sumar_columna(matriz_votos: list,indice_col:int) -> int | float:
    acumulador = 0
    
    for fil in range(len(matriz_votos)):
        acumulador += matriz_votos[fil][indice_col]
    
    return acumulador

def promediar_jurados(matriz_votos: list) -> None:
    """Muestra los promedios de cada jurado

    Args:
        matriz_votos (list): Recibe la lista de votos

    Returns:
        str: Hace un print de los promedios
    """
    for col in range(len(matriz_votos[0])):
        suma_columna = sumar_columna(matriz_votos,col)
        promedio = calcular_promedio(suma_columna,len(matriz_votos))
        print(f"El promedio del jurado {col+1} es de: {round(promedio,2)}")

def encontrar_jurado(lista_promedios: list, opcion: str) -> int:
    """Encuentra al jurado mas estricto o generoso

    Args:
        lista_promedios (list): Recibe la lista de promedios
        opcion (str): Recibe si quiere buscar al mas estricto o al mas generoso

    Returns:
        int: Devuelve la posicion del jurado
    """
    bandera = True
    jurado_dos = 0
    bandera_iguales = False
    if opcion == "Generoso" :
        for i in range(len(lista_promedios)):
            if bandera == True:
                valor_maximo = lista_promedios[i]
                jurado = i+1
                bandera = False
            elif lista_promedios[i] > valor_maximo:
                valor_maximo = lista_promedios[i]
                jurado = i+1
            elif lista_promedios[i] == valor_maximo:
                jurado_dos = i+1
                bandera_iguales = True
        if bandera_iguales == True:
            print(f"El jurado {jurado} y {jurado_dos} son los dos mas generosos")
        else:
            print(f"El jurado {jurado} fue el mas generoso")
                
    else:
        for i in range(len(lista_promedios)):
            if bandera == True:
                valor_minimo = lista_promedios[i]
                jurado = i+1
                bandera = False
            elif lista_promedios[i] < valor_minimo:
                valor_minimo = lista_promedios[i]
                jurado = i+1
            elif lista_promedios[i] == valor_minimo:
                jurado_dos = i+1
                bandera_iguales = True
        if bandera_iguales == True:
            print(f"El jurado {jurado} y {jurado_dos} son los dos mas estrictos")
        else:
            print(f"El jurado {jurado} fue el mas estricto")
                 

def calcular_jurado_estricto(matriz_votos: list) -> str:
    """Calcula el jurado mas estricto

    Args:
        matriz_votos (list): Recibe la lista de votos

    Returns:
        str: Hace un print del jurado mas estricto
    """
    promedios = []

    for col in range(len(matriz_votos[0])):
        suma_col = sumar_columna(matriz_votos,col)
        promedio = calcular_promedio(suma_col,len(matriz_votos))
        promedios += [promedio]
    encontrar_jurado(promedios,"Estricto")                              
    


    
def calcular_jurado_generoso(matriz_votos: list) -> str:
    """Calcula el jurado mas generoso

    Args:
        matriz_votos (list): Recibe la lista de votos

    Returns:
        str: Hace un print del jurado mas generoso
    """
    promedios = []

    for col in range(len(matriz_votos[0])):
        suma_col = sumar_columna(matriz_votos,col)
        promedio = calcular_promedio(suma_col,len(matriz_votos))
        promedios += [promedio]
    encontrar_jurado(promedios,"Generoso")
    
calcular_jurado_generoso([[1,3,3],[0,3,3],[1,3,3]])
def encontrar_iguales(total: list, array_nombre: int) -> bool:
    """Encuentra los participantes con la misma suma de votos

    Args:
        total (list): Recibe la lista total de votos de cada participantes
        array_nombre (int): Lista de nombres

    Returns:
        bool: Retorna true si encontro si no false
    """
    retorno = False
    for i in range(len(total)):
        for j in range(i+1,len(total)):
            if total[i] == total[j]:
                print(f"Se encontro que los participantes {array_nombre[i]} y {array_nombre[j]} tienen el mismo total de puntuacion {total[i]} ")
                retorno = True
                
    return retorno

def mostrar_participantes_iguales(matriz_votos: list, array_nombre: list)-> bool:
    """Busca los participantes con la misma suma de votos

    Args:
        matriz_votos (list): Lista de votos
        array_nombre (list): Lista de array

    Returns:
        bool: Devuelve true si encontro si no false
    """
    
    totales = []
    
    for fil in range(len(matriz_votos)):
        suma = sumar_fila(matriz_votos,fil)
        totales += [suma]
    if encontrar_iguales(totales,array_nombre) == True:
        retorno = True
    else:
        retorno = False
    return retorno

def buscar_participante(matriz_votos: list, array_nombre: list) -> bool:
    """Busca el nombre del participante y lo valida

    Args:
        matriz_votos (list): Lista de votos
        array_nombre (list): lista de participantes

    Returns:
        bool: devuelve true si lo encontro si no false
    """
    nombre = input("ingrese el nombre del participante: ")
    retorno = False
    while validar_participante(nombre) == False:
        print("Error")
        nombre = input("Reingrese el nombre del participante: ")
    for i in range(len(array_nombre)):
        if nombre == array_nombre[i]:
            retorno = True
            mostrar_por_participante(array_nombre ,matriz_votos, i)
            
    return retorno

def mostrar_top_tres(matriz_votos: list, array_nombre: list) -> None:
    """Muestra el top 3 mejores promedios de los participantes

    Args:
        matriz_votos (list): Recibe la lista de nombres
        array_nombre (list): Recibe los votos del participante

        Hace un print con la informacion
    """
    lista_promedios = []
    
    for fil in range(len(matriz_votos)):
        total_puntaje = sumar_fila(matriz_votos,fil)
        promedio = calcular_promedio(total_puntaje,len(matriz_votos[fil]))
        lista_promedios += [round(promedio,2)]

    
    for i in range(len(lista_promedios)-1):
            for j in range(i + 1,len(lista_promedios)):
                
                if lista_promedios[i] < lista_promedios[j]:
                    aux = lista_promedios[i]
                    lista_promedios [i] = lista_promedios[j]
                    lista_promedios[j] = aux
                    aux_nombre = array_nombre[i]
                    array_nombre[i] = array_nombre[j]
                    array_nombre[j] =aux_nombre
    print("TOP 3 DE MEJORES PROMEDIOS")
    for y in range(3):
        print(f"Participante {array_nombre[y]} con un promedio de {lista_promedios[y]}  ")
        
def mostrar_participante_ordenados(array_nombres:list, matriz_votos: list) -> None:
    """Muestra los participantes ordenados alfabeticamente con sus respectivas notas

    Args:
        array_nombres (list): Recibe la lista de nombres
        matriz_votos (list): Recibe los votos del participante

        Hace un print con la informacion
    """
    for i in range(len(array_nombres)-1):
            for j in range(i + 1,len(array_nombres)):
                
                if array_nombres[i] > array_nombres[j]:
                    aux = array_nombres[i]
                    array_nombres [i] = array_nombres[j]
                    array_nombres[j] = aux
                    aux_voto = matriz_votos[i]
                    matriz_votos[i] = matriz_votos[j]
                    matriz_votos[j] = aux_voto
    mostrar_puntuacion_participantes(array_nombres, matriz_votos) 


