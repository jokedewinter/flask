from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)


@app.route("/")
def index():
    quotes = ["If people do not believe that mathematics is simple, it Neumann", "Computer science is no more about computers than astronomy", "To understand recursion you must first understand recursion", "You look at things that are and ask, why? I dream of things", "Mathematics is the key and door to the sciences. -- Galileo", "Not everyone will understand your journey. That's fine."]
    random_number = randint(0, len(quotes) - 1)
    quote = quotes[random_number]
    return render_template("index.html", title="home", **locals())


@app.route("/about")
def about():
    return render_template("about.html", title="about")


@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"]
    result="All OK"
    return render_template("confirmation.html", title="Form confirmation", **locals())


if __name__ == "__main__":
    app.run(debug=True)
