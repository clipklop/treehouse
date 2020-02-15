from flask import Flask, render_template


app = Flask(__name__)
name = 'Mischa'


@app.route('/')
@app.route('/<name>')
def home(name='Mischa'):
    # name = request.args.get('name', name)
    return render_template('index.html', name=name)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    context = {'num1': num1, 'num2': num2, 'total': num1+num2, 'name': name}
    return render_template('add.html', **context)


app.run(debug=True)
