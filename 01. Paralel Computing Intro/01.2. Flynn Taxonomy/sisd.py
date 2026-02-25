import sys
import time

def parse_n(default: int = 1_000_000) -> int:
	if len(sys.argv) >= 2:
		return int(sys.argv[1])
	return default

def main() -> None:
	n = parse_n()

	start_time = time.perf_counter_ns()
	total = 0
	for i in range(1, n + 1):
		total += i * i
	elapsed = time.perf_counter_ns() - start_time

	print("Flynn: SISD")
	print("N:", n)
	print("Total sum:", total)
	print("Time taken:", elapsed, "nanoseconds")

if __name__ == "__main__":
	main()