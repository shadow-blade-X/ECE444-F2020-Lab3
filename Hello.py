from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

appJX = Flask(__name__)
bootstrap = Bootstrap(appJX)
moment = Moment(appJX)

@appJX.route('/')
def index():
 return render_template('index.html', current_time=datetime.utcnow())

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
