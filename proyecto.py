import os
import sys
import random

sys.stdout.reconfigure(encoding="utf-8")

from prettytable import PrettyTable


# Lectura de archivo (equipos)
def OpenFile(ini, fin):
    datos = []
    rutas = [
        "C:/Users/Diego Hernandez/OneDrive/Documentos/archivo_proyecto_final.txt",
        "../archivo_proyecto_final.txt",
        "archivo_proyecto_final.txt",
        "Tablas_estadisticas.txt"
    ]
    archivo = None
    for r in rutas:
        try:
            archivo = open(r, encoding="utf-8")
            break
        except FileNotFoundError:
            continue
    
    if not archivo:
        print("Error: No se pudo encontrar el archivo de datos.")
        sys.exit(1)
        
    with archivo:
        lineas = archivo.readlines()
        indice = 0
        while indice < len(lineas):
            if lineas[indice][0 : len(ini)] == ini:
                o = indice
                while True:
                    o += 1
                    if lineas[o][0 : len(ini)] == fin:
                        break

                    datos.append(lineas[o])

            indice += 1

        return datos


def calcular_ave(JG, JJ):
    if int(JG) >= 0 or int(JJ) >= 0:
        return round(float(JG) / float(JJ), 3)

    return 0


def calcular_dif(JJ, JG, JJ_lider, JG_lider):
    if int(JJ) > 0 or int(JG) >= 0:
        return round(int(JG_lider - JG) - ((JJ_lider - JJ) / 2), 1)
    return 0


# almacen de datos de los equipos
lista_equipos = OpenFile("@@@@@", "@@@@-")
equipos = []

for datos_equipo in lista_equipos:
    partes = datos_equipo.split()
    equipo = {
        "id": int(partes[0]),
        "equipo": " ".join(partes[1:-3]),
        "JJ": int(partes[-3]),
        "JG": int(partes[-2]),
        "JP": int(partes[-1]),
        "AVE": calcular_ave(int(partes[-2]), int(partes[-3])),
        "DIF": 0,
    }
    equipos.append(equipo)

# ordenar los equipos por mayor average a menor y calculos de la diferencia
for equipo in equipos:
    equipo_lider = max(equipos, key=lambda x: x["AVE"])
    equipo["DIF"] = calcular_dif(
        equipo["JJ"], equipo["JG"], equipo_lider["JJ"], equipo_lider["JG"]
    )


def obtener_equipos_por_average():
    return sorted(equipos, key=lambda eq: eq["AVE"], reverse=True)


def obtener_nombre_equipo_por_id(id):
    for equipo in equipos:
        if equipo["id"] == id:
            return equipo["equipo"]

    return ""


# almacen de datos de los pitchers


# calculo efectividad
def calculo_efectividad(cl, il):
    if float(il) > 0:
        resultado = (float(cl) * 9) / float(il)
        return round(resultado, 2)

    return 0


# calculo del whip
def calculo_whip(bb, h, il):
    if float(il) > 0:
        resultado = (float(bb) + float(h)) / float(il)
        return round(resultado, 2)

    return 0


# calculo de ponche por base por bola
def calculo_ponches_basexbola(p, bb):
    if int(bb) > 0:
        resultado = int(p) / int(bb)

        return round(resultado, 2)
    return 0


lista_pitcher = OpenFile("*****", "****-")
pitchers = []

for datos_pitcher in lista_pitcher:
    partes_pitcher = datos_pitcher.split()
    pitcher = {
        "id_equipo": int(partes_pitcher[0]),
        "#": int(partes_pitcher[1]),
        "Nom": partes_pitcher[2],
        "Ape": " ".join(partes_pitcher[3:-6]),
        "Pos": partes_pitcher[-6],
        "P": int(partes_pitcher[-5]),
        "BB": int(partes_pitcher[-4]),
        "H": int(partes_pitcher[-3]),
        "IL": float(partes_pitcher[-2]),
        "CL": int(partes_pitcher[-1]),
        "EFE": calculo_efectividad(
            float(partes_pitcher[-1]), float(partes_pitcher[-2])
        ),
        "WHIP": calculo_whip(
            float(partes_pitcher[-4]),
            float(partes_pitcher[-3]),
            float(partes_pitcher[-2]),
        ),
        "P/BB": calculo_ponches_basexbola(
            int(partes_pitcher[-5]), int(partes_pitcher[-4])
        ),
    }
    pitchers.append(pitcher)

# almacen de dato de los bateadores


def calculo_promedio_bate(h, tb):
    if int(h) >= 0 and int(tb) > 0:
        resultado = float(h) / float(tb)
        return round(resultado, 3)

    return 0


def calculo_porcentaje_alcanzar_bases(h, bb, hbp, tb, sf):
    numerador = float(h) + float(bb) + float(hbp)
    denominador = float(tb) + float(bb) + float(hbp) + float(sf)
    if numerador >= 0 and denominador > 0:
        resultado = numerador / denominador
        return round(resultado, 3)
    return 0


