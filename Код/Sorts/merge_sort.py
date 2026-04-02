import random
import time
import matplotlib.pyplot as plt

def merge_sort(A):
    if len(A) <= 1:
        return A
    
    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


sizes = [10, 100, 500, 1000, 5000]
arrays = [[random.randint(0, 100) for _ in range(size)] for size in sizes]


print('Прогрев: начат')
for _ in range(100):
    merge_sort(arrays[0]) # 10
    merge_sort(arrays[1]) # 100
    merge_sort(arrays[2]) # 500
print('Прогрев: окончен\n')


execution_times = []

for arr in arrays:
    average_time = 0
    for _ in range(10):
        start_time = time.perf_counter()
        A_sorted = merge_sort(arr)
        end_time = time.perf_counter()
        average_time += (end_time - start_time)
    
    avg_final = average_time / 10
    execution_times.append(avg_final)
    print(f"Закончен подсчёт сортировки последовательности длиной: {len(arr)}\t{avg_final:.6f} сек.")


plt.style.use('dark_background')
plt.figure(figsize=(8, 6))
plt.plot(sizes, execution_times, marker='o', color='#7fff7f', linewidth=2)
plt.title('Сортировка Слиянием (Merge Sort)')
plt.xlabel('Размер данных (N)')
plt.ylabel('Время выполнения (T, сек)')
plt.grid(True, linestyle='--', alpha=0.5)


filename = 'merge_sort_graph.png'
plt.savefig(filename)
print(f"\nГрафик сохранен в файл: {filename}")