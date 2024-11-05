# app.py

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify(message=f"Hello, {name}! Welcome to our site.")

if __name__ == "__main__":
    app.run(debug=True)