def calcular_slugging(h, dosb, tresb, hr, tb, bb, hbp, sf):
    numerador = float(1 * h) + float(2 * dosb) + float(3 * tresb) + float(4 * hr)
    denominador = float(tb) + float(bb) + float(hbp) + float(sf)

    if numerador >= 0 and denominador > 0:
        resultado = numerador / denominador
        return round(resultado, 3)
    return 0


lista_bateador = OpenFile("&&&&&", "&&&&-")
bateadores = []

for datos_bateador in lista_bateador:
    partes_bateador = datos_bateador.split()
    bateador = {
        "id_equipo_b": int(partes_bateador[0]),
        "#": int(partes_bateador[1]),
        "Nom": partes_bateador[2],
        "Ape": " ".join(partes_bateador[3:-10]),
        "Pos": partes_bateador[-10],
        "H": int(partes_bateador[-9]),
        "BB": int(partes_bateador[-8]),
        "HBP": int(partes_bateador[-7]),
        "SF": int(partes_bateador[-6]),
        "TB": int(partes_bateador[-5]),
        "2B": int(partes_bateador[-4]),
        "3B": int(partes_bateador[-3]),
        "HR": int(partes_bateador[-2]),
        "CI": int(partes_bateador[-1]),
        "PRO": calculo_promedio_bate(
            int(partes_bateador[-9]), int(partes_bateador[-5])
        ),
        "OBP": calculo_porcentaje_alcanzar_bases(
            int(partes_bateador[-9]),
            int(partes_bateador[-8]),
            int(partes_bateador[-7]),
            int(partes_bateador[-5]),
            int(partes_bateador[-6]),
        ),
        "SLG": calcular_slugging(
            int(partes_bateador[-9]),
            int(partes_bateador[-4]),
            int(partes_bateador[-3]),
            int(partes_bateador[-2]),
            int(partes_bateador[-5]),
            int(partes_bateador[-8]),
            int(partes_bateador[-7]),
            int(partes_bateador[-6]),
        ),
    }
    bateadores.append(bateador)

# almacen datos defensas


# calculo promedio de fildeo (F%)
def calculo_promedio_fildeo(O, A, E):
    lances = calculo_lances(O, A, E)
    if lances > 0:
        return round(float(O + A) / float(lances), 3)
    return 0


# calculo de_total_lances
def calculo_lances(O, A, E):
    if float(O) >= 0 and float(A) >= 0 and float(E) >= 0:
        return float(O) + float(A) + float(E)

    return 0


# calculo de ponche por base por bola
def calculo_doble_play_sobre_juego(DP, JJ):
    if float(JJ) >= 0 and float(DP) >= 0:
        return round(float(DP) / float(JJ), 3)

    return 0


lista_defensores = OpenFile("!!!!!", "!!!!-")
defensores = []

for datos_defensas in lista_defensores:
    partes_defensa = datos_defensas.split()
    defensa = {
        "id_d": int(partes_defensa[0]),
        "#_d": int(partes_defensa[1]),
        "Nom_d": (partes_defensa[2]),
        "Ape_d": " ".join(partes_defensa[3:-6]),
        "Pos_d": (partes_defensa[-6]),
        "JJ_d": int(partes_defensa[-5]),
        "O_d": int(partes_defensa[-4]),
        "A_d": int(partes_defensa[-3]),
        "E_d": int(partes_defensa[-2]),
        "DP_d": int(partes_defensa[-1]),
        "F%": calculo_promedio_fildeo(
            int(partes_defensa[-4]), int(partes_defensa[-3]), int(partes_defensa[-2])
        ),
        "TL": calculo_lances(
            int(partes_defensa[-4]), int(partes_defensa[-3]), int(partes_defensa[-2])
        ),
        "DP/J": calculo_doble_play_sobre_juego(
            int(partes_defensa[-1]), int(partes_defensa[-5])
        ),
    }
    defensores.append(defensa)


# funcion de limpiar pantalla y que se vea mas estetico en la terminal
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def titulo():  # llamado del titulo
    clear()
    titulo = "UNIVERSIDAD CATÓLICA ANDRÉS BELLO".upper()
    titulo2 = "FACULTAD DE INGENIERÍA".upper()
    titulo3 = "ESCUELA DE INGENIERÍA INFORMÁTICA".upper()
    titulo4 = "FUNDAMENTOS DE LA PROGRAMACIÓN".upper()
    titulo5 = "ESTADÍSTICAS DEL BEISBOL".upper()
    titulo6 = "HECHO POR DIEGO HERNÁNDEZ Y ANDRÉS DE QUINTAL".upper()

    print(titulo.center(120, " "))
    print(titulo2.center(120, " "))
    print(titulo3.center(120, " "))
    print(titulo4.center(120, " "))
    print(titulo5.center(120, " "))
    print(titulo6.center(120, " "))


