import time
import matplotlib.pyplot as plt
from hybrid_sort import HybridSort
from generate_data import generate_data

sorter = HybridSort()

fixed_size = 10000
data = generate_data(fixed_size, fixed_size, seed=42)[0]

S_values = list(range(1, 10000, 500))
comparisons = []
times_taken = []

for S in S_values:
    start_time = time.time()
    sorter.sort(data, S)
    end_time = time.time()

    comparisons.append(sorter.comparison_count)
    times_taken.append(end_time - start_time)

    sorter.comparison_count = 0

plt.figure(figsize=(10, 5))

# Plotting comparisons
plt.subplot(1, 2, 1)
plt.plot(S_values, comparisons, 'o-', label=f'n={fixed_size}')
plt.xlabel('Threshold value (S)')
plt.ylabel('Key Comparisons')
plt.title('Key Comparisons vs Threshold Value (S)')
plt.legend()
plt.grid(True)

# Plotting time taken
plt.subplot(1, 2, 2)
plt.plot(S_values, times_taken, 'o-', label=f'n={fixed_size}')
plt.xlabel('Threshold value (S)')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken vs Threshold Value (S)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
