from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


from flask_wtf.csrf import CSRFProtect

# CSRF protection

csrf = CSRFProtect()

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)

import os

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

csrf.init_app(app)

bootstrap = Bootstrap(app)


# Routes


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

# return render_template('index.html', datetime = str(datetime.now()))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