# llamado del menu, lo reflejado en pantalla para que el usuario interactue (a su vez para que las opciones se reflejen centradas)
def menu():
    opcion = 0
    while opcion > 6 or opcion < 1:
        titulo()
        print(" ")

        op1 = "1 Estadísticas de pitcheo".capitalize()
        op2 = "2 Estadísticas de bateo".capitalize()
        op3 = "3 Estadísticas defensivas".capitalize()
        op4 = "4 Estadísticas colectivas".capitalize()
        op5 = "5 Módulo de simulación".capitalize()
        op6 = "6 Salir".capitalize()

        print(op1.center(120, " "))
        print(op2.center(120, " "))
        print(op3.center(120, " "))
        print(op4.center(120, " "))
        print(op5.center(120, " "))
        print(op6.center(120, " "))

        opcion_mp = int(input("Introduzca una opcion del 1 al 6: "))

        if opcion_mp == 1:
            clear()
            menu_1()

        if opcion_mp == 2:
            clear()
            menu_2()

        if opcion_mp == 3:
            clear()
            menu_3()

        if opcion_mp == 4:
            clear()
            menu_4()

        if opcion_mp == 5:
            clear()
            menu_5()

        if opcion_mp == 6:
            clear()
            menu_6()


# menu_1 estadisticas de pitcheo
def menu_1():
    titulo()
    print(" ")

    op1_1 = "1 estadisticas de pitcheo por equipo".capitalize()
    op2_1 = "2 lideres de pitcheo en el torneo".capitalize()
    op3_1 = "3 regresar al menu anterior ".capitalize()

    print(op1_1.center(120, " "))
    print(op2_1.center(120, " "))
    print(op3_1.center(120, " "))

    opcion_1 = int(input("introduzca la opcion que desea: "))

    while opcion_1 < 1 or opcion_1 > 3:
        titulo()
        menu_1()

    if opcion_1 == 1:
        titulo()
        estadisticas_pitcher()

    if opcion_1 == 2:
        titulo()
        lideres_pitcheo()

    if opcion_1 == 3:
        titulo()
        menu()


# menu_2 estadisticas de bateo
def menu_2():
    titulo()
    print(" ")

    op1_2 = "1 estadisticas de bateo por equipo".capitalize()
    op2_2 = "2 lideres de bateo en el torneo".capitalize()
    op3_2 = "3 regresar al menu anterior ".capitalize()

    print(op1_2.center(120, " "))
    print(op2_2.center(120, " "))
    print(op3_2.center(120, " "))

    opcion_2 = int(input("introduzca la opcion que desea: "))

    while opcion_2 < 1 or opcion_2 > 3:
        titulo()
        menu_2()

    if opcion_2 == 1:
        titulo()
        estadisticas_bateo()

    if opcion_2 == 2:
        titulo()
        lideres_bateo()

    if opcion_2 == 3:
        titulo()
        menu()


# menu_3 estadisticas defensivas
def menu_3():
    titulo()
    print(" ")

    op1_3 = "1 estadisticas defensivas por equipo".capitalize()
    op2_3 = "2 equipos lideres en defensa en el torneo".capitalize()
    op3_3 = "3 regresar al menu anterior ".capitalize()

    print(op1_3.center(120, " "))
    print(op2_3.center(120, " "))
    print(op3_3.center(120, " "))

    opcion_3 = int(input("introduzca la opcion que desea: "))

    while opcion_3 < 1 or opcion_3 > 3:
        titulo()
        menu_3()

    if opcion_3 == 1:
        titulo()
        estadisticas_defensivas()

    if opcion_3 == 2:
        titulo()
        lideres_defensa()

    if opcion_3 == 3:
        titulo()
        menu()


# menu_4 estadisticas colectivas
def menu_4():
    titulo()
    print(" ")

    op1_4 = "1 tabla de posiciones de los equipos de la liga".capitalize()
    op2_4 = "2 regresar al menu anterior".capitalize()

    print(op1_4.center(120, " "))
    print(op2_4.center(120, " "))

    opcion_4 = int(input("introduzca la opcion que desea: "))

    while opcion_4 < 1 or opcion_4 > 2:
        titulo()
        menu_4()

    if opcion_4 == 1:
        titulo()
        estadisticas_colectivas()

    if opcion_4 == 2:
        titulo()
        menu()


# menu 5 simulacionnnnnnn
def menu_5():
    titulo()
    print(" ")

    op1_5 = "1 simulacion de equipos elegidos por el usuario ".capitalize()
    op2_5 = "2 simulacion aleatoria".capitalize()
    op3_5 = "3 regresar al menu anterior".capitalize()

    print(op1_5.center(120, " "))
    print(op2_5.center(120, " "))
    print(op3_5.center(120, " "))

    opcion_5 = int(input("introduzca la opcion que desea: "))

    while opcion_5 < 1 or opcion_5 > 3:
        titulo()
        menu_5()

    if opcion_5 == 1:
        simulacion_equipos(False)

    if opcion_5 == 2:
        titulo()
        simulacion_equipos(True)

    if opcion_5 == 3:
        titulo()
        menu()


def menu_6():
    titulo()
    print(" ")

    op1_6 = "1 cerrar programa ".capitalize()
    op2_6 = "2 regresar al menu anterior".capitalize()

    print(op1_6.center(120, " "))
    print(op2_6.center(120, " "))

    opcion_6 = int(input("introduzca la opcion que desea: "))

    while opcion_6 < 1 or opcion_6 > 2:
        titulo()
        menu_6()

    if opcion_6 == 1:
        clear()
        sys.exit()
    if opcion_6 == 2:
        titulo()
        menu()


