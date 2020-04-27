from flask_wtf import FlaskForm
from wtforms import  TextAreaField
from wtforms.validators import InputRequired, Email, DataRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('description', validators=[DataRequired('A description is required'), Length(max=150)])
    photo = FileField('photo', validators=[FileRequired('No photo was submitted.'), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
