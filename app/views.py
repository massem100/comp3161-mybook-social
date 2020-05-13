"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from datetime import date, time, datetime
from app import app, login_manager, mysql
from app.forms import UploadForm, LoginForm, SignupForm, PhotoForm, GroupForm, textForm, ImageForm, SearchFriends, SearchGroups, EditProfileForm, CommentForm
from app.models import User, Post, Comment, Friend, Photo
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask import Flask,render_template, request, jsonify, redirect, url_for, flash, session
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from operator import attrgetter, itemgetter

posts = []
@app.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    

    text_form = textForm()
    image_form = ImageForm()
    comment_form = CommentForm()
    
   
    if request.method == 'GET': 

        cur = mysql.connection.cursor()
        cur.execute(""" select post.post_id, post.userid,post_date, post_time,
         user.username, text_message from post JOIN text_post JOIN user ON post.post_id = text_post.post_id and post.userid = user.userid; """)
        text_posts = cur.fetchall()

        for i in text_posts: 
            post_id = i[0]
            userid = i[1]
            post_date = i[2]
            post_time = i[3]
            username = i[4]
            text_message = i[5]
            
            posts.append(Post(post_id, userid,username, post_date, post_time, text_message, " ", " "))

        cur = mysql.connection.cursor()
        cur.execute(""" select post.post_id, post.userid,post_date, post_time, user.username, image_filename,caption from post JOIN
                 image_post JOIN user ON post.post_id = image_post.post_id and post.userid = user.userid; """)
        image_posts = cur.fetchall()

        userid = current_user.id
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
    
            posts.append(Post(post_id, userid, username, post_date, post_time, " ", image_filename, caption))
        
        
        
        posts.sort(key= lambda i: ( i.post_date, i.post_time ), reverse =True)
        

        # ---------------------------------------------------------------------------------
              

        return render_template('dashboard.html', text_form=text_form, image_form=image_form, posts=posts, comment_form = comment_form)

    if request.method == 'POST':
        # # postNumber = request.args.get('post_id', post_id)
        # # print(postNumber)
        # # <-- the post instance you need
        # # post = Post.select().where(Post.post_id == postNumber).get()
        # comment = comment_form.comment.data
        # userid = current_user.id
        # date_posted = format_date_joined(datetime.now())
        # time_posted = format_time_joined(datetime.now())

        # # INSERT INTO comment values (1, 4, 1, "Great Post",'14:22', DATE '2015-12-17');
        # if comment_form.validate_on_submit():
        #     cur = mysql.connection.cursor()
        #     cur.execute(""" INSERT INTO comment (comment_id, post_id, userid, comment_Content, time_posted, date_posted)
        #             VALUES (NULL, (SELECT post_id FROM post WHERE post_id = "{}"), "{}", "{}", "{}", "{}") """.format(post_id, userid, comment, time_posted, date_posted))
        #     post = cur.fetchall()
        #     print(post)
        #     mysql.connection.commit()
            
        #     flash("Comment posted!", 'success')
        #     return redirect(url_for('dashboard'))

        return render_template('dashboard.html', text_form=text_form, image_form=image_form, comment_form=comment_form)
    else:   
        return render_template('dashboard.html', text_form=text_form, image_form=image_form, comment_form=comment_form)

        
    
        
@app.route('/dashboard/text_post', methods= ['POST'])
@login_required
def text(): 
    text_form = textForm()
    image_form = ImageForm()
    comment_form = CommentForm()
     
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
        flash('Form not submitted, check submission', 'info')
        return render_template('dashboard.html', text_form=text_form, image_form=image_form, comment_form=comment_form, posts=posts)
    else: 
        return render_template('dashboard.html', text_form=text_form, image_form=image_form, comment_form=comment_form, posts=posts)



@app.route('/dashboard/image_post', methods = ['POST'])
@login_required
def image(): 
    image_form = ImageForm()
    comment_form = CommentForm()
    text_form = textForm()
    
    if request.method == 'POST' and image_form.validate(): 
       
        if image_form.validate_on_submit():
            
            photo = image_form.photo.data
            photo_filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

            caption = image_form.image_desc.data
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

        flash(' File not uploaded, check if file uploaded is an image', 'info')
        return render_template('dashboard.html', text_form = text_form, image_form = image_form, comment_form = comment_form)
    else: 
        return render_template('dashboard.html', text_form = text_form, image_form = image_form, comment_form = comment_form)

