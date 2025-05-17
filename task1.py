import random
import time
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(1000000)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def measure_time(sort_func, array, repeats=5):
    times = []
    for _ in range(repeats):
        arr_copy = array.copy()
        start = time.time()
        sort_func(arr_copy)
        end = time.time()
        times.append(end - start)
    return sum(times) / repeats

if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    randomized_times = []
    deterministic_times = []

    for size in sizes:
        array = [random.randint(0, 1_000_000) for _ in range(size)]

        r_time = measure_time(randomized_quick_sort, array)
        d_time = measure_time(deterministic_quick_sort, array)

        randomized_times.append(r_time)
        deterministic_times.append(d_time)

        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {r_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {d_time:.4f} секунд\n")

    plt.plot(sizes, randomized_times, label='Рандомізований QuickSort')
    plt.plot(sizes, deterministic_times, label='Детермінований QuickSort')
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.grid(True)
    plt.show()
