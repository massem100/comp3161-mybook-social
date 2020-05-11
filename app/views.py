"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from datetime import date, time, datetime
from app import app, login_manager, mysql
from app.forms import UploadForm, LoginForm, SignupForm, PhotoForm, textForm, ImageForm, SearchFriends, SearchGroups, EditProfileForm, CommentForm
from app.models import User, Post
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask import Flask,render_template, request, jsonify, redirect, url_for, flash, session
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from operator import attrgetter, itemgetter

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
    comment_form = CommentForm()
    # cur = mysql.connection.cursor()
    # cur.execute(""" SELECT * """)
    posts = []
    if request.method == 'GET': 

        cur = mysql.connection.cursor()
        cur.execute(""" select post.post_id, post.userid,post_date, post_time, user.username, text_message from post JOIN text_post JOIN user ON post.post_id = text_post.post_id and post.userid = user.userid; """)
        text_posts = cur.fetchall()

        # print(text_posts)
        for i in text_posts: 
            post_id = i[0]
            userid = i[1]
            post_date = i[2]
            post_time = i[3]
            username = i[4]
            text_message = i[5]
            # print(post_id, userid, post_date, post_time, text_message)
            # users.append(User(userid,username, f_name, l_name, gender, dob, user_password))
            posts.append(Post(post_id, userid,username, post_date, post_time, text_message, " ", " "))

        cur = mysql.connection.cursor()
        cur.execute(""" select post.post_id, post.userid,post_date, post_time, user.username, image_filename,caption from post JOIN
                 image_post JOIN user ON post.post_id = image_post.post_id and post.userid = user.userid; """)
        image_posts = cur.fetchall()

        cur = mysql.connection.cursor()
        cur.execute(
            """ SELECT username FROM user WHERE userid = '{}' """.format(userid))
        username = cur.fetchall()

        for i in image_posts: 
            post_id = i[0]
            userid = i[1]
            post_date = i[2]
            post_time = i[3]
            username = i[4]
            image_filename = secure_filename(i[5])
            caption = i[6]

            # photo_filename = secure_filename(photo.filename)

            # print(post_id, userid, post_date, post_time, image_filename, caption)
            posts.append(Post(post_id, userid, username, post_date, post_time, " ", image_filename, caption))
    

        # I sorted the the array first by date and then
        #  sorted the result by time in order to achieve accurate results
        
        sorted_by_time_date= sorted(posts, key= lambda i: ( i.post_date, i.post_time ), reverse =True)

        #This was done just to test the arrangement of the posts- leaving it here in case I need to test again        
        # print(posts[0].post_id, posts[0].post_date, posts[0].post_time)
        # print(posts[1].post_id, posts[1].post_date, posts[1].post_time)
        # print(posts[2].post_id, posts[2].post_date, posts[2].post_time)
        
        
        

        return render_template('dashboard.html', text_form=text_form, image_form=image_form, posts=sorted_by_time_date)

    if request.method == 'POST':

        
        # Post(post_id, userid, post_date, post_time, text_message, image_filename, caption)



        return render_template('dashboard.html', text_form = text_form, image_form = image_form, posts = posts)
    else:   
        return render_template('dashboard.html', text_form=text_form, image_form=image_form)

        
    
        
@app.route('/dashboard/text_post', methods= ['POST', 'GET'])
@login_required
def text(): 
    text_form = textForm()
    image_form = ImageForm()
     
    if request.method == 'POST':
        if text_form.validate_on_submit() and text_form.text_post.data:

            worded_post = text_form.text_post.data
            # use statements below with implemented functions to format the time before storing on the database
            userid = current_user.id
            post_date = format_date_joined(datetime.now())
            post_time = format_time_joined(datetime.now())

            cur = mysql.connection.cursor()
            cur.execute(""" INSERT INTO post (post_id, userid, post_date, post_time) 
                        VALUES (NULL, "{}", "{}", "{}") """.format(userid, post_date, post_time))

            cur.execute(""" INSERT INTO text_post (text_id, post_id, text_message) 
                    VALUES (NULL, (SELECT max(post_id) FROM post WHERE userid = '{}'), "{}") """.format(userid, worded_post))

            mysql.connection.commit()
            cur.close()
            

            flash('Text Uploaded', 'success')
            return  redirect(url_for('dashboard'))
        return render_template('dashboard.html', text_form=text_form, image_form=image_form)
    else: 
        return render_template('dashboard.html', text_form=text_form, image_form=image_form)



