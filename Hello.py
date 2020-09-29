from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
import re
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email

appJX = Flask(__name__)
moment = Moment(appJX)
bootstrap = Bootstrap(appJX)
appJX.config['SECRET_KEY'] = 'hard to'

class NameForm(Form):
 name = StringField('What is your name?', validators=[Required()])
 emailAdd = StringField('What is your UofT Email address?', validators=[Required()], render_kw={'type':'email'})
 submit = SubmitField('Submit')


@appJX.route('/', methods=['GET', 'POST'])
def index():
 form = NameForm()
 if form.validate_on_submit():

  old_name = session.get('name')
  if old_name is not None and old_name != form.name.data:
   flash('Looks like you have changed your name!')
  session['name'] = form.name.data

  old_emailAdd = session.get('emailAdd')
  if old_emailAdd is not None and old_emailAdd != form.emailAdd.data:
   flash('Looks like you have changed your email!')
  session['emailAdd'] = form.emailAdd.data

  if not re.fullmatch(r".*@mail.utoronto.ca", session.get('emailAdd')):
   session['uoftMailWarning']= "123"
  else:
   session['uoftMailWarning']= None
  return redirect(url_for('index'))
 return render_template('index.html', form = form, name = session.get('name'), emailAdd=session.get('emailAdd'), uoftMailWarning=session.get('uoftMailWarning'))

@appJX.route('/user/<name>')
def user(name):
 return render_template('user.html', name=name, current_time=datetime.utcnow())

@appJX.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

@appJX.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500

if __name__ == '__main__':
 appJX.run(debug=True)
