from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,TextAreaField,RadioField
from wtforms.validators import DataRequired,Email,Length,EqualTo


class admin_form(FlaskForm):
    Email=StringField('E-mail',validators=[DataRequired()])
    Password=PasswordField("Password",validators=[DataRequired()])
    
    Submit=SubmitField("Submit")

class new_candidate(FlaskForm):
    Name=StringField('Candidate name',validators=[DataRequired()])
    Voter_id=StringField('Voter Id',validators=[DataRequired()])
    cat = RadioField('cate:', choices = ['Male', 'Female'])
    


