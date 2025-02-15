from lector_data import process_files
from algoritmos_ordenamiento import (
    bubble_sort,
    insertion_sort,
    merge_sort_recursivo,
    merge_sort_iterativo,
    quicksort_recursivo,
    quicksort_iterativo
)

def main():
    folder_path = r"C:\data\primeraprogramada"  # Using raw string for Windows path

    # Dictionary of algorithms and their names
    algorithms = [
        (bubble_sort, "bubble_sort"),
        (insertion_sort, "insertion_sort"),
        (merge_sort_recursivo, "merge_sort_recursivo"),
        (merge_sort_iterativo, "merge_sort_iterativo"),
        (quicksort_recursivo, "quicksort_recursivo"),
        (quicksort_iterativo, "quicksort_iterativo")
    ]

    # Process each algorithm
    for algorithm, name in algorithms:
        print(f"\nProcessing with {name}...")
        process_files(folder_path, algorithm, name)

if __name__ == "__main__":
    main()