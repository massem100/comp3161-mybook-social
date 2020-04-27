from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField, StringField, PasswordField, SelectField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('description', validators=[DataRequired('A description is required'), Length(max=150)])
    photo = FileField('photo', validators=[FileRequired('No photo was submitted.'), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])


class LoginForm(FlaskForm):
    email = StringField('Email', [Email( message=('Not a valid email address.')), DataRequired('Email field is empty')])
    password = PasswordField('Password', validators = [DataRequired('Please enter a password'), Length(max =10)])
    

class SignupForm(FlaskForm):
    f_name = StringField('First Name', validators=[DataRequired(message ='First name field empty')])
    l_name = StringField('Last Name',validators=[DataRequired('Last name field empty')])
    email = EmailField('Email', validators=[Email(), InputRequired(), Length(max=50)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[InputRequired()])
    password = PasswordField('Password', validators=[DataRequired(message="Please enter a password.")])
    confirmPassword = PasswordField('Repeat Password', [EqualTo(password, message='Passwords must match.')])
    birthday = DateField('Date of Birth', validators=[DataRequired(message = "Please enter your date of birth")])
