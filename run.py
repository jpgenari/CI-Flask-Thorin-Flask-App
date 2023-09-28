import os
from flask import Flask # importing Flask class from flask


app = Flask(__name__) # creates an instance and store in the variable app, first argument __name__ is the name of application module, single name uses double underscore


@app.route("/") # decorator, starts with @ , wraps the function
def index():
    return "Hello, World"

if __name__ == "__main__": # __main__ wrapped in "" is the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True # should never be True for production projects or when submitting milestone project, it allows arbitrary code to run, security flaw, should be used only when developing
    )
