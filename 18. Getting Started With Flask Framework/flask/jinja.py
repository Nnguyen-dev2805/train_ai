### Building URL dynamically
### Variable rule
### Jinja 2 template engine

## Jinja 2 template engine
"""

{{ }}: expressions to print output in html
{% %}: conditions, for loops, etc.
{# #}: comments
"""

from flask import Flask, render_template, request

# nó tạo ra một thể hiện của class Flask
# nó là ứng dụng WSGI (Web Server Gateway Interface)

app = Flask(__name__)


@app.route(
    "/"
)  # nếu người dùng truy cập vào đường dẫn gốc của ứng dụng thì nó sẽ gọi hàm ngay dưới nó là welcome
def welcome():
    return "Welcome to Flask!"


@app.route(
    "/index"
)  # nếu người dùng truy cập vào đường dẫn /index thì nó sẽ gọi hàm index
def hello():
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("form.html")


## Variable rule
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {"score": score, "result": res}

    return render_template("result1.html", result=exp)


if __name__ == "__main__":
    app.run(
        debug=True
    )  # chạy ứng dụng Flask với chế độ debug, giúp hiển thị lỗi và tự động tải lại ứng dụng khi có thay đổi
