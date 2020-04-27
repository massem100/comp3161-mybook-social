from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField, StringField, PasswordField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, DataRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('description', validators=[DataRequired('A description is required'), Length(max=150)])
    photo = FileField('photo', validators=[FileRequired('No photo was submitted.'), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])


class LoginForm(FlaskForm):
    email = StringField('Email', [Email( message=('Not a valid email address.')), DataRequired('Email field is empty')])
    password = PasswordField('Password', validators = [DataRequired('Please enter a password'), Length(max =10)])
    # recaptcha = RecaptchaField()

class SignupForm(FlaskForm):
    f_name = StringField('First Name',validators=[DataRequired('First name field empty')])
    l_name = StringField('First Name',validators=[DataRequired('Last name field empty')])
    email = EmailField('email', validators=[Email(), InputRequired(), Length(max=50)])
    gender = SelectField('gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[InputRequired()])
    
