
import csv
import math

TEMP_MIN = -50
TEMP_MAX = 100
UMBRAL_ALTA = 35


def validar_temperatura(valor):

    try:
        temperatura = float(valor)
    except (ValueError, TypeError):
        return False, None          

    if not math.isfinite(temperatura):
        return False, None          
    if TEMP_MIN <= temperatura <= TEMP_MAX:
        return True, temperatura
    return False, None             


def clasificar_temperatura(valor):

    return "Alta" if valor >= UMBRAL_ALTA else "Normal"


def motivo_rechazo(valor):
    
    try:
        numero = float(valor)
    except (ValueError, TypeError):
        return "Temperatura no numérica"
    if not math.isfinite(numero):
        return "Temperatura no numérica"
    return f"Temperatura fuera de rango ({TEMP_MIN} a {TEMP_MAX})"


def procesar_registros(registros):
    
    validos, rechazados = [], []
    sumas, conteos = {}, {}

    for fila in registros:
        es_valido, temperatura = validar_temperatura(fila["temperatura"])

        if es_valido:
            validos.append({
                "sensor": fila["sensor"],
                "temperatura": temperatura,
                "ubicacion": fila["ubicacion"],
                "clasificacion": clasificar_temperatura(temperatura),
            })
            zona = fila["ubicacion"]
            sumas[zona] = sumas.get(zona, 0.0) + temperatura
            conteos[zona] = conteos.get(zona, 0) + 1
        else:
            rechazados.append({
                "sensor": fila["sensor"],
                "temperatura": fila["temperatura"],
                "ubicacion": fila["ubicacion"],
                "motivo": motivo_rechazo(fila["temperatura"]),
            })

    promedios = {zona: sumas[zona] / conteos[zona] for zona in sumas}
    return validos, rechazados, promedios


def escribir_csv(nombre, campos, filas):
    with open(nombre, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas)


def ejecutar_pruebas():
   
    lineas = ["--- Prueba de validacion ---"]
    casos = ["24.5", "38.2", "-80.0", "Vacio", "-50", "100", "100.1", ""]
    for caso in casos:
        es_valido, _ = validar_temperatura(caso)
        lineas.append(f"valor: {caso!r:>8} -> ¿es valido?: {es_valido}")
    return lineas


def main():
   
    with open("datos.csv", mode="r", encoding="utf-8", newline="") as archivo:
        registros = list(csv.DictReader(archivo))

    
    validos, rechazados, promedios = procesar_registros(registros)

    
    escribir_csv("validos.csv",
                 ["sensor", "temperatura", "ubicacion", "clasificacion"], validos)
    escribir_csv("rechazados.csv",
                 ["sensor", "temperatura", "ubicacion", "motivo"], rechazados)

    
    salida = ejecutar_pruebas()
    salida += ["", "=== INDICADORES Y RESULTADOS ===",
               f"Registros leidos: {len(registros)}",
               f"Registros validos: {len(validos)}",
               f"Total de registros rechazados: {len(rechazados)}",
               "", "Promedio de temperatura por ubicacion:"]
    for zona, promedio in promedios.items():
        salida.append(f" - {zona}: {promedio:.2f} °C")
    salida += ["", "Archivos 'validos.csv' y 'rechazados.csv' generados con exito."]

    texto = "\n".join(salida)
    print(texto)
    with open("resultados", mode="w", encoding="utf-8") as f:
        f.write(texto + "\n")


if __name__ == "__main__":
    main()
