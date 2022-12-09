from flask import Flask

app = Flask(__name__)


@app.route('/')
def show():
    return 'hi'


@app.route('/products')
def show_products():
    return 'products page'


if __name__ == '__main__':
    app.run(debug=True)
