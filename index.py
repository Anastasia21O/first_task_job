from flask import Flask, render_template, request
from scripts.main import task_first, task_second, select_all, delete_user, add_user, update_user, select_user, numeration

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html', mass=select_all(), numeration=numeration())

@app.route('/task/<int:number_task>')
def show_table(number_task):
    mass_query = []

    if number_task == 1:
        mass_query = task_first()
    else:
        mass_query = task_second()

    return render_template('table.html', mass=mass_query, task_number=number_task)

@app.route('/add', methods=['GET'])
def user_add():
    return render_template('add.html')

@app.route('/add', methods=['POST'])
def user_add_save():
    user = [request.form['name'], request.form['sorname'], request.form['age'], request.form['phone'], request.form['salary']]
    add_user(user)
    return render_template('index.html', mass=select_all())

@app.route('/update/<int:user_id>', methods=['GET'])
def user_update(user_id):
    user = select_user(user_id)
    return render_template('update.html', user=user)

@app.route('/update/<int:user_id>', methods=['POST'])
def user_update_save(user_id):
    user = [request.form['name'], request.form['sorname'], request.form['age'], request.form['phone'],
            request.form['salary']]
    update_user(user, user_id)
    return render_template('index.html', mass=select_all())

@app.route('/delete/<int:user_id>')
def user_delete(user_id):
    delete_user(user_id)
    return render_template('index.html', mass=select_all())



