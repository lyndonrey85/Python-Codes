from flask import Flask render_template, redirect, request, session

app = Flask(__name__)

@app.route('/')
def counter()
    if 'counting' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
        
app.run(debug=True)
