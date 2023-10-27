from flask import Flask
from flask import render_template
from forca import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/outra-rota')
def outro_hello_world():
    return 'Outro hello!'

if __name__ == '__main__':
    app.run(debug=True)