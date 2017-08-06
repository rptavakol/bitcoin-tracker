from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import api_call as api

app = Flask(__name__)
bootstrap = Bootstrap(app)

if __name__ == "__main__":
    app.run()

@app.route('/no-ajax')
def no_ajax():
    return render_template("no_ajax.html", data=api.get_price(0))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/run')
def run():
    return api.get_price(1)