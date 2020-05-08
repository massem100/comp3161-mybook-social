"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from datetime import date, time, datetime
from app import app, login_manager, mysql
from app.forms import UploadForm, LoginForm, SignupForm, PhotoForm, textForm, ImageForm, SearchFriends, SearchGroups
from app.models import User
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask import Flask,render_template, request, jsonify, redirect, url_for, flash, session
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash


"""
#This is how we will connect to the SQL server and make queries to the database in FLask.
cur = mysql.connection.cursor()
cur.execute('''SELECT * FROM customer''')
rv = cur.fetchall()

mysql.close()
"""


@app.route('/dashboard', methods = ['POST', 'GET'])
@login_required
def dashboard():

    text_form = textForm()
    image_form = ImageForm()

    # print(current_user.id)
    if request.method =='POST':
        if text_form.validate_on_submit():

            worded_post = text_form.text_post.data 
            # use statements below with implemented functions to format the time before storing on the database
            userid = current_user.id
            post_date = format_date_joined(datetime.now())
            post_time = format_time_joined(datetime.now())


           
            cur = mysql.connection.cursor()
            cur.execute(""" INSERT INTO post (post_id, userid, post_date, post_time) 
                        VALUES (NULL, "{}", "{}", "{}") """.format(userid,post_date,post_time))
            
            cur.execute(""" INSERT INTO text_post (text_id, post_id, text_message) 
                    VALUES (NULL, (SELECT max(post_id) FROM post WHERE userid = '{}'), "{}") """.format(userid, worded_post))
         
            mysql.connection.commit()
            cur.close()
            
            flash('Post created!', 'success')
            return render_template('dashboard.html', text_form = text_form, image_form = image_form)
           

        return render_template('dashboard.html', text_form = text_form, image_form = image_form)
            
    else: 
            
        return render_template('dashboard.html', text_form=text_form, image_form=image_form)
    

        """
        validate form and set up if statements to get data into tables.

        Need to setup in such a way to fill posts table too.. to set userid = call on current_user
        get current date and time and format it and generate post id.
        """

    return render_template('dashboard.html', text_form = text_form, image_form = image_form)



@app.route('/userprofile', methods = ['POST','GET'])
@login_required
def userprofile():
    form = PhotoForm()
    text_form = textForm()
    image_form = ImageForm()
    
   
    return render_template('user_profile.html',form = form, text_form = text_form, image_form = image_form)
    
@app.route('/groups', methods = ['GET', 'POST'])
def groups():

    return render_template('groups.html')

# Route to host form to search group
@app.route('/searchgroup', methods = ['GET'])
def searchgroup(): 
    groupform = SearchGroups()
    # cur = mysql.connection.cursor()
    # cur.execute('SELECT * FROM customer WHERE customer_id ="CUS-00001" ')
    # customer = cur.fetchall()
    # cur.close()
    return render_template('search_group.html', form= groupform)

# Route to display the active group 
@app.route('/groups/<group_id>', methods =['POST'])
def viewGroup():
    
    return 'route to display group'

@app.route('/friends', methods = ['POST', 'GET'])
def friends():
    form = SearchFriends()
    if request.method =='POST': 

        return 'x'
    return render_template('friends.html', form = form)


@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        flash('You are already logged in, logout to reach login page', 'info')
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST' and form.validate_on_submit():
        
        username = form.username.data
        # print(username)
        password = form.password.data
        
        # using your model, query database for a user based on the username
        # and password submitted. Remember you need to compare the password hash.
        # You will need to import the appropriate function to do so.
        # Then store the result of that query to a `user` variable so it can be
        # passed to the login_user() method below.
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM user WHERE username = "{}" '''.format(username))
        user = cur.fetchall()
        # print(user)
        if user is not None: 
            id= user[0][0]
            username_  = user[0][1]
            f_name = user[0][2]
            l_name = user[0][3]
            gender = user[0][4]
            dob = user[0][5]
            user_password_hash = user[0][6]
        # print(username, user_password_hash)
        
        if user is not None and check_password_hash(user_password_hash, password):
            remember_me = False
            # print ('pass here')
            
            login_user(User(id,username_,f_name, l_name, gender, dob, user_password_hash))
            
            print('reaching here')
            return redirect(url_for('dashboard'))
        else: 
            flash('Password not a match', 'danger')
            return render_template('login.html', form= form)
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
            
            cur.execute('''INSERT INTO user (userid,username, f_name, l_name, gender, date_of_birth, user_password) VALUES (NULL, %s, %s, %s, %s, %s, %s)''',
            (username, first_name, last_name, gender, date_of_birth, user_password))

            data = cur.fetchall()
            mysql.connection.commit()
            cur.close()

            flash('Congratulations, you are now a registered user!', 'success')
            return redirect(url_for('login'))
        return render_template('signup.html', form = form)
    else:
        # print( 'NOT REACHING POST')
        # Remember to setup error display messages
        return render_template('signup.html', form = form)

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    # print(type(id))
    # userid = str(id)
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM user WHERE userid = "{}"'''.format(id))
    user = cur.fetchall()
    # print (user)
    if user > ():
        id = user[0][0]
        username_ = user[0][1]
        f_name = user[0][2]
        l_name = user[0][3]
        gender = user[0][4]
        dob = user[0][5]
        user_password_hash = user[0][6]
        # print('this a print' + user)
        # print(id)
        # print(username_)
        # print(user)
        result = User(id, username_, f_name, l_name, gender, dob, user_password_hash)

        return result
   

    

   
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.', 'warning')
    return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


def get_uploaded_images():
    lst = []
    rootdir = os.getcwd()
    # print rootdir
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
            lst.append(file)
    return lst


def format_date_joined(date_joined):
    return (date_joined.strftime("%Y-%m-%d"))


def format_time_joined(date_joined):
    return (date_joined.strftime("%X"))


###
# Routing for your application.
###
# Please create all new routes and view functions above this route.

# Here we define a function to collect form errors from Flask-WTF which we can later use
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
