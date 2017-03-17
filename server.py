from flask import Flask, url_for, render_template
from flask_login import login_required, current_user
import jinja2
import json
import os


app = Flask(__name__, template_folder='./page')

@app.route("/user/<username>")
def show_user(username):
  return "user %s" % username

@app.route('/about/')
def about():
  return render_handle('about')

def render_handle(pathname):
  print('render' + pathname)
  return render_template(pathname + '.jinja2')

if __name__ == "__main__":
  app.run('127.0.0.1', 7777)