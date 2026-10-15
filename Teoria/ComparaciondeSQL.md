
En SQL los datos están organizados en tablas guardadas en una base de datos. Antes de hacer cualquier cálculo se descartan los datos erróneos o irrelevantes: los registros vacíos (NULL) y las temperaturas fuera del rango permitido (-50 a 100).

Como la columna temperatura es numérica (DECIMAL), el valor "Vacío" del sensor S05 no puede almacenarse como texto: se inserta como NULL, y el filtro BETWEEN lo excluye porque comparar NULL nunca es verdadero.

Se separan las lecturas por cada lugar usando GROUP BY y se calcula la temperatura media de cada uno con la función AVG().


## CODIGO EN SQL
### 1. Crear la tabla para almacenar las mediciones


    CREATE TABLE mediciones_sensores 
        (
            sensor VARCHAR(10),
            temperatura DECIMAL(5,2),
            ubicacion VARCHAR(50)
        );

### 2. Insertar los datos de entrada 
    ('S01', 24.5, 'Zona A'),
    ('S02', 38.2, 'Zona B'),
    ('S03', -80.0, 'Zona A'),
    ('S04', 31.0, 'Zona B'),
    ('S05', NULL, 'Zona A');

### 3. Filtrar valores válidos (-50 a 100) y calcular el promedio por ubicación
    SELECT 
        ubicacion,
        ROUND(AVG(temperatura), 2) AS promedio_temperatura
    FROM 
        mediciones_sensores
    WHERE 
        temperatura IS NOT NULL
        AND temperatura BETWEEN -50 AND 100
    GROUP BY 
        ubicacion;

-- Resultado esperado:
-- Zona A | 24.50
-- Zona B | 34.60
