import random
import time
import matplotlib.pyplot as plt

def bubble_sort(A):
    A_copy = A.copy()
    n = len(A_copy)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if A_copy[j] > A_copy[j + 1]:
                A_copy[j], A_copy[j + 1] = A_copy[j + 1], A_copy[j]
                swapped = True
        if not swapped:
            break
    return A_copy


sizes = [10, 100, 500, 1000, 5000]
arrays = [[random.randint(0, 100) for _ in range(size)] for size in sizes]


print('Прогрев: начат')
for _ in range(100):
    bubble_sort(arrays[0]) # 10
    bubble_sort(arrays[1]) # 100
    bubble_sort(arrays[2]) # 500
print('Прогрев: окончен\n')


execution_times = []

for arr in arrays:
    average_time = 0
    for _ in range(10):
        start_time = time.perf_counter()
        A_sorted = bubble_sort(arr)
        end_time = time.perf_counter()
        average_time += (end_time - start_time)
    
    avg_final = average_time / 10
    execution_times.append(avg_final)
    print(f"Закончен подсчёт сортировки последовательности длиной: {len(arr)}\t{avg_final:.6f} сек.")


plt.style.use('dark_background')
plt.figure(figsize=(8, 6))
plt.plot(sizes, execution_times, marker='o', color='#ff7f7f', linewidth=2)
plt.title('Сортировка Пузырьком (Bubble Sort)')
plt.xlabel('Размер данных (N)')
plt.ylabel('Время выполнения (T, сек)')
plt.grid(True, linestyle='--', alpha=0.5)


filename = 'bubble_sort_graph.png'
plt.savefig(filename)
print(f"\nГрафик сохранен в файл: {filename}")