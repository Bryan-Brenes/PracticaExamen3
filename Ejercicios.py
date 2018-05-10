# ----------------------------------------------------------------------------------------
# Ejercicio 1: posiciones
# ----------------------------------------------------------------------------------------
# auxiliar a nuevos_tiempos
def convertir_tiempos(lista, indice, resultado):
    if indice == len(lista):
        return resultado
    else:
        jugador = lista[indice]
        tiempo = jugador[1]
        seg = tiempo % 100
        min = ((tiempo // 100) % 100) * 60
        hor = (tiempo // 10000) * 3600
        seg_t = seg + min + hor
        nuevaInfo = [jugador[0], seg_t]
        resultado.append(nuevaInfo)

        return convertir_tiempos(lista, indice + 1, resultado)

# da una lista de las mismas dimensiones pero con todos los tiempo en segundos
def nuevos_tiempos(lista, indice, resultado):
    if indice == len(lista):
        return resultado
    else:
        resultado.append(convertir_tiempos(lista[indice], 0, []))
        return nuevos_tiempos(lista, indice + 1, resultado)

#--------------------------------------------------------------------------

# da una lista del mismo tamano solo con los jugadores por etapa
def filtrar_jugadores_en_todas_etapas(lista, indice, resultado):
    if indice == len(lista):
        return resultado
    else:
        listaJugadores = obtener_jugadores(lista[indice], 0, [])
        listaJugadores = set(listaJugadores)
        listaJugadores = list(listaJugadores)
        resultado.append(listaJugadores)
        return filtrar_jugadores_en_todas_etapas(lista, indice + 1, resultado)

def obtener_jugadores(lista, indice, resultado):
    if indice == len(lista):
        return resultado
    else:
        nombreJugador = lista[indice][0]
        resultado.append(nombreJugador)
        return obtener_jugadores(lista, indice + 1, resultado)

#--------------------------------------------------------------------------

# lista de una dimension los jugadores que estan en todas las etapas
# la entrada en la lista solo de jugadores
def listar_jugador_todas_etapas(lista, indice, resultado):
    if indice == len(lista):
        return resultado
    else:
        if indice == 0:
            resultado = lista[indice]
        else:
            resultado = list(set(resultado).intersection(set(lista[indice])))

        return listar_jugador_todas_etapas(lista, indice + 1, resultado)

#--------------------------------------------------------------------------

# elimnina los jugadores que no estan en todas las etapas
# devuelve una matriz
def eliminar_jugadores_no_todas_etapas(lista, indice, resultado, listaJugadores):
    if indice == len(lista):
        return resultado
    else:
        resultado.append(elimina_jugadores_aux(lista[indice], 0 , [], listaJugadores))
        return eliminar_jugadores_no_todas_etapas(lista, indice + 1, resultado, listaJugadores)

def elimina_jugadores_aux(lista, indice, resultado, listaJugadores):
    if indice == len(lista):
        return resultado
    else:
        if lista[indice][0] in listaJugadores:
            resultado.append(lista[indice])
        return elimina_jugadores_aux(lista, indice + 1, resultado, listaJugadores)

#--------------------------------------------------------------------------

# Da una lista con la suma de tiempos de cada uno de los jugadores que estan
# en todas la etapas

def suma_tiempos(lista, indice, resultado, listaJudores):
    if indice == len(listaJudores):
        return resultado
    else:
        suma = sumaJugador_aux(lista, 0, 0, listaJudores[indice], 0)
        resultado.append(tuple([listaJudores[indice], suma]))
        return suma_tiempos(lista, indice + 1, resultado, listaJudores)

def sumaJugador_aux(lista, indiceGlobal, indice, Jugador, resultado):
    if indiceGlobal == len(lista):
        return resultado
    else:
        if indice == len(lista[0]):
            indiceGlobal += 1
            indice = 0
        if indiceGlobal != len(lista):
            if lista[indiceGlobal][indice][0] == Jugador:
                resultado += lista[indiceGlobal][indice][1]
        return sumaJugador_aux(lista, indiceGlobal, indice + 1, Jugador, resultado)

# --------------------------------------------------------------------------

#
def obtener_ranking_por_etapa(lista, resultado):
    if lista == list():
        return resultado
    else:
        tupla = tuple(obtener_menor_tiempo_aux(lista, 0, []))
        resultado.append(tupla)
        lista.remove(tupla)
        return obtener_ranking_por_etapa(lista, resultado)

def obtener_menor_tiempo_aux(lista, indice, resultado):
    if indice == len(lista):
        return resultado
    else:
        if resultado == list():
            resultado = tuple(lista[indice])
        else:
            if lista[indice][1] < resultado[1]:
                resultado = tuple(lista[indice])
        return obtener_menor_tiempo_aux(lista, indice + 1, resultado)

#--------------------------------------------------------------------------

def devolver_tiempos(lista, indice, resultado):
    if indice == len(lista):
        return resultado
    else:
        tiempo = lista[indice][1]
        horas = tiempo // 3600
        if horas == 0:
            horas = ''
        min = (tiempo % 3600) // 60
        seg = (tiempo % 3600) % 60
        formatoTiempo = eval(str(horas) + '{0:02g}'.format(min) + '{0:02g}'.format(seg))
        resultado.append(tuple([lista[indice][0], formatoTiempo]))

        return devolver_tiempos(lista, indice + 1, resultado)


'''lista = [ [(100, 11512), (2, 15050), (130, 12320), (101, 12050), (125, 11501), (115, 20000) ],
[(130, 14050), (100, 15050), (125, 14515), (2, 23000), (101, 15000) ],
[(100, 4520), (101, 4720), (130, 4520), (125, 4600) ] ]'''

def posiciones(lista):
    listaJugadoresTodasEtapas = listar_jugador_todas_etapas(filtrar_jugadores_en_todas_etapas(lista, 0, []), 0, [], )
    jugadores_para_clasificar = eliminar_jugadores_no_todas_etapas(nuevos_tiempos(lista, 0, []), 0, [], listaJugadoresTodasEtapas)
    listaSumaTiempos = suma_tiempos(jugadores_para_clasificar, 0, [], listaJugadoresTodasEtapas)

    return obtener_ranking_por_etapa(devolver_tiempos(listaSumaTiempos, 0, []), [])

# ----------------------------------------------------------------------------------------
# Ejercicio 2:
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# Ejercicio 3: lista_principal
# ----------------------------------------------------------------------------------------

def lista_principal(lista):
    return lista_principal_aux(lista)

def lista_principal_aux(lista):
    if lista == list():
        return []
    else:
        if type(lista[0]) == int:
            return [lista[0]] + lista_principal_aux(lista[1:])
        else:
            return lista_principal_aux(lista[0]) + lista_principal_aux(lista[1:])

# print(lista_principal([ 10, 15, [ 5, 40], 8, [ [ 10, 75, 6], 8 ] ]))
# print(lista_principal([[ [ [ 2], [ 99, 4, 6 ] ], 8 ], 10, 75, 15, [ 100, [ 90, 80, [ 5, 8 ] ], 85]] ))

# ----------------------------------------------------------------------------------------
# Ejercicio 4: crea_listas ---------FALTA POR IMPLEMENTAR----------
# ----------------------------------------------------------------------------------------

def crea_listas(lista):
    if isinstance(lista, list):
        return crea_listas_aux(lista, True)
    else:
        return 'Error: la entrada debe ser una lista'

def crea_listas_aux(lista, asc):
    if lista == list():
        return []
    else:
        pass

# ----------------------------------------------------------------------------------------
# Ejercicio 5: pbp
# ----------------------------------------------------------------------------------------


def pbp(ini, fin):
    if isinstance(ini, int) and isinstance(fin, int):
        if ini > 1 and fin > 1:
            if fin >= ini:
                return pbp_aux(ini, fin)
            else:
                return 'Error: el fin debe ser mayor o igual al inicio'
        else:
            return 'Error: las entradas deben ser mayores a 1'
    else:
        return 'Error: las entradas deben ser enteros'


def pbp_aux(ini, fin):
    if ini > fin:
        return []
    else:
        es_primo = verificarPrimo(ini, 2)
        if es_primo:
            ini_base_2 = convertir_a_base_2(ini)
            if str(ini_base_2) == ''.join(list(reversed(list(str(ini_base_2))))):
                return [ini] + pbp_aux(ini + 1, fin)
            else:
                return pbp_aux(ini + 1, fin)
        else:
            return pbp_aux(ini + 1, fin)


def verificarPrimo(n, num):
    if num == n:
        return True
    else:
        if n % num == 0:
            return False
        else:
            return verificarPrimo(n, num + 1)


def convertir_a_base_2(n):
    listaResiduos = convertir_a_base_2_aux(n)
    return eval(''.join(reversed(listaResiduos)))


def convertir_a_base_2_aux(n):
    if n == 0:
        return []
    else:
        return [str(n%2)] + convertir_a_base_2_aux(n//2)


# ----------------------------------------------------------------------------------------
# Ejercicio 6: extrae_diagonal
# ----------------------------------------------------------------------------------------


def extrae_diagonal(lista, diagonal):
    if len(lista[0]) == len(lista):
        if abs(diagonal) <= len(lista) - 1:
            if diagonal >= 0:
                return extrae_diagonal_aux(lista, 0, diagonal)
            elif diagonal < 0:
                return extrae_diagonal_aux(lista, abs(diagonal), 0)
        else:
            return 'Error: la diagonal no existe'
    else:
        return 'Error: la matriz debe ser cuadrada'

def extrae_diagonal_aux(lista, indiceFila, indiceColumna):
    if indiceFila == len(lista):
        return []
    if indiceColumna == len(lista[0]):
        return []
    else:
        if indiceFila != len(lista):
            return [lista[indiceFila][indiceColumna]] + extrae_diagonal_aux(lista, indiceFila + 1, indiceColumna + 1)

print(extrae_diagonal([[20, 50, 60, 70, 80], [15, 20, 16, 40, 50], [30, 56, 60, 25, 30], [41, 85, 90, 64,
70], [68, 43, 12, 24, 16]], 0))

# <>