@app.route('/dashboard/image_post', methods = ['POST', 'GET'])
@login_required
def image(): 
    image_form = ImageForm()
    
    text_form = textForm()
    # print('SIGH MAN CHRO')
    if request.method == 'POST': 
        # print('DEH YA')
        if image_form.validate_on_submit():
            # print('reaching here')
            photo = image_form.photo.data
            caption = image_form.image_desc.data

            photo_filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

            userid = current_user.id
            post_date = format_date_joined(datetime.now())
            post_time = format_time_joined(datetime.now())

            cur = mysql.connection.cursor()
            cur.execute(""" INSERT INTO post (post_id, userid, post_date, post_time) 
                        VALUES (NULL, "{}", "{}", "{}") """.format(userid, post_date, post_time))

            cur.execute(""" INSERT INTO image_post (image_id, post_id, image_filename, caption) 
                    VALUES (NULL, (SELECT max(post_id) FROM post WHERE userid = '{}'), "{}", "{}") """.format(userid, photo_filename, caption))

            mysql.connection.commit()
            cur.close()
            

            flash('Image Uploaded!', 'success')
            return redirect(url_for('dashboard'))
        return render_template('dashboard.html', text_form = text_form, image_form = image_form)
    else: 
        return render_template('dashboard.html', text_form = text_form, image_form = image_form)


@app.route('/dashboard/<post_id>/comments', methods =['POST'])
def comments(post_id):

    comment_form = CommentForm()
    text_form = textForm()
    image_form = ImageForm()

    if request.method == 'POST' and comment_form.comment.data: 
        # thi
        comment = comment_form.comment.data

        userid = current_user.id
        date_posted = format_date_joined(datetime.now())
        time_posted = format_time_joined(datetime.now())


        # cur = mysql.connection.cursor()
        # cur.execute(""" INSERT INTO comment  """)

        
        # comment_id, post_id, userid, comment_Content, time_posted, date_posted


        flash('Comment added successfully', 'success')
        return redirect(url_for('dashboard'))

    return render_template('dashboard.html', comment_form = comment_form,text_form = text_form, image_form = image_form)


