from flask import Flask
from flask import render_template
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/calc",methods=['POST'])
def calc():
    expression = request.form["expression"]
    calculation_result = eval(expression) # This should be secure, right?
    return render_template('result.html',result=calculation_result)
