import os
import json
from flask import Flask, render_template, request, flash # importing Flask class from flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__) # creates an instance and store in the variable app, first argument __name__ is the name of application module, single name uses double underscore
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/") # decorator, starts with @ , wraps the function
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__": # __main__ wrapped in "" is the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True # should never be True for production projects or when submitting milestone project, it allows arbitrary code to run, security flaw, should be used only when developing
    )
