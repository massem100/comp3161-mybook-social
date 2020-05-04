from flask import Flask
from flask_wtf.csrf import CSRFProtect 
from flask_mysqldb import MySQL
from flask_login import LoginManager
from werkzeug.security import check_password_hash, generate_password_hash


# Folder to store images etc to be used in the app, only filename will be stored in the database.
UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda'

# password = 'pbkdf2:sha256:150000$uYDMjgNm$bd9a9c2ab56e93b8ed5ffe1d9a7e6cea2e849efc7ed7fb8f1f02c200360c71f8'
# SQL DECLARE Statements, password should be hashed before passing it.
# Statements below allow us to initicalize the MYSQL database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] ='SQLpass'
app.config['MYSQL_DB'] = 'mybook'

# Initializing the SQL connection to our app.
mysql = MySQL(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

csrf = CSRFProtect(app)

app.config.from_object(__name__)
from app import views
