from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def no_ninjas():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    x = url_for('static', filename='tmnt.png')
    return render_template('index2.html', filename='tmnt.png', urlstr = x)

   

@app.route('/ninja/<color>')
def ninjacolor(color):

    if color == 'blue':
         x=url_for('static', filename='leonardo.jpg')
    elif color == 'orange':
         x=url_for('static', filename='michelangelo.jpg')
    elif color == 'red':
         x=url_for('static', filename='raphael.jpg')
    elif color == 'purple':
         x=url_for('static', filename='donatello.jpg')
    else:
         x=url_for('static', filename='notapril.jpg')

    return render_template('index2.html', urlstr = x)
    # do not hardcode


app.run(debug=True)