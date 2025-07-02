from flask import Flask

# nó tạo ra một thể hiện của class Flask
# nó là ứng dụng WSGI (Web Server Gateway Interface) 

app = Flask(__name__)

@app.route('/') # nếu người dùng truy cập vào đường dẫn gốc của ứng dụng thì nó sẽ gọi hàm ngay dưới nó là welcome
def welcome():
    return 'Welcome to Flask!'

@app.route('/hello') # nếu người dùng truy cập vào đường dẫn /hello thì nó sẽ gọi hàm hello
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True) # chạy ứng dụng Flask với chế độ debug, giúp hiển thị lỗi và tự động tải lại ứng dụng khi có thay đổi