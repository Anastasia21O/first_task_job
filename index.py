from flask import Flask, render_template
from scripts.main import mass_query_first, mass_query_sod

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('proba.html', mass=mass_query_first)

@app.route('/hello')
def hello_world():
    return "<p>Hello, World!</p>"



app.run(debug=True)