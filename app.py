from flask import Flask 
x = Flask(__name__)
@x.route('/')
def home():
    return '<h1> This is my web page</h1>'
@x.route('/users')
def userspage():
    return 'This is the user page'
@x.route('/Aboutus')
def aboutus():
    return 'This is a About us page'

if __name__ == '__main__':
    x.run(port=6969)