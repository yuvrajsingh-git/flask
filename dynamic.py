from flask import Flask,render_template
dyn=Flask(__name__)

@dyn.route('/')
def index():
   return'This is a Home page'
@dyn.route('/user')
def user():
    return render_template('index.html')
@dyn.route('/user/<username>')
def nameinstance(username):
  return f'Welcome Back {username} Have a Good Day'

@dyn.route('/contact/<int:number>')
def displayNumber(number):
   return f'The conatct number is {number} Have a Bad Day'

if __name__ == '__main__':
    dyn.run(port= 86956)