from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index1.html')

@app.route('/ninjas')

def ninjas():
    return render_template('index2.html')

@app.route('/dojo')

def dojo():
    return render_template('index3.html')
app.run(debug = True)