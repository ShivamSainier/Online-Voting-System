from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,TextAreaField,RadioField,IntegerField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from flask_wtf.file import FileField



class admin_form(FlaskForm):
    Email=StringField('Admin Id',validators=[DataRequired(),Length(min=3,max=50)])
    Submit=SubmitField("Submit")

class candidatee(FlaskForm):
    Name=StringField('Candidate name',validators=[DataRequired(),Length(min=3,max=50)])
    Voter_id=StringField('Candidate Id',validators=[DataRequired()])
    address=TextAreaField('Address',validators=[DataRequired(),Length(min=10,max=50)])  
    phone=StringField('Phone No',validators=[DataRequired()])
    picture=FileField('Add Picture')
    submit=SubmitField('Submit')

class c_voter(FlaskForm):
    Voter_id=StringField('voter id',validators=[DataRequired()])
    phone=StringField('Phone No',validators=[DataRequired()])
    F_name=StringField("Father's name",validators=[DataRequired()])
    Age=StringField('Age',validators=[DataRequired()])
    address=TextAreaField('Address',validators=[DataRequired()])  
    pincode=StringField('Pincode',validators=[DataRequired()])
    submit=SubmitField('Submit')

class user(FlaskForm):
    login=StringField("Login id",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    Submit=SubmitField("Submit")
    


