import threading
import multiprocessing
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def sync(n):
    start_time = time.time()
    for _ in range(10):
        fibonacci(n)
    end_time = time.time()
    with open('artifacts/task_1.txt', 'a') as f:
        f.write(f"Sync time: {end_time - start_time} seconds\n")


def threads(n):
    start_time = time.time()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    with open('artifacts/task_1.txt', 'a') as f:
        f.write(f"Thread time: {end_time - start_time} seconds\n")


def processes(n):
    start_time = time.time()
    processes = []
    for _ in range(10):
        process = multiprocessing.Process(
            target=fibonacci, args=(n,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    with open('artifacts/task_1.txt', 'a') as f:
        f.write(f"Multiprocessing time: {end_time - start_time} seconds\n")


def main():
    n = 33
    threads(n)
    processes(n)
    sync(n)


if __name__ == "__main__":
    main()