# Imprimir tabla de Pretty Table
def mostrar_datos_en_tabla(columnas, datos, titulo_tabla):
    tabla = PrettyTable()
    tabla.field_names = columnas
    for d in datos:
        tabla.add_row(d)
    print(tabla)

    def archivo_p():
        with open("Tablas_estadisticas.txt", "a") as filep:
            filep.write("\n" + titulo_tabla + "\n\n")
            filep.write(str(tabla) + "\n")
            filep.write(" ")

    archivo_p()


# funcion para mostrar solo los equipos sin los datos numericos
def cambio_formato_equipo(equipo):
    equipo = equipo.split(" ", 1)[1]
    equipo = equipo.rsplit(" ", 3)[0]
    return equipo


# llamado de la sub opcion 1 del menu 1
def estadisticas_pitcher():
    ini = "@@@@@"
    fin = "@@@@-"

    # equipos = OpenFile(ini, fin)
    print(" ")
    for equipo in equipos:
        # eq = cambio_formato_equipo(equipo)
        eq = str(equipo["id"]) + ")" + equipo["equipo"]
        print(eq.center(120, " "))

    back = str(len(equipos) + 1) + ") regresar menu principal"
    print(back.center(120, " "))

    op_equipo_pitcher = 0

    while op_equipo_pitcher < 1 or op_equipo_pitcher > len(equipos) + 1:
        op_equipo_pitcher = int(input("introduce el equipo que deseas seleccionar: "))

    if 1 <= op_equipo_pitcher <= len(equipos):
        datos_pitcher(pitchers, op_equipo_pitcher, equipos[op_equipo_pitcher - 1])
    elif op_equipo_pitcher == len(equipos) + 1:
        clear()
        menu()
    else:
        print(
            "Opción no válida. Por favor, introduce un número entre 1 y "
            + str(len(equipos) + 1)
        )


def obtener_estadisticas_equipo(equipo):
    estadisticas = equipo.rsplit(" ", 3)[1]
    return estadisticas


def datos_pitcher(pitchers, op_equipo_pitcher, equipo):
    clear()
    titulo()
    print(" ")
    print(equipo["equipo"].center(120, " "))
    print(" ")
    haypitcher = False

    tabla_p = PrettyTable()
    columnas_pitchers = [
        "ID",
        "#",
        "Nom",
        "Ape",
        "Pos",
        "P",
        "BB",
        "H",
        "IL",
        "CL",
        "EFE",
        "WHIP",
        "P/BB",
    ]
    tabla_p.field_names = columnas_pitchers

    for pitcher in pitchers:
        if pitcher["id_equipo"] == int(op_equipo_pitcher):
            haypitcher = True
            valores_p = [
                pitcher["id_equipo"],
                pitcher["#"],
                pitcher["Nom"],
                pitcher["Ape"],
                pitcher["Pos"],
                pitcher["P"],
                pitcher["BB"],
                pitcher["H"],
                pitcher["IL"],
                pitcher["CL"],
                pitcher["EFE"],
                pitcher["WHIP"],
                pitcher["P/BB"],
            ]
            tabla_p.add_row(valores_p)

    if haypitcher:
        print(tabla_p)

    else:
        print("el equipo seleccionado no tiene pitcher".center(120, " "))

    pausa()


# sub opcion de lideres en pitcheo
def lideres_pitcheo():
    print(" ")
    op1 = "lideres en efectividad"
    op2 = "lideres en ponche"
    op3 = "lideres en WHIP"
    print(op1.center(120, " "))

    lidersEO = sorted(pitchers, key=lambda p: p["EFE"], reverse=False)
    p_lidersEO = agrupar_lideres_pitcheo(lidersEO, "EFE")
    mostrar_datos_en_tabla(
        ["N.", "Nom", "Ape", "Equipo", "EFE"], p_lidersEO, "Lideres en efectividad"
    )

    print(op2.center(120, " "))

    liderPO = sorted(pitchers, key=lambda p: p["P"], reverse=True)
    p_lidersPO = agrupar_lideres_pitcheo(liderPO, "P")
    mostrar_datos_en_tabla(
        ["N.", "Nom", "Ape", "Equipo", "P"], p_lidersPO, "Lideres en ponches"
    )

    print(op3.center(120, " "))

    liderWO = sorted(pitchers, key=lambda p: p["WHIP"], reverse=False)
    p_lidersWO = agrupar_lideres_pitcheo(liderWO, "WHIP")
    mostrar_datos_en_tabla(
        ["N.", "Nom", "Ape", "Equipo", "WHIP"], p_lidersWO, "Lideres en whip"
    )

    pausa()


def nombre_equipo(numequipo):
    ini = "@@@@@"
    fin = "@@@@-"
    datos_equipo = OpenFile(ini, fin)
    for equipo in datos_equipo:
        if equipo[0:1] == numequipo:
            return cambio_formato_equipo(equipo)


