from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm as Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Regexp,Email
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'new hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField("What is your name?", validators=[DataRequired()])
    email = StringField("What is your UofT email address?", validators=[DataRequired(),Email(granular_message=True)])
    submit = SubmitField('Submit')

def update(form, fields):
    for field in fields:
        old_field = session.get(field)
        if old_field is not None and old_field != form[field].data:
            flash(f'Looks like you have changed your {field}!')
        session[field] = form[field].data

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    email = None
    form = NameForm()
    if form.validate_on_submit():
        update(form,['name','email'])
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)
