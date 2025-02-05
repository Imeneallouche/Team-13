from flask import Flask
from flask import render_template
from flask import request
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/post")
def get_image():
    writeup_path=request.args.get('path')
    return render_template('post.html',title=writeup_path,content=open(os.path.join(os.getcwd(),'posts',writeup_path)).read())