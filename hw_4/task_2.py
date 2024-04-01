import math
import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def calculate_integral(f, a, step, i):
    return f(a + i * step) * step


def integrate_interval(args):
    f, a, step, start, end = args
    return sum(calculate_integral(f, a, step, i) for i in range(start, end))


def integrate_function(f, a, b, *, n_jobs=1, n_iter=1000000, executor_type=ThreadPoolExecutor):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs

    args = [(f, a, step, i * chunk_size, min((i + 1) * chunk_size, n_iter)) for i in range(n_jobs)]

    with executor_type(max_workers=n_jobs) as executor:
        results = list(executor.map(integrate_interval, args))

    return sum(results)


if __name__ == '__main__':
    n_jobs = os.cpu_count() * 2

    for jobs in range(1, n_jobs + 1):
        start_time_threads = time.perf_counter()
        integrate_function(math.cos, 0, math.pi / 2, n_jobs=jobs, executor_type=ThreadPoolExecutor)
        end_time_threads = time.perf_counter()

        start_time_processes = time.perf_counter()
        integrate_function(math.cos, 0, math.pi / 2, n_jobs=jobs, executor_type=ProcessPoolExecutor)
        end_time_processes = time.perf_counter()

        res = f'Threads n_jobs: {jobs} time: {end_time_threads - start_time_threads}\n'
        res += f'Processes n_jobs: {jobs} time: {end_time_processes - start_time_processes}\n\n'

        with open('artifacts/task_2.txt', 'a') as f:
            f.write(res)