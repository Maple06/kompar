import time

N = 5_000_000
data = range(1, N + 1)
total = 0

start_time = time.perf_counter_ns()

for i in data:
    total += i * i

print("Total sum:", total)
print("Time taken:", time.perf_counter_ns() - start_time, "nanoseconds")