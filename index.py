from flask import Flask, render_template
from scripts.main import mass_query_first, mass_query_sod, mass_query_all

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html', mass=mass_query_all)

@app.route('/task/<int:number_task>')
def show_table(number_task):
    mass_query = []

    if number_task == 1:
        mass_query = mass_query_first
    else:
        mass_query = mass_query_sod

    return render_template('table.html', mass=mass_query, task_number=number_task)



