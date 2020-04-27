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
from flask import Flask,render_template, request, jsonify, redirect, url_for, flash
from app.forms import UploadForm, LoginForm, SignupForm
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash

# Initializing the SQL connection to our app.
mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods = ['POST', 'GET'])
def login(): 
    form = LoginForm()

    """ 
    waiting to setup when database has been added
    
    """
    if form.validate_on_submit():

        return redirect(url_for('dashboard'))
    
    form.email.data
    form.password.data


    return render_template('login.html', form = form)

@app.route('/signup')
def signup():

    form = SignupForm()
    if form.validate_on_submit():

        # flash('Sign Up Successful', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', form = form)


@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')

@app.route('/userprofile')
def userprofile():

    return render_template('user_profile.html')


@app.route('/groups')
def groups():

    return render_template('groups.html')


@app.route('/friends')
def friends():

    return render_template('friends.html')



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
e
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
