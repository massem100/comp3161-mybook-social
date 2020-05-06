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
    