@app.route('/userprofile', methods = ['POST','GET'])
@login_required
def userprofile():
    image_form = ImageForm()
    form = PhotoForm()
    text_form = textForm()
    edit_form= EditProfileForm()

    if request.method == 'POST':
        if text_form.validate_on_submit() and text_form.text_post.data:

            worded_post = text_form.text_post.data
            # use statements below with implemented functions to format the time before storing on the database
            userid = current_user.id
            post_date = format_date_joined(datetime.now())
            post_time = format_time_joined(datetime.now())

            cur = mysql.connection.cursor()
            cur.execute(""" INSERT INTO post (post_id, userid, post_date, post_time) 
                        VALUES (NULL, "{}", "{}", "{}") """.format(userid, post_date, post_time))

            cur.execute(""" INSERT INTO text_post (text_id, post_id, text_message) 
                    VALUES (NULL, (SELECT max(post_id) FROM post WHERE userid = '{}'), "{}") """.format(userid, worded_post))

            mysql.connection.commit()
            

            flash('Text Uploaded', 'success')
            return  redirect(url_for('userprofile'))
        return render_template('user_profile.html',form = form, text_form = text_form, image_form = image_form,edit_form=edit_form)

        if image_form.validate_on_submit():
            
            photo = image_form.photo.data
            caption = image_form.image_desc.data

            photo_filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

            userid = current_user.id
            post_date = format_date_joined(datetime.now())
            post_time = format_time_joined(datetime.now())

            cur = mysql.connection.cursor()
            cur.execute(""" INSERT INTO post (post_id, userid, post_date, post_time) 
                        VALUES (NULL, "{}", "{}", "{}") """.format(userid, post_date, post_time))

            cur.execute(""" INSERT INTO image_post (image_id, post_id, image_filename, caption) 
                    VALUES (NULL, (SELECT max(post_id) FROM post WHERE userid = '{}'), "{}", "{}") """.format(userid, photo_filename, caption))

            mysql.connection.commit()

            flash('Image Uploaded!', 'success')
            return redirect(url_for('userprofile'))
        return render_template('user_profile.html',form = form, text_form = text_form, image_form = image_form,edit_form=edit_form)
    
    #Working on this section. To upload photo to profile 
    # photo_id int(10) not null unique AUTO_INCREMENT,
    # userid int(10) not null,
    # photo_desc varchar(150),
    # photo_filename varchar(100) not null,
    # date_added date not null,
    if form.validate_on_submit():
        photo = form.photo.data

        photo_filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
        userid = current_user.id
        post_date = format_date_joined(datetime.now())
        post_time = format_time_joined(datetime.now())

        # cur = mysql.connection.cursor()
        ###
        #cur.execute(""" INSERT INTO post (post_id, userid, post_date, post_time) 
        #               VALUES (NULL, "{}", "{}", "{}") """.format(userid, post_date, post_time))

        #cur.execute(""" INSERT INTO photo (photo_id, userid, photo_desc, photo_filename,date_added) 
        #           VALUES (NULL, (SELECT max(photo_id) FROM post WHERE userid = '{}'), "{}", "{}","{}") """.format(userid,photo_desc, photo_filename, date_added))
        ###
        # mysql.connection.commit()

        flash('Image Uploaded!', 'success')
        return redirect(url_for('userprofile'))
    return render_template('user_profile.html',form = form, text_form = text_form, image_form = image_form,edit_form=edit_form)
    

    
    
    
@app.route('/groups', methods = ['GET', 'POST'])
def groups():
    form = PhotoForm()
    text_form = textForm()
    image_form = ImageForm()
    
   
    return render_template('groups.html',form = form, text_form = text_form, image_form = image_form)
    

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
@app.route('/a_groups')
def a_group():
    form = PhotoForm()
    text_form = textForm()
    image_form = ImageForm()
    return render_template('a_group.html', form=form, text_form=text_form, image_form=image_form)

# @app.route('/friends', methods = ['POST', 'GET'])
# def friends():
#     sf_form = SearchFriends()
#     if request.method =='POST': 

#         return 'x'
#     return render_template('friends.html', form = sf_form)

@app.route('/friends', methods = ['POST', 'GET'])
def friends():

    sf_form = SearchFriends()
    if request.method == 'POST':
        if sf_form.validate_on_submit(): 
            search_result = sf_form.friends_search.data

            if search_result == '':
                
                cur= mysql.connection.cursor()
                cur.execute(""" SELECT * from user """)
                all_users = cur.fetchall()
                # print(all_users)
                users = []
                for i in all_users: 
                   userid = i[0]
                   username = i[1]
                   f_name = i[2]
                   l_name = i[3]
                   gender = i[4]
                   dob = i[5]
                   user_password = i[6]

                   users.append(User(userid,username, f_name, l_name, gender, dob, user_password))
                #    print(users)
                return render_template('friends.html', form=sf_form, users=users)

                

        
        return render_template('friends.html', form = sf_form, users = users)
    else:
        
        return render_template('friends.html', form = sf_form)

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
        if user > (): 
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
            flash('No users in database', 'danger')
            return render_template('login.html', form = form)
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
