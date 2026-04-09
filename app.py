from flask import Flask, render_template

app = Flask(__name__)


@app.route("/talabalar")
def talabalar_view():
    talabalar = ["Zafar", "Malika", "Ali", "Gulnora", "Bekzod"]
    return render_template("talabalar.html",
        data=sorted(talabalar),
        son=len(talabalar))



if __name__ == '__main__':
    app.run(debug=True)
