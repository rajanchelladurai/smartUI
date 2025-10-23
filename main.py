import flask,requests
import os
from flask import render_template, url_for
from werkzeug.utils import redirect
from flask import request
app = flask.Flask(__name__)

@app.route('/')
def task():
    return render_template('task.html')


if __name__ =='__main__':
    app.run()

