from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField, StringField, PasswordField, SelectField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('description', validators=[DataRequired('A description is required'), Length(max=150)])
    photo = FileField('photo', validators=[FileRequired('No photo was submitted.'), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('A username is required')])
    password = PasswordField('Password', validators = [DataRequired('Please enter a password')])
    

class SignupForm(FlaskForm):
    f_name = StringField('First Name', validators=[DataRequired('First name field empty')])
    l_name = StringField('Last Name',validators=[DataRequired('Last name field empty')])
    username = StringField('Username', validators=[DataRequired('A username is required')])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired('Select a Gender')])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    confirmPassword = PasswordField('Repeat Password', validators=[DataRequired()])
    birthday = DateField('Date of Birth', format='%m/%d/%Y', validators=[DataRequired("Please enter your date of birth")])

class GroupForm(FlaskForm):
    group_name = StringField('Group Name', validators=[DataRequired('Group must have a name')])
    group_type = SelectField('Group Type', choices=[('Public', 'Public'), ('Private', 'Private')], validators=[DataRequired('Group type must be added')])
    desc = TextAreaField('Group Description', validators=[Length( max =150)])

class PhotoForm(FlaskForm):
    photo = FileField('photo', validators=[FileRequired('No photo was submitted.'), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    photo_desc = TextAreaField('Photo Description', validators=[])

class textForm(FlaskForm):
    text_post = TextAreaField('Text Post', validators=[DataRequired('Post content missing'), Length(max=140)])

class ImageForm(FlaskForm):
    photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg','png'], 'Images only!')])
    image_desc = TextAreaField('Caption', validators=[])

class SearchFriends(FlaskForm):
    friends_search = StringField('Friend Search', validators=[])

class SearchGroups(FlaskForm):
    group_search = StringField('Group Search', validators=[])


class EditProfileForm(FlaskForm):
    f_name = StringField('First Name', validators=[DataRequired('First name field empty')])
    l_name = StringField('Last Name',validators=[DataRequired('Last name field empty')])
    username = StringField('Username', validators=[DataRequired('A username is required')])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired('Select a Gender')])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    confirmPassword = PasswordField('Repeat Password', validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[])
    bio = TextAreaField('Bio', validators=[])
    birthday = DateField('Date of Birth', format='%m/%d/%Y', validators=[DataRequired("Please enter your date of birth")])
    email = EmailField('Email', validators=[])
    phone_num = StringField('Phone Number', validators=[])
    profile_pic = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','jpeg', 'png'], 'Images only!')])

class CommentForm(FlaskForm): 
    post_id = StringField('Post Number', validators=[DataRequired('Copy the post Number')])
    comment = TextAreaField('Comment', validators=[DataRequired(' Comment Field cannot be empty')])
