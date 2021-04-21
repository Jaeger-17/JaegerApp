from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/BMI", methods=["POST", "GET"])
def BMI():
    return render_template("BMI.html")

@app.route("/retire")
def retire():
    return render_template("Retire.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template()

app.route("/<usr>")
def user(usr):
    return render_template()

'''
@app.route("/<name>")
def user(name):
    return f"Hello, {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))
'''

if __name__ == "__main__":
    app.run(debug=True)