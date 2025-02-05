from flask import Flask
from flask import render_template
from flask import request
import subprocess

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/calc",methods=['POST'])
def calc():
    expression = request.form["expression"]
    # Friendship ended with python, bash is my new best friend. Let's see if you can get through this
    calculation_result= subprocess.Popen(f"echo {expression} | bc",stdout=-1,stderr=subprocess.STDOUT,shell=True).communicate()[0].decode()
    return render_template('result.html',result=calculation_result)