import os
import csv
import time
from punt_play import punt_play

class lector_data:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        
    def read_file(self, filename):
        punt_plays = []
        with open(os.path.join(self.folder_path, filename), newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Verificar existencia de columnas críticas
            required_fields = ['GameID', 'HomeTeam', 'AwayTeam', 'Yards.Gained', 'qtr']
            if not all(field in reader.fieldnames for field in required_fields):
                raise ValueError(f"Archivo {filename} tiene estructura inválida")

            for row in reader:
                # Acceso robusto al campo de descripción
                desc_field = row.get('desc') or row.get('Desc') or row.get('DESC') or ''
                
                if "punt" in desc_field.lower() and "fumble" not in desc_field.lower():
                    try:
                        game_id = row['GameID']
                        teams = f"{row['HomeTeam']} @ {row['AwayTeam']}"
                        yards = int(row['Yards.Gained'])
                        quarter = int(row['qtr'])
                        punt_plays.append(punt_play(game_id, teams, yards, quarter))
                    except (KeyError, ValueError) as e:
                        print(f"Error procesando fila en {filename}: {str(e)}")
                        continue
        
        return punt_plays

        
    
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Game ID", "Teams", "Yards", "Quarter"])
        for play in data:
            writer.writerow([play.game_id, play.teams, play.yards, play.quarter])
    
def process_files(folder_path, algorithm, algorithm_name):
    lector = lector_data(folder_path)
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            year = filename.split("_")[-1].split(".")[0]  # Extraer el año del nombre del archivo
            punt_plays = lector.read_file(filename)

            # Ordenar con el algoritmo especificado
            start_time = time.time()
            if algorithm_name == "bubble_sort":
                sorted_plays, comparisons, swaps = algorithm(punt_plays)
            elif algorithm_name == "insertion_sort":
                sorted_plays, comparisons, swaps = algorithm(punt_plays)
            end_time = time.time()

            if algorithm_name == "merge_sort_recursivo":
                sorted_plays, comparisons, swaps = algorithm(punt_plays)
            elif algorithm_name == "merge_sort_iterativo":
                sorted_plays, comparisons, swaps = algorithm(punt_plays)
            end_time = time.time()
 
            if algorithm_name == "quicksort_recursivo":
                sorted_plays, comparisons, swaps = algorithm(punt_plays)    
            elif algorithm_name == "quicksort_iterativo":
                sorted_plays, comparisons, swaps = algorithm(punt_plays)
            end_time = time.time()

            if algorithm_name == "bubble_sort":
                sorted_plays, comparisons, swaps = algorithm(punt_plays)
            elif algorithm_name == "insertion_sort":
                sorted_plays, comparisons, swaps = algorithm(punt_plays)
            end_time = time.time()
 
 

            

            # Guardar resultados en un archivo CSV
            output_filename = f"primera_parte-{algorithm_name}-{year}-resultado.csv"
            save_to_csv(sorted_plays, output_filename)

            # Imprimir estadísticas
            print(f"Archivo: {filename}")
            print(f"Algoritmo: {algorithm_name}")
            print(f"Tiempo de inicio: {start_time}, Duración: {end_time - start_time}, Tiempo final: {end_time}")
            print(f"Comparaciones: {comparisons}, Intercambios: {swaps}")
            print("-" * 50)