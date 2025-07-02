from flask import Flask, render_template,request

# nó tạo ra một thể hiện của class Flask
# nó là ứng dụng WSGI (Web Server Gateway Interface) 

app = Flask(__name__)

@app.route('/') # nếu người dùng truy cập vào đường dẫn gốc của ứng dụng thì nó sẽ gọi hàm ngay dưới nó là welcome
def welcome():
    return 'Welcome to Flask!'

@app.route('/index') # nếu người dùng truy cập vào đường dẫn /index thì nó sẽ gọi hàm index
def hello():
    return render_template('index.html')

@app.route('/form',methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True) # chạy ứng dụng Flask với chế độ debug, giúp hiển thị lỗi và tự động tải lại ứng dụng khi có thay đổi