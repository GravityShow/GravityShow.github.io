from flask import Flask, render_template


app = Flask(__name__)


@app.route("/<name>")
def hello_world(name=None):
    return render_template("index.html", user_name=name)

@app.route("/about")
def about():
    return render_template("about.html")