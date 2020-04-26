from flask import Flask
from flask_wtf.csrf import CSRFProtect 
from flask_mysqldb import MySQL
from flask_login import LoginManager

UPLOAD_FOLDER = './app/static/uploads'

USERNAME = 'admin'
PASSWORD = 'password123'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'SQLpass'
app.config['MYSQL_DB'] = 'bankdb'

mysql = MySQL(app)


# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

csrf = CSRFProtect(app)

app.config.from_object(__name__)
from app import views