@app.route('/dashboard/post/<post_id>', methods = ['POST'])
@login_required
def single_post(post_id):

    image_form = ImageForm()
    comment_form = CommentForm()
    text_form = textForm()
    # print(post_id)
    if request.method == 'POST': 
        
        # print(postNumber)
        # <-- the post instance you need
        # post = Post.select().where(Post.post_id == postNumber).get()
        comment = comment_form.comment.data
        post_id = int(comment_form.post_id.data)
        userid = current_user.id
        date_posted = format_date_joined(datetime.now())
        time_posted = format_time_joined(datetime.now())
       

        # INSERT INTO comment values (1, 4, 1, "Great Post",'14:22', DATE '2015-12-17');
        if comment_form.validate_on_submit():
            cur = mysql.connection.cursor()
            cur.execute(""" INSERT INTO comment (comment_id, post_id, userid, comment_Content, time_posted, date_posted)
                    VALUES (NULL, (SELECT post_id FROM post WHERE post_id = "{}"), "{}", "{}", "{}", "{}") """.format(post_id, userid, comment, time_posted, date_posted))
            post = cur.fetchall()
            # print(post)
            mysql.connection.commit()

            flash("Comment posted!", 'success')
            return redirect(url_for('dashboard'))

        flash('File not submitted, ensure fields are filled out', 'info')
        return render_template('dashboard.html', text_form=text_form, image_form=image_form, comment_form=comment_form)
    else:   
        return render_template('dashboard.html', text_form=text_form, image_form=image_form, comment_form=comment_form)

        
    

@app.route('/userprofile', methods = ['POST','GET'])
@login_required
def userprofile():
    image_form = ImageForm()
    form = PhotoForm()
    text_form = textForm()
    edit_form= EditProfileForm()

    profile_posts = []
    photos = []
    allphotos =[]
    if request.method == 'GET':

        username =current_user.username

        cur = mysql.connection.cursor()
        cur.execute(""" select * from (select post.post_id, post.userid,post_date, post_time,
         user.username, text_message from post JOIN text_post JOIN user ON post.post_id = text_post.post_id and post.userid = user.userid) as result
         WHERE username = '{}' """.format(username))
        text_posts = cur.fetchall()

       
        for i in text_posts:
            post_id = i[0]
            userid = i[1]
            post_date = i[2]
            post_time = i[3]
            username = i[4]
            text_message = i[5]
            
            profile_posts.append(Post(post_id, userid, username, post_date, post_time, text_message, " ", " "))

        cur = mysql.connection.cursor()
        cur.execute(""" select * from (select post.post_id, post.userid,post_date, post_time, user.username, image_filename,caption from post JOIN
                 image_post JOIN user ON post.post_id = image_post.post_id and post.userid = user.userid) as result WHERE username = '{}' """.format(username))
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

        
            profile_posts.append(Post(post_id, userid, username, post_date, post_time, " ", image_filename, caption))
        
       
        sorted_by_time_date = sorted(profile_posts, key=lambda i: (i.post_date, i.post_time), reverse=True)
        # ----------------------------------------------------------------------------------------
        
        # Section to select Profile Photos 
        userid = current_user.id
        cur = mysql.connection.cursor()
        cur.execute("""SELECT * FROM photo WHERE userid = '{}' ORDER BY RAND() limit 4""".format(userid))
        photo_results = cur.fetchall()
        # print(photo_results)

        for i in  photo_results: 
            photo_id = i[0]
            userid = i[1]
            photo_desc = i[2]
            photo_filename = i[3]
            date_added = i[4]

            photos.append(Photo(photo_id, userid, photo_desc, photo_filename, date_added))

        
        cur = mysql.connection.cursor()
        cur.execute(
            """SELECT * FROM photo WHERE userid = '{}'  """.format(userid))
        all_photo_results = cur.fetchall()
        # print(photo_results)

        for i in all_photo_results:
            photo_id = i[0]
            userid = i[1]
            photo_desc = i[2]
            photo_filename = i[3]
            date_added = i[4]

            allphotos.append(Photo(photo_id, userid, photo_desc, photo_filename, date_added))

        

        return render_template('user_profile.html', form=form, text_form=text_form, image_form=image_form, 
                                edit_form=edit_form, posts=sorted_by_time_date, photos = photos, allphotos = allphotos)

    # Handle Adding Photos to profile
    if request.method == 'POST':
        if form.validate_on_submit():

            photo = form.photo.data
            photo_desc = form.photo_desc.data

            photo_filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
            userid = current_user.id
            date_added = format_date_joined(datetime.now())
           
            cur = mysql.connection.cursor()            
            cur.execute(""" INSERT INTO photo (photo_id, userid, photo_desc, photo_filename,date_added) 
                      VALUES (NULL, "{}", "{}", "{}","{}") """.format(userid,photo_desc, photo_filename, date_added))
            
            mysql.connection.commit()

        flash('Photo Added!', 'success')
        return redirect(url_for('userprofile'))
    return render_template('user_profile.html',form = form, text_form = text_form, image_form = image_form, edit_form=edit_form)

