## Multithreading 
## Khi nào nên dùng multithreading?

### CPU chờ I/O-bound: tức CPU nhãn rỗi trong khi chờ, nên bạn có thể dùng nhiều thread để thực hiện song song nhiều tác vụ I/O, tận dụng thời gian chờ
### Khi muốn chia sẻ dữ liệu dễ dàng giữa các tác vụ
### Khi cần xử lý nhiều tác vụ đồng thời mà không cần nhiều CPU 

import threading
import time

def print_numbers():
    for i in range(5): 
        time.sleep(2) # giả sử thời gian I/O
        print(f"Number: {i}")
        
def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letter: {letter}")

# create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t=time.time()
# start the threads
t1.start()
t2.start()

# wait for both threads to finish
t1.join()  # main thread sẽ chờ cho t1,t2 kết thúc rồi mới thực hiện tiếp 
t2.join()

finished_time = time.time() - t
print(finished_time)