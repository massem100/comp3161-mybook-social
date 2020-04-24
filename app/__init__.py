from flask import Flask
from flaskext.mysql import MySQL
from flask_wtf.csrf import CSRFProtect 


UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda'

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'SQLpass'
app.config['MYSQL_DATABASE_DB'] = 'bankdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = '3306'
db = mysql.init_app(app)

csrf = CSRFProtect(app)

app.config.from_object(__name__)
from app import views
