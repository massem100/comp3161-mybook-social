from flask_login import UserMixin
from flask_login._compat import unicode
from app import app, login_manager, mysql


class User(UserMixin):
            
    def __init__(self, id, username, f_name, l_name, gender, date_of_birth, password):
        self.id= id
        self.f_name = f_name
        self.username = username
        self.l_name = l_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.password = password
        

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User "{}">'.format(self.username)


class Post(UserMixin): 

    def __init__(self, post_id, userid,username, post_date, post_time, text_message, image_filename, caption):
        self.post_id = post_id
        self.userid = userid
        self.username =username
        self.post_date =post_date
        self.post_time = post_time 
        self.text_message = text_message
        self.image_filename = image_filename
        self.caption = caption
        
    def get_id(self):
        try:
            return unicode(self.post_id)  # python 2 support
        except NameError:
            return str(self.post_id)  # python 3 support

    def __repr__(self):
        return '<Post "{}">'.format(self.post_id)

        """
        comment_id int(11) not null unique AUTO_INCREMENT,
        post_id int(10) not null,
        userid int(10) not null,
        comment_Content varchar(250) not null,
        time_posted time not null,
        date_posted date not null,
        """
class Comment(UserMixin):

    def __init__(self, comment_id,post_id, userid, comment_Content, time_posted, date_posted):
        self.comment_id = comment_id
        self.post_id = post_id
        self.userid = userid
        self.comment_Content = comment_Content
        self.time_posted = time_posted
        self.date_posted = date_posted
    
    def get_id(self):
        try:
            return unicode(self. comment_id)  # python 2 support
        except NameError:
            return str(self.comment_id)  # python 3 support

    def __repr__(self):
        return '<Comment "{}" "Post{}" "User {}" >'.format(self.comment_id, self.post_id, self.userid)


