from flask import Flask, render_template, url_for
from pathlib import Path

current_directory = Path.cwd()

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to Python Flask! Love, Z"


home_path = str(current_directory / 'templates' / 'index.html')
@app.route('/home')
def home():
    url_for('static', filename='francisco.css')
    # # redirecting to the *same page*, but without parameters
    # from flask import redirect
    # import requests
    # return redirect(request.path, code=302)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
