# Flynn's Taxonomy

This folder demonstrates **Flynn’s Taxonomy** (SISD, SIMD, MISD, MIMD) using the same study case of computing the sum of squares.

All scripts were run with **N = 1,000,000** and produced the same result:

`Total sum = 333333833333500000`

## What each script represents

### SISD (Single Instruction, Single Data)
- One instruction stream executes over one data stream.
- Implementation here: a normal Python `for` loop accumulating `i*i`.

### SIMD (Single Instruction, Multiple Data)
- One instruction stream applies the same operation to multiple data elements at once.
- Implementation here: NumPy vectorization (`x*x` over a whole array).

### MISD (Multiple Instruction, Single Data)
- In theory: multiple instruction streams operate on the same data stream.
- Implementation here: two different “instruction streams” compute the same mathematical result:
	- a loop method, and
	- a closed-form formula $n(n+1)(2n+1)/6$,
	then we compare to verify correctness.
- Timing note: the loop still dominates (similar to SISD), so it’s not expected to be faster.

### MIMD (Multiple Instruction, Multiple Data)
- Multiple instruction streams operate on multiple data streams (true parallelism).
- Implementation here: split the range into chunks and use multiple processes.
- Why it can be slower here on Windows: process start-up (“spawn”), inter-process communication, scheduling, and Python-level overhead can outweigh the benefit unless the workload is large enough.

## Results (your runs)

Times are taken from the console outputs you provided.

| Flynn class | Script | N | Workers | Time (ns) | Time (ms) | Speedup vs SISD |
|---|---|---:|---:|---:|---:|---:|
| SISD | `sisd.py` | 1,000,000 | 1 | 53,022,700 | 53.02 | 1.00× |
| SIMD | `simd.py` | 1,000,000 | (vectorized) | 3,907,800 | 3.91 | 13.56× |
| MISD | `misd.py` | 1,000,000 | 2 threads | 51,342,700 | 51.34 | 1.03× |
| MIMD | `mimd.py` | 1,000,000 | 24 | 388,082,000 | 388.08 | 0.14× |

## Interpretation

- SIMD wins in this study case
- **MIMD is slower in this measurement** even with 24 workers because the job per worker is too small relative to overhead:
	- Windows process spawning is expensive,
	- work distribution and result collection add synchronization cost.

## Notes / fairness of the comparison

- These scripts are meant to illustrate the taxonomy concepts, not to be a perfect apples-to-apples benchmark.
- For more stable timing, run each case multiple times and report an average/median.
