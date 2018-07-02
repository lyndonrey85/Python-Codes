from flask import Flask, render_template, request, redirect, flash, session
import re

app = Flask(__name__)
# bcrypt = Bcrypt(app)
app.secret_key = "mysecretkey"

mysql = MySQLConnector(app, 'the_wall')

def validate(email, first_name, last_name, password):
    if email and not email_regex.match(request.form['email']):
        flash("Invalid Email Address!")
    if first_name and not name_regex.match(request.form['first_name']):
        flash("Invalid first name")
    if last_name and not name_regex.match(request.form['last_name']):
        flash("Invalid last name")
    if password and len(password) < 6:
        flash("Password must be over 6 characters")

# @app.route('/')
# def index():
#     if 'user' in session:
#         return redirect('/wall')
#     else:
#         return render_template('/index.html')

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/wall')
    else:
        return render_template('/index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form['email'] and request.form['pw']:
        query = "SELECT * FROM users WHERE email=:email"
        data = {
            'email': request.form['email']
        }
    if len(mysql.query_db(query, data)) > 0:
        user = mysql.query_db(query, data)[0]
        print("user: {}".format(user))
    
    session['user'] = user
    flash("Log in Successful")
    return redirect('/wall')
    flash("Incorrect username or password")
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logged_out():
    session.pop('user', None)
    return redirect('/')

# @app.route('/logout', methods=['POST]')
# def logged_out():
#     session.pop('user', None)
#     return redirect('/')

@app.route('/register', methods=['POST'])
def registration():
    errors = 0
    query = "SELECT email FROM users WHERE email=:email"
    data = {
        'email': request.form['email']
    }
    registered_users = mysql.query_db(query, data)
    print(registered_users)
    if registered_users:
        errors += 1
        flash("Email has already been used")
    if not request.form['email']:
        errors += 1
        flash("Please add an email")
    if not name_regex.match(request.form['first_name']) or not name_regex.match(request.form['last_name']):
        errors += 1
        flash("Invalid first or last name")
    if not email_regex.match(request.form['email']):
        errors += 1
        flash("Invalid Email Address!")
    if len(request.form['pw']) < 6:
        errors += 1
        flash("Password must be greater than 6 characters")
    if request.form['pw'] != request.form['pw_confirmation']:
        errors += 1
        flash("Password must match password confirmation")
    if errors == 0:
        flash("New user successfully registered")
        pw_hash = bcrypt.generate_password_hash(request.form['pw'])
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, Now(), Now());"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'pw_hash': pw_hash
        }
        mysql.query_db(query, data)
        query = "SELECT * FROM users WHERE email=:email AND first_name=:first_name AND last_name=:last_name"
        user = mysql.query_db(query, data)[0]
        session['user'] = user
        return redirect('/wall')
    return redirect('/')

@app.route('/wall')
def wall():
    print(session['user'])
    if 'user' in session:
        query = "SELECT first_name, last_name, message_text, DATE_FORMAT(messages.created_at, '%M %D %Y %H:%i') AS created_at, messages.id, user_id FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
        message_list = mysql.query_db(query)
        query = "SELECT first_name, last_name, comment_text, DATE_FORMAT(comments.created_at, '%M %D %Y %H:%i') AS created_at, message_id FROM comments JOIN users ON comments.user_id = users.id ORDER BY comments.created_at"
        comment_list = mysql.query_db(query)
        return render_template('/wall.html', message_list = message_list, comment_list = comment_list)
    else:
        flash("You are not logged in")
        return redirect('/')

# @app.route('/wall')
# def wall():
#     print(session['user'])
#     if 'user' in session:
#         query = "SELECT first_name, last_name, message_text, DATE_FORMAT(messages.created_at, '%M %D %Y %H:%i') AS created_at, messages.id, user_id FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
# adding message page
@app.route('/wall/message', methods=['POST'])
def add_message():
    message_text = request.form['message']
    query = "INSERT INTO messages (message_text, created_at, updated_at, user_id) VALUES (:message_text, Now(), Now(), :user_id)"
    data = {
        'message_text': message_text,
        'user_id': session['user']['id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')
# putting in comments
@app.route('/wall/comment/<message_id>', methods=['POST'])
def add_comment(message_id):
    query = "INSERT INTO comments (comment_text, created_at, updated_at, user_id, message_id) VALUES (:comment_text, Now(), Now(), :user_id, :message_id)"
    data = {
        'comment_text': request.form['comment'],
        'user_id': session['user']['id'],
        'message_id': message_id
    }
    mysql.query_db(query, data)
    return redirect('/wall')
# deleting comments
# @app.route('/wall/message/delete/<id>')
# def delete_comment(id):
#     del_comments_query = "DELETE FROM comments WHERE message_id = :id"
#     data = {
#         'id': id
#     }
#     mysql.query_db(del_comments_query, data)
#     del_message_query = "DELETE FROM messages WHERE id = :id"
#     mysql.query_db(del_message_query, data)
#     return redirect('/wall')

@app.route('/wall/message/delete/<id>')
def delete_comment(id):
    del_comments_query = "DELETE FROM comments Where message_id = :id"
    data = {
        'id' : id
    }
    mysql.query_db(del_message_query, data)
    del_message_query = "DELETE FROM messages Where id = :id"
    mysql.query_db(del_message_query, data)
    return redirect('/wall')

app.run(debug=True)