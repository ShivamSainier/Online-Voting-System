from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,TextAreaField,RadioField,IntegerField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from flask_wtf.file import FileField



class admin_form(FlaskForm):
    Email=StringField('E-mail',validators=[DataRequired()])
    Password=PasswordField("Password",validators=[DataRequired()])
    Submit=SubmitField("Submit")

class candidate(FlaskForm):
    Name=StringField('Candidate name',validators=[DataRequired()])
    Voter_id=StringField('Candidate Id',validators=[DataRequired()])
    address=TextAreaField('Address',validators=[DataRequired()])  
    cat = RadioField('cate:', choices = ['Male', 'Female'])
    phone=IntegerField('Phone No',validators=[DataRequired(),Length(min=10,max=12)])
    picture=FileField('Add Picture')

    submit=SubmitField('Submit')

class create_voter(FlaskForm):
    Voter_id=StringField('voter id',validators=[DataRequired()])
    phone=IntegerField('Phone No',validators=[DataRequired(),Length(min=10,max=12)])
    F_name=StringField("Father's name",validators=[DataRequired()])
    Age=IntegerField('Age',validators=[DataRequired(),Length(min=2,max=2)])
    Gender= RadioField('Gender:', choices = ['Male', 'Female'])
    address=TextAreaField('Address',validators=[DataRequired()])  
    pincode=IntegerField('Pincode',validators=[DataRequired(),Length(min=2,max=2)])
    submit=StringField('Submit')
    


