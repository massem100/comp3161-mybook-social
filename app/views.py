"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from flask_mysqldb import MySQL
from app import app, login_manager
from datetime import datetime
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_login import login_user, logout_user, current_user, login_required
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from app.forms import LoginForm
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash


mysql = MySQL(app)

###
# Routing for your application.
###

# Please create all new routes and view functions above this route.
# This route is now our catch all route for our VueJS single page
# application.
@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    # error = None
    # if request.method == 'POST':
        # if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
        #     error = 'Invalid username or password'
        # else:
        #     session['logged_in'] = True

    #         # flash('You were logged in', 'success')
    #         return redirect(url_for('dashboard'))
    # return render_template('login.html', error=error)
    
    return render_template('login.html')

@app.route('/signup')
def register(): 

    return render_template('signup.html')

@app.route('/dashboard')

def dashboard():

    return render_template('dashboard.html')

@app.route('/userprofile')
@login_required
def userprofile():

    return render_template('user_profile.html')



@app.route('/friends')
@login_required
def showfriends():

    return render_template('friends.html')




@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', 'success')
    return redirect(url_for('home'))
"""
# cur = mysql.connection.cursor()
    # cur.execute('''SELECT * FROM customer''')
    # rv = cur.fetchall()

    # mysql.close()
   

"""
@login_manager.user_loader
def load_user(id):
    return '1'

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
