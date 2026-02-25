import sys
import time
from concurrent.futures import ThreadPoolExecutor

def parse_n(default: int = 1_000_000) -> int:
	if len(sys.argv) >= 2:
		return int(sys.argv[1])
	return default

def sum_squares_loop(n: int) -> int:
	total = 0
	for i in range(1, n + 1):
		total += i * i
	return total

def sum_squares_formula(n: int) -> int:
	# 1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6
	return n * (n + 1) * (2 * n + 1) // 6

def main() -> None:
	n = parse_n()

	start_time = time.perf_counter_ns()
	with ThreadPoolExecutor(max_workers=2) as executor:
		future_loop = executor.submit(sum_squares_loop, n)
		future_formula = executor.submit(sum_squares_formula, n)
		total_loop = future_loop.result()
		total_formula = future_formula.result()
	elapsed = time.perf_counter_ns() - start_time

	print("Flynn: MISD")
	print("N:", n)
	print("Total sum (loop):", total_loop)
	print("Total sum (formula):", total_formula)
	print("Match:", total_loop == total_formula)
	print("Time taken:", elapsed, "nanoseconds")

if __name__ == "__main__":
	main()