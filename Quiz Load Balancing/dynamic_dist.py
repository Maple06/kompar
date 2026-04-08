import threading
import time
from collections import deque

# 1. SETUP: Defining the initial tasks
tasks_worker_1 = deque([2, 5, 8, 3, 6, 4]) # Heavy load
tasks_worker_2 = deque([1, 1, 2])          # Light load
all_queues = [tasks_worker_1, tasks_worker_2]

# --- CALCULATION OF EXPECTED OPTIMAL TIME ---
total_work = sum(tasks_worker_1) + sum(tasks_worker_2)
num_workers = len(all_queues)
# The "Ideal" time if everything is perfectly distributed
expected_optimal_time = total_work / num_workers 

print(f"Total Workload: {total_work}s")
print(f"Number of Workers: {num_workers}")
print(f"Expected Optimal Time (per worker): {expected_optimal_time}s")
print("-" * 40)

def execute_worker(worker_id, my_queue):
    start_time = time.time()
    print(f"Worker {worker_id} starting with {list(my_queue)} tasks.")
    
    while True:
        if my_queue:
            task_duration = my_queue.popleft()
            print(f"Worker {worker_id} executing task: {task_duration}s")
            # Simulation scale: 0.1s per 'task unit'
            time.sleep(task_duration * 0.1) 
        else:
            # DYNAMIC DISTRIBUTION: Work Stealing
            found_work = False
            for other_queue in all_queues:
                if len(other_queue) > 1:
                    stolen_task = other_queue.pop()
                    print(f"--- Worker {worker_id} stole task {stolen_task}s from peer! ---")
                    my_queue.append(stolen_task)
                    found_work = True
                    break
            
            if not found_work:
                break 

    end_time = time.time()
    actual_duration = (end_time - start_time) * 10 # Multiplying by 10 to reverse the 0.1 scale
    print(f"Worker {worker_id} finished. Actual runtime units: {actual_duration:.1f}s")

# Run workers
threads = [threading.Thread(target=execute_worker, args=(i, all_queues[i])) for i in range(2)]
for t in threads: t.start()
for t in threads: t.join()