@app.route('/userprofile/textpost', methods = ['POST'])
@login_required
def profile_textpost(): 
    text_form = textForm() 
    image_form = ImageForm() 
    edit_form = EditProfileForm()
    photo_form = PhotoForm()

    if request.method == 'POST':
        if text_form.validate_on_submit() and text_form.text_post.data:

            worded_post = text_form.text_post.data
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
            return redirect(url_for('userprofile'))
        return render_template('user_profile.html', photo_form = photo_form, text_form=text_form, image_form=image_form, edit_form=edit_form)

@app.route('/userprofile/image_post', methods = ['POST'])
@login_required
def profile_imagepost():
    image_form = ImageForm()
    comment_form = CommentForm()
    photo_form = PhotoForm()
    text_form = textForm()
    edit_form = EditProfileForm()


    
    if request.method == 'POST':
        
        if image_form.validate_on_submit():
           
            photo = image_form.photo.data
            photo_filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

            caption = image_form.image_desc.data
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
            return redirect(url_for('userprofile'))
        return render_template('user_profile.html', text_form=text_form, image_form=image_form, comment_form=comment_form, photo_form = photo_form)        
    
@app.route('/userprofile/editprofile', methods = ['POST'])
@login_required 
def editprofile(): 

    image_form = ImageForm()
    comment_form = CommentForm()
    photo_form = PhotoForm()
    text_form = textForm()
    edit_form = EditProfileForm

    if request.method == 'POST': 

        f_name = edit_form.f_name.data
        l_name = edit_form.l_name.data 
        username = edit_form.username.data 
        gender = edit_form.gender.data 
        password = edit_form.password.data 
        confirmPassword = edit_form.confirmPassword.data 
        nationality = edit_form.nationality.data 
        bio = edit_form.bio.data 
        email = edit_form.email.data
        phone_num = edit_form.phone_num.data 
        profile_pic = edit_form.profile_pic.data

        # cur = mysql.connection.cursor()
        # cur.execute(""" """)

        return redirect(url_for('userprofile'))
    return render_template('user_profile.html', image_form = image_form, comment_form = comment_form, photo_form = photo_form, text_form = text_form, edit_form = edit_form)

@app.route('/a_group/<group_id>', methods = ['GET', 'POST'])
@login_required
def a_group(group_id):
    
    
  
    return render_template('a_group.html')
    
    
@app.route('/groups', methods = ['GET', 'POST'])
@login_required
def groups():
    group_form = GroupForm()

    if request.method == 'POST': 

        admin_id = current_user.id
        group_name = group_form.group_name.data 
        group_type = group_form.group_type.data
        group_desc = group_form.desc.data
        date_created= format_date_joined(datetime.now())

        cur = mysql.connection.cursor()
        cur.execute(""" INSERT INTO friend_group (group_id, admin_id, groupname, date_created, grouptype, group_description) 
        VALUES (NULL, "{}", "{}", "{}","{}","{}")""".format(admin_id, group_name,date_created,group_type, group_desc))

        mysql.connection.commit()
       

        flash('Group created successfully', 'success')
        return redirect(url_for('searchgroup')) 
    return render_template('groups.html', group_form = group_form)
    

# Route to host form to search group
@app.route('/searchgroup', methods = ['GET'])
@login_required
def searchgroup(): 
    groupform = SearchGroups()
    # cur = mysql.connection.cursor()
    # cur.execute('SELECT * FROM customer WHERE customer_id ="CUS-00001" ')
    # customer = cur.fetchall()
    # cur.close()
    return render_template('search_group.html', form= groupform)

# Route to display the active group 

@app.route('/friends', methods = ['POST', 'GET'])

