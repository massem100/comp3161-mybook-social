from flask_login import UserMixin
from flask_login._compat import unicode
from app import app, login_manager, mysql, admin





class User(UserMixin):
            
    def __init__(self, id, username, f_name, l_name, gender, date_of_birth, password, photo):
        self.id= id
        self.f_name = f_name
        self.username = username
        self.l_name = l_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.password = password
        self.photo = photo
        

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User "{}">'.format(self.username)




class Post(UserMixin): 

    def __init__(self, post_id, userid,username, post_date, post_time, text_message, image_filename, caption,photo):
        self.post_id = post_id
        self.userid = userid
        self.username =username
        self.post_date =post_date
        self.post_time = post_time 
        self.text_message = text_message
        self.image_filename = image_filename
        self.caption = caption
        self.photo = photo
        
    def get_id(self):
        try:
            return unicode(self.post_id)  # python 2 support
        except NameError:
            return str(self.post_id)  # python 3 support

    def __repr__(self):
        return '<Post "{}">'.format(self.post_id)

        
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
            return unicode(self.comment_id)  # python 2 support
        except NameError:
            return str(self.comment_id)  # python 3 support

    def __repr__(self):
        return '<Comment "{}" "Post{}" "User {}" >'.format(self.comment_id, self.post_id, self.userid)


class Friend(UserMixin):

    def __init__(self, fid, friend_owner, friend_id, friend_type, friend_username, friend_f_name, friend_l_name, photo):
       self.fid = fid
       self.friend_owner = friend_owner
       self.friend_id = friend_id
       self.friend_type = friend_type
       self.friend_username = friend_username 
       self.friend_f_name= friend_f_name
       self.friend_l_name = friend_l_name
       self.photo = photo


    def get_id(self):
        try:
            return unicode(self.fid)  # python 2 support
        except NameError:
            return str(self.fid)  # python 3 support

    def __repr__(self):

        return '<Friend "{}" "{}" >'.format(self.friend_id, self.friend_username)

class Photo(UserMixin):

    def __init__(self, photo_id, userid, photo_desc, photo_filename, date_added):
        self.photo_id =photo_id
        self.userid = userid
        self.photo_desc = photo_desc
        self.photo_filename = photo_filename
        self.date_added = date_added


    def get_id(self):
        try:
            return unicode(self.photo_id)  # python 2 support
        except NameError:
            return str(self.photo_id)  # python 3 support

    def __repr__(self):
        return '<Photo "{}" "User {}" >'.format(self.photo_id,  self.userid)

# class Group(UserMixin):
class Profile(UserMixin):

    def __init__(self, profile_id, userid, profile_photo, nationality, user_bio):
        self.profile_id = profile_id
        self.userid = userid
        self.profile_photo = profile_photo
        self.nationality = nationality
        self.user_bio = user_bio

    def get_id(self):
        try:
            return unicode(self.profile_id)  # python 2 support
        except NameError:
            return str(self.profile_id)  # python 3 support

    def __repr__(self):
        return '<Profile "{}" "User {}" >'.format(self.profile_id,  self.userid)



   
