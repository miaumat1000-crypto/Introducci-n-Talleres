# Comparaciones

En el caso del ejercicio del taller se usa el código para revisar si el valor de una medición es correcto y seguro, asegurándose de que no sea ni muy alto ni muy bajo (regla de calidad: -50 a 100).

Para procesar un archivo en C se utiliza la función fopen("datos.csv", "r") para abrirlo en modo lectura (y se verifica que no devuelva NULL).

## Explicación de cómo se leería un archivo con múltiples registros:

    1. Se omite la primera línea (los encabezados) mediante la función fgets().

    2. Se implementa un bucle while que lee línea por línea con fgets() hasta alcanzar el final del archivo (EOF), y se separan los valores por comas (sensor, temperatura, ubicacion) con strtok() o sscanf().

    3. Se toma el campo de temperatura (texto) y se convierte en un número con decimales (float) con strtof() o sscanf(); si la conversión falla, como con el valor "Vacio" del sensor S05, el registro se rechaza. Solo si la conversión funciona se verifica con validar_temperatura() que esté en el rango permitido.

    4. Los registros válidos y rechazados se escriben en archivos con fprintf(), y se cierra el archivo con fclose().

En C todo esto debe programarse manualmente (buffers, memoria, conversión de texto), por lo que el esfuerzo es mayor que en Python o SQL.


## CODIGO EN C

    #include <stdio.h>

    // Función para validar una temperatura individual (-50 a 100)
    int validar_temperatura(float temp) 
        {
            if (temp >= -50.0 && temp <= 100.0) 
                {
                    return 1; // Registro Válido
                }
            return 0; // Registro Inválido
        }

    int main() 
        {
            float temp_prueba = 24.5;
            if (validar_temperatura(temp_prueba)) 
                {
                    printf("Temperatura %.2f: VÁLIDA\n", temp_prueba);
                } 
                else 
                {
                    printf("Temperatura %.2f: INVÁLIDA\n", temp_prueba);
                }
            return 0;
        }
La biblioteca stdio.h es fundamental en este código porque proporciona las funciones de entrada y salida estándar indispensables para interactuar con la consola y los archivos del sistema. En esta implementación, permite utilizar printf() para mostrar en pantalla el resultado de la validación de las temperaturas de forma clara, además de ser la base necesaria para gestionar operaciones de lectura y escritura en archivos de texto o CSV