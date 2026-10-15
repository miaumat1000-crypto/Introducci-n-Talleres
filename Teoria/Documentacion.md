# DOCUMENTACIÓN DE LA SOLUCIÓN EN PYTHON (taller.py)

Objetivo
Leer mediciones de sensores desde datos.csv, validarlas, clasificarlas, calcular el promedio por ubicación y generar un archivo de registros válidos y otro de rechazados.

## REGLAS DE CALIDAD (hipotéticas, con fines pedagógicos)
    1. La temperatura debe ser numérica.
    2. El intervalo permitido es de -50 a 100 (ambos extremos incluidos).
    3. Las mediciones iguales o superiores a 35 se clasifican como "Alta"; el resto de las válidas son "Normal".
    4. Los registros inválidos deben identificarse (con su motivo) y contabilizarse.

## FUNCIONES
    - validar_temperatura(valor): intenta convertir el valor con float(). Retorna (True, temperatura) si es numérico y está en el rango; retorna (False, None) si no es numérico ("Vacio", cadena vacía, nan, inf) o está fuera de rango. Se reutiliza para cada fila.
    - clasificar_temperatura(valor): retorna "Alta" si valor >= 35, de lo contrario "Normal".
    - motivo_rechazo(valor): indica si el rechazo fue por "Temperatura no numérica" o "Temperatura fuera de rango (-50 a 100)".
    - procesar_registros(registros): recorre las filas reutilizando las funciones anteriores y retorna los válidos, los rechazados y el promedio por ubicación.
    - escribir_csv(...): genera validos.csv y rechazados.csv.
    - ejecutar_pruebas(): prueba la validación con datos válidos e inválidos (incluye los límites -50, 100 y 100.1).

