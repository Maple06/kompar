import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

def parse_args(default_n: int = 1_000_000, default_workers: int | None = None) -> tuple[int, int]:
	n = int(sys.argv[1]) if len(sys.argv) >= 2 else default_n
	if len(sys.argv) >= 3:
		workers = int(sys.argv[2])
	else:
		workers = default_workers or (os.cpu_count() or 2)
	return n, workers

def sum_squares_range(bounds: tuple[int, int]) -> int:
	start, end = bounds
	return sum(i * i for i in range(start, end + 1))

def chunk_ranges(n: int, workers: int) -> list[tuple[int, int]]:
	workers = max(1, workers)
	chunk_size = n // workers
	ranges: list[tuple[int, int]] = []
	for pid in range(workers):
		start = pid * chunk_size + 1
		end = (pid + 1) * chunk_size if pid < workers - 1 else n
		if start <= end:
			ranges.append((start, end))
	return ranges

def main() -> None:
	n, workers = parse_args()
	bounds = chunk_ranges(n, workers)

	start_time = time.perf_counter_ns()
	with ProcessPoolExecutor(max_workers=workers) as executor:
		total = sum(executor.map(sum_squares_range, bounds))
	elapsed = time.perf_counter_ns() - start_time

	print("Flynn: MIMD")
	print("N:", n)
	print("Workers:", workers)
	print("Total sum:", total)
	print("Time taken:", elapsed, "nanoseconds")

if __name__ == "__main__":
	main()