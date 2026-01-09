from flask import Flask, render_template, request

app = Flask(__name__)

# 入力ページ
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# 結果ページ（POST専用）
@app.route("/result", methods=["POST"])
def result():
    name = request.form["username"]

    # 🔴 空チェック
    if name == "":
        error = "名前を入力してください"
        return render_template("index.html", error=error)

    # 🟢 正常なら結果ページへ
    return render_template("result.html", name=name)

@app.route("/hello")
def hello():
    return "HELLO 123"

if __name__ == "__main__":
    app.run(debug=True)
