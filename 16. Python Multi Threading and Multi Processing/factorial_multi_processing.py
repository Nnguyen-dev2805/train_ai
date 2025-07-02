# tính giai thừa với những số lớn thì cần multi-processing để tăng tốc độ tính toán

import multiprocessing
import time
import math
import sys

# increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000) # cho phép chuyển đổi chuỗi thành số nguyên với số chữ số lớn hơn

## function to calculate factorial

def compute_factorial(n):
    """Compute the factorial of a number."""
    print(f"Calculating factorial of {n}...")
    time.sleep(1)  # Simulate a time-consuming calculation
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result

if __name__ == "__main__":
    # List of numbers to compute factorial
    numbers = [1000, 2000, 3000, 4000, 5000]

    # Create a pool of workers
    with multiprocessing.Pool() as pool:
        # Map the compute_factorial function to the list of numbers
        results = pool.map(compute_factorial, numbers)

    print("All factorials computed.")
    print(results)