from multiprocessing import Process, Queue
import time


def partial_calculation(start, end, queue):
    s = sum(i * i for i in range(start, end + 1))
    queue.put(s)

if __name__ == "__main__":
    q = Queue()

    N = 5_000_000
    num_processes = 4
    chunk_size = N // num_processes

    processes = []
    for pid in range(1, num_processes + 1):
        start = (pid - 1) * chunk_size + 1
        end = pid * chunk_size if pid < num_processes else N
        processes.append(Process(target=partial_calculation, args=(start, end, q)))

    start_time = time.perf_counter_ns()

    for p in processes:
        p.start()

    total = sum(q.get() for _ in range(num_processes))
    for p in processes:
        p.join()

    print("Processes: ", num_processes)
    print("Total sum:", total)
    print("Time taken:", time.perf_counter_ns() - start_time, "nanoseconds")