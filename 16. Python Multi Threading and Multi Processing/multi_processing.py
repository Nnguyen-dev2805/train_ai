## Multiprocessing

## Khi nào nên sử dụng multiprocessing?
## CPU-bound: Công việc nặng về tính toán, cần nhiều CPU để xử lý nhanh chóng, không có nhiều thao tác chờ I/O
## Khi cần tận dụng tối đa CPU, chạy song song nhiều tác vụ nặng

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)  # giả sử thời gian tính toán
        print(f"Square: {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)  # giả sử thời gian tính toán
        print(f"Cube: {i * i * i}")

if __name__ == '__main__':
    # Kiểm tra xem có phải đang chạy trong môi trường chính hay không
    # Nếu không có dòng này, sẽ gặp lỗi khi chạy trên Windows vì multiprocessing cần biết điểm bắt đầu
    # của tiến trình mới để tránh tạo ra vô số tiến trình con
    
    ## create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()
    # start the processes
    p1.start()
    p2.start()
    # wait for both processes to finish
    p1.join()  # main process sẽ chờ cho p1,p2 kết thúc rồi mới thực hiện tiếp
    p2.join()
    finished_time = time.time() - t
    print(finished_time)
    # Note: Multiprocessing sẽ tạo ra các tiến trình con độc lập, mỗi tiến trình có bộ nhớ riêng, không chia sẻ dữ liệu trực tiếp như threading