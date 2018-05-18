from flask import Flask
from flask import redirect
from flask import template_rendered
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return template_rendered('index.html')

@app.route('/user/<name>')
def user(name):
    return template_rendered('user.html',name=name)

if __name__ == '__main__':
    manager.run()
