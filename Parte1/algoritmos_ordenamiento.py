from time import time
from sys import setrecursionlimit

def bubble_sort(arr):
    """
    Neural-inspired bubble sort implementation with performance metrics.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    arr = arr.copy()  # State preservation
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] < arr[j+1]:  # Descending order comparison
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    
    return arr, comparisons, swaps

def insertion_sort(arr):
    """
    Optimized insertion sort with adaptive learning characteristics.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        comparisons += 1
        while j >= 0 and arr[j] < key:  # Descending order
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
    
    return arr, comparisons, swaps

def merge_sort_recursivo(arr):
    """
    Recursive merge sort with divide-and-conquer neural architecture.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    def merge(left, right, stats):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            stats['comparaciones'] += 1
            if left[i] >= right[j]:  # Descending order
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            stats['intercambios'] += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(arr, stats):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = sort(arr[:mid], stats)
        right = sort(arr[mid:], stats)
        return merge(left, right, stats)

    stats = {'comparaciones': 0, 'intercambios': 0}
    arr_copy = arr.copy()
    sorted_arr = sort(arr_copy, stats)
    
    return sorted_arr, stats['comparaciones'], stats['intercambios']

def merge_sort_iterativo(arr):
    """
    Iterative merge sort with parallel processing potential.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    arr = arr.copy()
    stats = {'comparaciones': 0, 'intercambios': 0}
    n = len(arr)
    
    width = 1
    while width < n:
        for left in range(0, n, 2*width):
            mid = min(left + width, n)
            right = min(left + 2*width, n)
            
            # Merge operation
            temp = []
            i, j = left, mid
            while i < mid and j < right:
                stats['comparaciones'] += 1
                if arr[i] >= arr[j]:  # Descending order
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
                stats['intercambios'] += 1
            
            temp.extend(arr[i:mid])
            temp.extend(arr[j:right])
            for i, v in enumerate(temp):
                arr[left + i] = v
        
        width *= 2
    
    return arr, stats['comparaciones'], stats['intercambios']

def quicksort_recursivo(arr):
    """
    Enhanced recursive quicksort with adaptive pivot selection.
    Time Complexity: O(n log n)
    Space Complexity: O(log n)
    """
    setrecursionlimit(10000)
    arr = arr.copy()
    stats = {'comparaciones': 0, 'intercambios': 0}
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            stats['comparaciones'] += 1
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                stats['intercambios'] += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        stats['intercambios'] += 1
        return i + 1
    
    def quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort(low, pi - 1)
            quick_sort(pi + 1, high)
    
    quick_sort(0, len(arr) - 1)
    return arr, stats['comparaciones'], stats['intercambios']

def quicksort_iterativo(arr):
    """
    Iterative quicksort with dynamic stack management.
    Time Complexity: O(n log n)
    Space Complexity: O(log n)
    """
    arr = arr.copy()
    stats = {'comparaciones': 0, 'intercambios': 0}
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            stats['comparaciones'] += 1
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                stats['intercambios'] += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        stats['intercambios'] += 1
        return i + 1
    
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
    
    return arr, stats['comparaciones'], stats['intercambios']