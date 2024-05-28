from flask import Flask, request

app = Flask(__name__)

msg = 'Hello world!'
person = {'name': 'John', 'age': 21}

@app.route('/')
def home():
    return f'<h3>{msg}</h3>'

@app.route('/spam')
def spam():
    return person, 201

@app.route('/hello/<name>')
def hello(name):
    # name = (request.args.get('name'))
    return {'message': f'Hello, {name}!'}

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return {'result': a + b}

@app.errorhandler(Exception)
def value_error(error):
    return {'error': str(error)}, 400

@app.errorhandler(404)
def not_found(err):
    print(err)
    return {'ERROR': 'Not Found'}, 404

app.run(debug=True)