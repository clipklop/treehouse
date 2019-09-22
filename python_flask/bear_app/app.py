"""
    * App to name your Bear, huh?
"""
from options import DEFAULTS
from flask import (
    Flask, render_template, redirect, url_for, request, make_response, flash)
import json


app = Flask(__name__)
app.secret_key = 'sdjoskj@sadjkfoskdokasdo.sdr5%$@!@#$%kfdo4trololo'


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    return render_template(
        'index.html',
        saves=get_saved_data()
    )


@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_saved_data(),
        options=DEFAULTS
    )


@app.route('/save', methods=['POST'])
def save():
    # import pdb; pdb.set_trace()
    # would let you trace the form data with request.form
    flash('Nice! You look fantastic!')
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response


app.run(debug=True)