def friends():
    s_friends = []
    sf_form = SearchFriends()
    if request.method == 'POST':
        if sf_form.validate_on_submit(): 
            search_result = sf_form.friends_search.data

            if search_result == '':
                
                cur= mysql.connection.cursor()
                cur.execute(""" SELECT * from user """)
                all_users = cur.fetchall()
               
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
                
                return render_template('friends.html', form=sf_form, users=users, s_friends=s_friends)
                    

        return render_template('friends.html', form= sf_form, users = users,  s_friends = s_friends)

    if request.method == 'GET':
        # School Friends Below 
        # ---------------------------------------------
        
        logged_in_user = current_user.id
        # print(friend_owner)
        # SELECT * from friend WHERE friend_owner = 2 and friend_type = "school"
        cur = mysql.connection.cursor()
        cur.execute(""" SELECT fid, friend_id, friend_owner, friend_type  from friend WHERE friend_owner = '{}'  and friend_type ='school'"""
        .format(logged_in_user))
        school_friends = cur.fetchall()
        # print(school_friends)

        # fid. friend_in, friend_owner and friend_type
        cur.execute(""" SELECT fid, friend_owner, friend_id, friend_type, username as friend_username, f_name as friend_f_name,
                         l_name as friend_last_name, profile_photo FROM friend JOIN user JOIN userprofile ON friend.friend_id = user.userid
                         and userprofile.userid = friend.friend_id and friend_type = "school" ORDER BY friend_f_name asc;""")
        school_friend_info= cur.fetchall()
        
        for i in school_friend_info: 
            fid= i[0]
            friend_id = i[2]
            friend_type = i[3]
            friend_username = i[4]
            friend_f_name = i[5]
            friend_l_name = i[6]
            photo = i[7]
            
            s_friends.append(Friend(fid,logged_in_user, friend_id, friend_type, friend_username, friend_f_name, friend_l_name, photo))
        # ---------------------------------------------------------------

        # Relatives Category Selected Below 
        # ----------------------------------------------------------------
        # relatives =[]
        # cur = mysql.connection.cursor()
        # cur.execute(""" SELECT fid, friend_owner, friend_id, friend_type, username as friend_username, f_name as friend_f_name,
        #  l_name as friend_last_name, profile_photo FROM friend JOIN user JOIN userprofile ON friend.friend_id = user.userid 
        #  and userprofile.userid = friend.friend_id  and friend_type = "relatives" ORDER BY friend_f_name asc;""")
        # relatives= cur.fetchall()
        # print(school_friends)
        # for i in school_friends:
        #     fid = i[0]
        #     friend_owner = i[1]
        #     friend_id = i[2]
        #     friend_type = i[3]
        #     friend_username = i[4]
        #     friend_f_name = i[5]
        #     friend_l_name = i[6]
        #     photo = i[7]

        #     s_friends.append(Friend(fid, friend_owner, friend_id, friend_type,
                                    # friend_username, friend_f_name, friend_l_name, photo))

        # print(s_friends)
    return render_template('friends.html', form = sf_form, s_friends = s_friends)

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
        
        
        
            if user is not None and check_password_hash(user_password_hash, password):
                remember_me = False
                                
                login_user(User(id,username_,f_name, l_name, gender, dob, user_password_hash))
                
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
    
    if request.method == 'POST' and form.validate():
        if form.validate_on_submit():
            
            username = form.username.data
            first_name = form.f_name.data
            last_name = form.l_name.data 
            gender = form.gender.data
            date_of_birth = form.birthday.data
            user_password = generate_password_hash(form.password.data)
            confirm_password = check_password_hash(user_password, form.password.data)
           
            
            cur = mysql.connection.cursor()            
            cur.execute('''INSERT INTO user (userid,username, f_name, l_name, gender, date_of_birth, user_password) VALUES 
            (NULL, %s, %s, %s, %s, %s, %s)''',(username, first_name, last_name, gender, date_of_birth, user_password))

            mysql.connection.commit()
            

            flash('Congratulations, you are now a registered user!', 'success')
            return redirect(url_for('login'))
        return render_template('signup.html', form = form)
    else:
       
        # Remember to setup error display messages
        return render_template('signup.html', form = form)

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):

    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM user WHERE userid = "{}"'''.format(id))
    user = cur.fetchall()
    
    if user > ():
        id = user[0][0]
        username_ = user[0][1]
        f_name = user[0][2]
        l_name = user[0][3]
        gender = user[0][4]
        dob = user[0][5]
        user_password_hash = user[0][6]
       
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
