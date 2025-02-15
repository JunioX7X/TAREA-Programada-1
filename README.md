# TAREA-Programada-1
Un poco de DATOS DE NFL con metodos de ordenamiento

# Análisis de Jugadas de Punt (NFL 2009-2017)

Proyecto para procesar y ordenar datos históricos de jugadas de punt de la NFL utilizando múltiples algoritmos de ordenamiento.

---

## 🛠️ Requisitos
- Python 3.8+
- Archivos CSV anuales de jugadas (2009-2017) en `/data/primeraprogramada/`

---

## 📂 Estructura del Proyecto

---

## 🧩 Componentes Clave

### 1. Clase `punt_play` (`punt_play2.py`)
Modela una jugada de punt con:
- ID del juego
- Equipos (formato `AwayTeam@HomeTeam`)
- Yardas
- Cuarto
- Fecha y hora

### 2. Lector de Datos (`lector_data_parte2.py`)
- **Método `read_punts()`**:
  - Lee archivos CSV anuales (2009-2017)
  - Filtra jugadas válidas (que contengan "punts" sin "fumble")
  - Crea objetos `punt_play`

### 3. Comparador Personalizado (`play_comparator.py`)
Define el orden prioritario:
1. Fecha (`_date`)
2. Cuarto (`_quarter`)
3. Yardas (`_yards`)
4. Hora (`_time`)

### 4. Algoritmos de Ordenamiento (`algoritmos_ordenamiento_parte2.py`)
| Algoritmo | Tipo | Optimizaciones |
|-----------|------|----------------|
| Bubble Sort | Estable | - |
| Insertion Sort | Estable | Versión interna para subarrays |
| Merge Sort | Recursivo/Iterativo | Combinación ordenada |
| Quicksort | Recursivo/Iterativo | Mediana de 3 + Insertion para subarrays ≤10 |

### 5. Script Principal (`main_parte2.py`)
Flujo de ejecución:
1. Lee y agrupa jugadas por año
2. Ejecuta 6 algoritmos de ordenamiento
3. Genera archivos CSV con resultados ordenados

---

## 🚀 Ejecución
```bash
# Configurar datos (ejemplo estructura Linux/Mac)
mkdir -p /data/primeraprogramada
mv pbp_2009.csv pbp_2010.csv ... /data/primeraprogramada/

# Ejecutar análisis
python main_parte2.py

parte2-bubble-sort-resultado_2015.csv
parte2-merge-sort-rec-resultado_2016.csv
...

Métricas Clave
Tiempos de ejecución por algoritmo/año registrados en consola
Ejemplo salida:
Copy code
TIME (2015): 0.4587 segundos (merge_sort_recursivo)
Resultados guardados en: /data/.../parte2-merge-sort-rec-resultado_20
