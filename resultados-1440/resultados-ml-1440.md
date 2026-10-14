# Reporte de Análisis de Datos - Pandas

`marco morquecho Machine Learning pandas, NC 1440`

## 1. DataFrame Convertido
```text
    Marca      Pais  Precio_promedio
0    Nike      EEUU              800
1  Adidas  Alemania              750
2    Puma  Alemania              700
3    Zara    España              500
4     H&M    Suecia              400
5  Levi's      EEUU              900
```

## 2.1 Primeras Filas (head) 1440
```text
    Marca      Pais  Precio_promedio
0    Nike      EEUU              800
1  Adidas  Alemania              750
```

## 2.2 Últimas Filas (tail) 1440
```text
    Marca    Pais  Precio_promedio
4     H&M  Suecia              400
5  Levi's    EEUU              900
```

## 2.3 Dimensiones (Filas, Columnas) 1440
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna 1440
```text
Marca                str
Pais                 str
Precio_promedio    int64
dtype: object
```

## 2.5 Información General (info) 1440
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   Marca            6 non-null      str  
 1   Pais             6 non-null      str  
 2   Precio_promedio  6 non-null      int64
dtypes: int64(1), str(2)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Precio_promedio'
```text
count      6.000000
mean     675.000000
std      189.076704
min      400.000000
25%      550.000000
50%      725.000000
75%      787.500000
max      900.000000
Name: Precio_promedio, dtype: float64
```

## 4. Ordenar Ascendente por Precio_promedio
```text
    Marca      Pais  Precio_promedio
4     H&M    Suecia              400
3    Zara    España              500
2    Puma  Alemania              700
1  Adidas  Alemania              750
0    Nike      EEUU              800
5  Levi's      EEUU              900
```

## 5. Ordenar Descendente por País
```text
    Marca      Pais  Precio_promedio
4     H&M    Suecia              400
3    Zara    España              500
0    Nike      EEUU              800
5  Levi's      EEUU              900
1  Adidas  Alemania              750
2    Puma  Alemania              700
```

`marco morquecho Machine Learning pandas, NC 1440`