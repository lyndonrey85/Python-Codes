from flask import Flask,render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template('index.html')
    
# @app.route('/', methods=['POST'])
# def walrus():
#     return redirect('/')

@app.route('/result', methods=['POST'])
def result(name, last, city):
    print result
    name = request.form['name']
    last = request.form['last']
    city = request.form['city']
    result = request.form
    return render_template("index2.html", name="name",last="last", city="city")

app.run(debug=True)