# llamado de la sub opcion 1 del menu 2
def estadisticas_bateo():
    ini = "@@@@@"
    fin = "@@@@-"

    # equipos = OpenFile(ini, fin)
    print(" ")
    for equipo in equipos:
        #     eq = cambio_formato_equipo(equipo)
        eq = str(equipo["id"]) + ")" + equipo["equipo"]
        print(eq.center(120, " "))

    ultimaop = str(len(equipos) + 1) + ") regresar menu principal"
    print(ultimaop.center(120, " "))

    op_equipo_bateo = 0

    while op_equipo_bateo < 1 or op_equipo_bateo > len(equipos) + 1:
        op_equipo_bateo = int(input("introduce el equipo que deseas seleccionar: "))

    if 1 <= op_equipo_bateo <= len(equipos):
        datos_bateador(bateadores, op_equipo_bateo, equipos[op_equipo_bateo - 1])
    elif op_equipo_bateo == len(equipos) + 1:
        clear()
        menu()
    else:
        print(
            "Opción no válida. Por favor, introduce un número entre 1 y "
            + str(len(equipos) + 1)
        )


def datos_bateador(bateadores, op_equipo_bateo, equipo):
    clear()
    titulo()
    print(" ")
    print(equipo["equipo"].center(120, " "))
    print(" ")
    haybateador = 0
    tabla_b = PrettyTable()
    columnas_bateadores = [
        "ID",
        "#",
        "Nom",
        "Ape",
        "Pos",
        "H",
        "BB",
        "HBP",
        "SF",
        "TB",
        "2B",
        "3B",
        "HR",
        "CI",
        "PRO",
        "OBP",
        "SLG",
    ]
    tabla_b.field_names = columnas_bateadores
    for bateador in bateadores:
        if bateador["id_equipo_b"] == int(op_equipo_bateo):
            haybateador = True
            valores_b = [
                bateador["id_equipo_b"],
                bateador["#"],
                bateador["Nom"],
                bateador["Ape"],
                bateador["Pos"],
                bateador["H"],
                bateador["BB"],
                bateador["HBP"],
                bateador["SF"],
                bateador["TB"],
                bateador["2B"],
                bateador["3B"],
                bateador["HR"],
                bateador["CI"],
                bateador["PRO"],
                bateador["OBP"],
                bateador["SLG"],
            ]
            tabla_b.add_row(valores_b)

    if haybateador:
        print(tabla_b)

    else:
        print("el equipo seleccionado no tiene bateador".center(120, " "))

    pausa()


def agrupar_lideres_bateo(lideres, metrica):
    top = 0
    r_lideres = []
    for bateador in lideres:
        top += 1
        if top < 4:
            lider = [
                top,
                bateador["Nom"],
                bateador["Ape"],
                obtener_nombre_equipo_por_id(bateador["id_equipo_b"]),
                bateador[metrica],
            ]
            r_lideres.append(lider)

    return r_lideres


# sub opcion de lideres en bateo
def lideres_bateo():
    print(" ")
    op1_b = "Lideres en Home Run"
    op2_b = "Lideres en Hits"
    op3_b = "Lideres en carreras impulsadas"

    print(op1_b.center(120, " "))

    liderHRo = sorted(bateadores, key=lambda b: b["HR"], reverse=True)
    lideresHro = agrupar_lideres_bateo(liderHRo, "HR")
    mostrar_datos_en_tabla(
        ["N.", "Nom", "Ape", "Equipo", "HR"], lideresHro, "Lideres en Home Runs"
    )

    print(op2_b.center(120, " "))

    liderHo = sorted(bateadores, key=lambda b: b["H"], reverse=True)
    lideresHo = agrupar_lideres_bateo(liderHo, "H")
    mostrar_datos_en_tabla(
        ["N.", "Nom", "Ape", "Equipo", "H"], lideresHo, "Lideres en Hits"
    )

    print(op3_b.center(120, " "))

    liderCI = sorted(bateadores, key=lambda b: b["CI"], reverse=True)
    lideresCI = agrupar_lideres_bateo(liderCI, "CI")
    mostrar_datos_en_tabla(
        ["N.", "Nom", "Ape", "Equipo", "CI"],
        lideresCI,
        "Lideres en carreras impulsadas",
    )

    pausa()


# llamado de la subopcion 1 del submenu 3 (estadisticas defensivas por equipo)


def estadisticas_defensivas():
    print(" ")
    for equipo in equipos:
        eq = str(equipo["id"]) + ")" + equipo["equipo"]
        print(eq.center(120, " "))

    ultimaop2 = str(len(equipos) + 1) + ") regresar menu principal"
    print(ultimaop2.center(120, " "))

    op_equipo_defensi = 0

    while op_equipo_defensi < 1 or op_equipo_defensi > len(equipos) + 1:
        op_equipo_defensi = int(input("introduce el equipo que deseas seleccionar: "))

    if 1 <= op_equipo_defensi <= len(equipos):
        datos_defensas(defensores, op_equipo_defensi, equipos[op_equipo_defensi - 1])
    elif op_equipo_defensi == len(equipos) + 1:
        clear()
        menu()
    else:
        print(
            "Opción no válida. Por favor, introduce un número entre 1 y "
            + str(len(equipos) + 1)
        )


