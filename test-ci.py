import time
import matplotlib.pyplot as plt
from hybrid_sort import HybridSort
from generate_data import generate_data

sorter = HybridSort()
S = 50  # fix the threshold

datasets = generate_data(1000, 1000000, seed=42)

sizes = []
comparisons = []
times_taken = []

for data in datasets:
    size = len(data)
    sizes.append(size)

    start_time = time.time()
    sorter.sort(data, S)
    end_time = time.time()

    comparisons.append(sorter.comparison_count)
    times_taken.append(end_time - start_time)

    sorter.comparison_count = 0

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(sizes, comparisons, 'o-', label=f'S={S}')
plt.xlabel('Input size (n)')
plt.ylabel('Key Comparisons')
plt.title('Key Comparisons vs Input Size')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(sizes, times_taken, 'o-', label=f'S={S}')
plt.xlabel('Input size (n)')
# rescale plt.xscale('linear') or 'log'
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken vs Input Size')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


# CONCLUSIONS: from the empirical results, it seems the time complexity is linear
# but theoretically it should be around n*log(n)
