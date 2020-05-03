"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from flask_mysqldb import MySQL
from app import app
from datetime import datetime
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask import Flask,render_template, request, jsonify, redirect, url_for, flash, session
from app.forms import UploadForm, LoginForm, SignupForm, PhotoForm
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash

# Initializing the SQL connection to our app.
mysql = MySQL(app)

@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')

@app.route('/userprofile', methods = ['POST','GET'])
def userprofile():
    form = PhotoForm()
    
    # cur = mysql.connection.cursor()
    # cur.execute('SELECT * FROM customer WHERE customer_id ="CUS-00001" ')
    # customer = cur.fetchall()
    # cur.close()
    return render_template('user_profile.html',form = form)
    
@app.route('/groups')
def groups():

    return render_template('groups.html')

@app.route('/searchgroup', methods = ['GET'])
def searchgroup(): 
    
    # cur = mysql.connection.cursor()
    # cur.execute('SELECT * FROM customer WHERE customer_id ="CUS-00001" ')
    # customer = cur.fetchall()
    # cur.close()
    return render_template('create_group.html')


@app.route('/friends')
def friends():

    return render_template('friends.html')


@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    """ 
    waiting to setup when database has been added
    Fetch data from database to validate login 

    add request.method = 'POST in form.validate_on_submit if statement
    
    """
    if request.method == 'POST' and form.validate_on_submit():
        form.username.data
        form.password.data
        
        # cur = mysql.connection.cursor()
        # cur.execute('INSERT INTO user VALUES (')
        # rv = cur.fetchall()

        return redirect(url_for('dashboard'))
    else:

        return render_template('login.html', form = form)
    if request.method =='GET':
        
        return render_template('login.html')


@app.route('/signup', methods = ['POST','GET'])
def signup():
    form = SignupForm()
    # print('YOU REACH YASUH?')
    if request.method == 'POST' and form.validate():
        # print('passing threshold')
        if form.validate_on_submit():
            # print('DEH YAH YUTE')   
            num = 0 
            num += 6
            # userid = "user-" +"{}".format(num + 1)
            username = form.username.data
            first_name = form.f_name.data
            last_name = form.l_name.data 
            gender = form.gender.data
            date_of_birth = form.birthday.data
            user_password = generate_password_hash(form.password.data)
            confirm_password = check_password_hash(user_password, form.password.data)
            # print(confirm_password)
            # print('DATA READ')
            """
            1. write if statement that if corfirm_password returns false.. raise error.. Passwords dont match!
            2. Setup actual userid to work and increment properly

            """
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s, %s)''', ("user-" + "{}".format(num),
                        username, first_name, last_name, gender, date_of_birth, user_password))

            data = cur.fetchall()
            mysql.connection.commit()
            cur.close()

            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        return render_template('signup.html', form = form)
    else:
        # print( 'NOT REACHING POST')
        # Remember to setup error display messages
        return render_template('signup.html', form = form)
    
    
    


###
# Routing for your application.
###

# Please create all new routes and view functions above this route.
# This route is now our catch all route for our VueJS single page
# application.


"""
#This is how we will connect to the SQL server and make queries to the database in FLask.
cur = mysql.connection.cursor()
cur.execute('''SELECT * FROM customer''')
rv = cur.fetchall()

mysql.close()
"""




# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
