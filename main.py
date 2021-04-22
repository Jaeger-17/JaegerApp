from flask import Flask, render_template, request
from BodyMassIndex import BodyMassIndex
from RetirementSavings import RetirementSavings

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/BMI", methods=["POST", "GET"])
def BMI():
    if request.method == 'POST':
        # Get data from form input
        feet = request.form['feet']
        inches = request.form['inches']
        weight = request.form['weight']
        # Put data into BodyMassIndex object
        userBmi = BodyMassIndex(feet, inches, weight)

        # Call calculation function
        result = userBmi.calculate_BMI()
        return render_template("BMI.html", result=result)
    else:
        return render_template("BMI.html")


@app.route("/retire", methods=["POST", "GET"])
def retire():
    if request.method == 'POST':
        # Get data from form input
        age = request.form['age']
        salary = request.form['salary']
        percent = request.form['percent']
        goal = request.form['goal']
        # Put data into RetirementSavings object
        userRetirement = RetirementSavings(age, salary, percent, goal)
        # Call calculation function
        resultRetire = userRetirement.calculate_goal_age()
        return render_template("Retire.html", resultRetire=resultRetire)
    else:
        return render_template("Retire.html")


'''
@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template()

app.route("/<usr>")
def user(usr):
    return render_template()


@app.route("/<name>")
def user(name):
    return f"Hello, {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))
'''

if __name__ == "__main__":
    app.run(debug=True)
