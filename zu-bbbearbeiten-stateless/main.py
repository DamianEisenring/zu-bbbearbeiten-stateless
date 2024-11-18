import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    todos = helper.get_all()  # Hier den Namen der Variablen angepasst
    return render_template('index.html', todos=todos)  # Auch hier den Namen der übergebenen Variablen angepasst

@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("title")  # 'text' durch 'title' ersetzt
    helper.add(title)
    return redirect(url_for("index"))

@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))
