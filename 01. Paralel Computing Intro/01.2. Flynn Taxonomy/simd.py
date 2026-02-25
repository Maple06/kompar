import sys
import time


def parse_n(default: int = 1_000_000) -> int:
	if len(sys.argv) >= 2:
		return int(sys.argv[1])
	return default


def main() -> None:
	n = parse_n()

	try:
		import numpy as np
	except ModuleNotFoundError:
		print("Flynn: SIMD")
		print("N:", n)
		print("Error: numpy is required for the SIMD/vectorized example.")
		print("Install with: pip install numpy")
		raise

	start_time = time.perf_counter_ns()
	x = np.arange(1, n + 1, dtype=np.int64)
	total = int(np.sum(x * x, dtype=np.int64))
	elapsed = time.perf_counter_ns() - start_time

	print("Flynn: SIMD")
	print("N:", n)
	print("Total sum:", total)
	print("Time taken:", elapsed, "nanoseconds")


if __name__ == "__main__":
	main()

