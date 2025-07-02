### Multithreading with ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
        time.sleep(1)  # giả sử thời gian I/O
        return f"Number: {number}"

numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)

for result in results:
    print(result)