# defensa
def datos_defensas(defensores, op_equipo_defensi, equipo):
    clear()
    titulo()
    print(" ")
    print(equipo["equipo"].center(120, " "))
    print(" ")
    haydefensa = False

    tabla_d = PrettyTable()
    columnas_defensas = [
        "ID",
        "#",
        "Nom",
        "Ape",
        "Pos",
        "JJ",
        "O",
        "A",
        "E",
        "DP",
        "F%",
        "TL",
        "DP/J",
    ]
    tabla_d.field_names = columnas_defensas

    for defensa in defensores:
        if defensa["id_d"] == int(op_equipo_defensi):
            haydefensa = True
            valores_d = [
                defensa["id_d"],
                defensa["#_d"],
                defensa["Nom_d"],
                defensa["Ape_d"],
                defensa["Pos_d"],
                defensa["JJ_d"],
                defensa["O_d"],
                defensa["A_d"],
                defensa["E_d"],
                defensa["DP_d"],
                defensa["F%"],
                defensa["TL"],
                defensa["DP/J"],
            ]
            tabla_d.add_row(valores_d)

    if haydefensa:
        print(tabla_d)

    else:
        print("el equipo seleccionado no tiene defensor".center(120, " "))

    pausa()


# pausa para ralentizar el programa
def pausa():
    print(" ")
    n = input("pulse cualquier tecla para continuar ")


def agrupar_lideres_defensa(lideres, metrica):
    top = 0
    r_lideres = []
    for defensa in lideres:
        top += 1
        if top < 4:
            lider = [
                top,
                obtener_nombre_equipo_por_id(defensa["id_d"]),
                defensa[metrica],
            ]
            r_lideres.append(lider)

    return r_lideres


# sub opcion de lideres en defensa
def lideres_defensa():
    print(" ")
    op1_d = "Defensiva con el mejor porcentaje de fildeo"
    op2_d = "Defensiva líder en precisión"
    op3_d = "Defensiva con el mejor doble play por juego"
    print(op1_d.center(120, " "))

    liderDF = sorted(defensores, key=lambda d: d["F%"], reverse=False)
    d_lideresDF = agrupar_lideres_defensa(liderDF, "F%")
    mostrar_datos_en_tabla(
        ["N", "Equipo", "F%"], d_lideresDF, "Lideres en mejor porcentaje de Fildeo"
    )

    print(op2_d.center(120, " "))

    liderDFE = sorted(defensores, key=lambda d: d["TL"], reverse=True)
    d_lideresDFE = agrupar_lideres_defensa(liderDFE, "TL")
    mostrar_datos_en_tabla(["N", "Equipo", "TL"], d_lideresDFE, "Lideres en precision")

    print(op3_d.center(120, " "))

    liderDIDI = sorted(defensores, key=lambda d: d["DP/J"], reverse=True)
    d_lideresDIDI = agrupar_lideres_defensa(liderDIDI, "DP/J")
    mostrar_datos_en_tabla(
        ["N", "Equipo", "DP/J"], d_lideresDIDI, "Lideres en Doble Play por Juego"
    )

    pausa()


def nombre_equipo(numequipo):
    ini = "@@@@@"
    fin = "@@@@-"
    datos_equipo = OpenFile(ini, fin)
    for equipo in datos_equipo:
        if equipo[0:1] == numequipo:
            return cambio_formato_equipo(equipo)


# llamado de la subopcion 1 del menu 4 (estadisticas colectivas)


def estadisticas_colectivas():
    print(" ")

    op1_e = "Tabla de Posiciones"
    print(" ")
    print(op1_e.center(120, " "))

    equipos_por_average = obtener_equipos_por_average()

    mostrar_tabla_lider_equipo(equipos_por_average)


def mostrar_tabla_lider_equipo(equipos_por_average):
    tabla_e = PrettyTable()
    columnas_equipos = ["Equipo", "JJ", "JG", "JP", "AVE", "DIF"]
    tabla_e.field_names = columnas_equipos
    for equipo in equipos_por_average:
        valores = [
            equipo["equipo"],
            equipo["JJ"],
            equipo["JG"],
            equipo["JP"],
            equipo["AVE"],
            equipo["DIF"],
        ]
        tabla_e.add_row(valores)

        # Imprimir la tabla
    print(tabla_e)

    def archivo_eq():
        with open("Tablas_estadisticas.txt", "a") as file_eq:
            file_eq.write("\n" + "Tabla colectiva" + "\n\n")
            file_eq.write(str(tabla_e) + "\n")
            file_eq.write(" ")

    archivo_eq()

    pausa()


def nombre_equipo(numequipo):
    ini = "@@@@@"
    fin = "@@@@-"
    datos_equipo = OpenFile(ini, fin)
    for equipo in datos_equipo:
        if equipo[0:1] == numequipo:
            return cambio_formato_equipo(equipo)


