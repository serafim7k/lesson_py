from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def get_start():
    return render_template('index.html')


@app.route('/from')
def my_site():
    return render_template('from_index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)