def lider_equipos(tipo):
    ini = "@@@@@"
    fin = "@@@@-"
    datos_equipos = OpenFile(ini, fin)
    lideres_e = []
    for equipos in datos_equipos:
        detalle = equipos.split()
        nombre = detalle[2] + " " + detalle[3]
        print("nnnm: ", nombre)
        equipo = nombre_equipo(detalle[0])
        if tipo == 1:
            valor = calcular_ave(detalle[5], detalle[4])

        lideres_e.append([nombre, equipo, valor])
    return lideres_e


def calcular_ave(JG, JJ):
    if int(JG) >= 0 and int(JJ) > 0:
        return round(float(JG) / float(JJ), 3)

    return 0


def agrupar_lideres_pitcheo(lideres, metrica):
    top = 0
    r_lideres = []
    for pitcher in lideres:
        top += 1
        if top < 4:
            lider = [
                top,
                pitcher["Nom"],
                pitcher["Ape"],
                obtener_nombre_equipo_por_id(pitcher["id_equipo"]),
                pitcher[metrica],
            ]
            r_lideres.append(lider)

    return r_lideres


# menu 1 opcion 5


def simulacion_equipos(aleatorio):
    clear()
    titulo()
    print(" ")

    for equipo in equipos:
        eq = str(equipo["id"]) + ")" + equipo["equipo"]
        print(eq.center(120, " "))

    ultimaop2 = str(len(equipos) + 1) + ") regresar menu anterior"
    print(ultimaop2.center(120, " "))

    print(" ")

    if aleatorio == True:
        op_equipo_sim = random.randint(1, len(equipos))
        op_equipo_sim2 = random.randint(1, len(equipos))

        if op_equipo_sim == op_equipo_sim2:
            simulacion_equipos(aleatorio)
            return

    if aleatorio == False:
        op_equipo_sim = int(
            input("Introduce el primer equipo que deseas seleccionar: ")
        )
        if op_equipo_sim == len(equipos) + 1:
            clear()
            titulo()
            menu_5()
            return
        op_equipo_sim2 = int(
            input("Introduce el segundo equipo que deseas seleccionar: ")
        )
        if op_equipo_sim2 == len(equipos) + 1:
            clear()
            titulo()
            menu_5()
            return

    if op_equipo_sim == op_equipo_sim2:
        print("No se puede realizar una simulacion entre dos equipos iguales")
        simulacion_equipos(aleatorio)
        return

    if (1 <= op_equipo_sim <= len(equipos)) and (
        1 <= op_equipo_sim2 <= len(equipos)
    ):
        # puntaje de los equipos
        puntaje_equipo1 = 0
        puntaje_equipo2 = 0
        # parametro ponches
        ponches_equipo1 = 0
        pitchers_equipo1 = 0

        ponches_equipo2 = 0
        pitchers_equipo2 = 0

        for p in pitchers:
            if p["id_equipo"] == op_equipo_sim:
                ponches_equipo1 += p["P"]
                pitchers_equipo1 += 1

            if p["id_equipo"] == op_equipo_sim2:
                ponches_equipo2 += p["P"]
                pitchers_equipo2 += 1

        print("Lider en Ponches (estadisticas pitcher)".center(120, " "))

        if pitchers_equipo1 > 0:
            promedio_ponches_equipo1 = round(ponches_equipo1 / pitchers_equipo1, 2)
        else:
            promedio_ponches_equipo1 = 0

        if pitchers_equipo2 > 0:
            promedio_ponches_equipo2 = round(ponches_equipo2 / pitchers_equipo2, 2)
        else:
            promedio_ponches_equipo2 = 0

        equipos_ponches = []

        if promedio_ponches_equipo1 > promedio_ponches_equipo2:
            equipos_ponches.append(
                [
                    1,
                    (obtener_nombre_equipo_por_id(op_equipo_sim)),
                    promedio_ponches_equipo1,
                ]
            )
            equipos_ponches.append(
                [
                    2,
                    (obtener_nombre_equipo_por_id(op_equipo_sim2)),
                    promedio_ponches_equipo2,
                ]
            )
        else:
            equipos_ponches.append(
                [
                    1,
                    (obtener_nombre_equipo_por_id(op_equipo_sim2)),
                    promedio_ponches_equipo2,
                ]
            )
            equipos_ponches.append(
                [
                    2,
                    (obtener_nombre_equipo_por_id(op_equipo_sim)),
                    promedio_ponches_equipo1,
                ]
            )

        mostrar_datos_en_tabla(
            ["N.", "Equipo", "Promedio Ponches"],
            equipos_ponches,
            "Simulacion promedio Ponches",
        )

        if promedio_ponches_equipo1 > promedio_ponches_equipo2:
            puntaje_equipo1 += 1
            print(
                f"{obtener_nombre_equipo_por_id(op_equipo_sim)} tiene {puntaje_equipo1} punto"
            )
        else:
            puntaje_equipo2 += 1
            print(
                f"{obtener_nombre_equipo_por_id(op_equipo_sim2)} tiene {puntaje_equipo2} punto"
            )

        # parametro Home Runs(bateadores)
        hr_equipo1 = 0
        bateadores_equipo1 = 0

        hr_equipo2 = 0
        bateadores_equipo2 = 0

        for b in bateadores:
            if b["id_equipo_b"] == op_equipo_sim:
                hr_equipo1 += b["HR"]
                bateadores_equipo1 += 1

            if b["id_equipo_b"] == op_equipo_sim2:
                hr_equipo2 += b["HR"]
                bateadores_equipo2 += 1

        print("Lider en Home Runs (estadisticas bateadores)".center(120, " "))

        if bateadores_equipo1 > 0:
            promedio_hr_equipo1 = round(hr_equipo1 / bateadores_equipo1, 2)
        else:
            promedio_hr_equipo1 = 0

        if bateadores_equipo2 > 0:
            promedio_hr_equipo2 = round(hr_equipo2 / bateadores_equipo2, 2)
        else:
            promedio_hr_equipo2 = 0

        equipos_hr = []

        if promedio_hr_equipo1 > promedio_hr_equipo2:
            equipos_hr.append(
                [
                    1,
                    (obtener_nombre_equipo_por_id(op_equipo_sim)),
                    promedio_hr_equipo1,
                ]
            )
            equipos_hr.append(
                [
                    2,
                    (obtener_nombre_equipo_por_id(op_equipo_sim2)),
                    promedio_hr_equipo2,
                ]
            )
        else:
            equipos_hr.append(
                [
                    1,
                    (obtener_nombre_equipo_por_id(op_equipo_sim2)),
                    promedio_hr_equipo2,
                ]
            )
            equipos_hr.append(
                [
                    2,
                    (obtener_nombre_equipo_por_id(op_equipo_sim)),
                    promedio_hr_equipo1,
                ]
            )

        mostrar_datos_en_tabla(
            ["N.", "Equipo", "Promedio Home Runs"],
            equipos_hr,
            "Simulacion promedio Home Runs",
        )

        if promedio_hr_equipo1 > promedio_hr_equipo2:
            puntaje_equipo1 += 1
            print(
                f"{obtener_nombre_equipo_por_id(op_equipo_sim)} tiene {puntaje_equipo1} puntos"
            )
        else:
            puntaje_equipo2 += 1
            print(
                f"{obtener_nombre_equipo_por_id(op_equipo_sim2)} tiene {puntaje_equipo2} puntos"
            )

        print

        # parametros defensas

        outs_equipo1 = 0
        defensores_equipo1 = 0

        outs_equipo2 = 0
        defensores_equipo2 = 0

        for d in defensores:
            if d["id_d"] == op_equipo_sim:
                outs_equipo1 += d["O_d"]
                defensores_equipo1 += 1

            if d["id_d"] == op_equipo_sim2:
                outs_equipo2 += d["O_d"]
                defensores_equipo2 += 1

        print("Lideres en Outs (estadisticas defensivas)".center(120, " "))

        if defensores_equipo1 > 0:
            promedio_outs_equipo1 = round(outs_equipo1 / defensores_equipo1, 2)
        else:
            promedio_outs_equipo1 = 0

        if defensores_equipo2 > 0:
            promedio_outs_equipo2 = round(outs_equipo2 / defensores_equipo2, 2)
        else:
            promedio_outs_equipo2 = 0

        equipos_out = []

        if promedio_outs_equipo1 > promedio_outs_equipo2:
            equipos_out.append(
                [
                    1,
                    (obtener_nombre_equipo_por_id(op_equipo_sim)),
                    promedio_outs_equipo1,
                ]
            )
            equipos_out.append(
                [
                    2,
                    (obtener_nombre_equipo_por_id(op_equipo_sim2)),
                    promedio_outs_equipo2,
                ]
            )
        else:
            equipos_out.append(
                [
                    1,
                    (obtener_nombre_equipo_por_id(op_equipo_sim2)),
                    promedio_outs_equipo2,
                ]
            )
            equipos_out.append(
                [
                    2,
                    (obtener_nombre_equipo_por_id(op_equipo_sim)),
                    promedio_outs_equipo1,
                ]
            )

        mostrar_datos_en_tabla(
            ["N.", "Equipo", "Promedio Outs"],
            equipos_out,
            "Simulacion promedio de Outs",
        )

        if promedio_outs_equipo1 > promedio_outs_equipo2:
            puntaje_equipo1 += 1
            print(
                f"{obtener_nombre_equipo_por_id(op_equipo_sim)} tiene {puntaje_equipo1} puntos"
            )
        else:
            puntaje_equipo2 += 1
            print(
                f"{obtener_nombre_equipo_por_id(op_equipo_sim2)} tiene {puntaje_equipo2} puntos"
            )

        print("Equipo Ganador".center(120, " "))

        equipo_ganador = []

        if puntaje_equipo1 > puntaje_equipo2:
            equipo_ganador.append([obtener_nombre_equipo_por_id(op_equipo_sim)])
        else:
            equipo_ganador.append([obtener_nombre_equipo_por_id(op_equipo_sim2)])

        mostrar_datos_en_tabla(
            ["Equipo Ganador"], equipo_ganador, "Simulacion equipo ganador"
        )

        pausa()


# inicio de programa principal
menu()
