from flask import Flask,render_template,redirect,url_for
from forms import *
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.secret_key="shivam@123"
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Votingsystem.db'

# Database models

class admin(db.Model):
    email=db.Column(db.String(120),nullable=False,primary_key=True)
    password=db.Column(db.String(120),nullable=False)
    def __repr__(self):
        return f"user('{self.email}',{self.password}')"

class candidate(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    candidate_name=db.Column(db.String(120),nullable=False)
    candidate_id=db.Column(db.String(120),nullable=False)
    address=db.Column(db.String(200),nullable=False)
    phone_no=db.Column(db.Integer,nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    image_file=db.Column(db.String(120),nullable=False,default='default.jpg')
    def __repr__(self):
        return f"user('{self.id}',{self.candidate_name}',{self.candidate_id},{self.address},{self.phone_no},{self.gender},{self.image_file})"

class voter(db.Model):
    id=db.Column(db.Integer,primary_key=True) 
    phone_no=db.Column(db.Integer,nullable=False)
    father_name=db.Column(db.String(120),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    gender=db.Column(db.String(120),nullable=False)
    address=db.Column(db.String(500),nullable=False)
    pincode=db.Column(db.Integer,nullable=False)
    image=db.Column(db.String(120),nullable=False,default='default.jpg')
    def __repr__(self):
        return f"user('{self.id}',{self.phone_no}',{self.father_name},{self.age},{self.gender},{self.address},{self.pincode},{self.image})"



# Routes 
@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/admin_login",methods=["GET","POST"])
def admin_login():
    form=admin_form()
    if form.validate_on_submit():
        data=form.Email.data
        email=admin.query.filter_by(email=data)
        if not email:
            return "<h1> Incorrect email or password</h1>"
        else:
            return redirect(url_for('main'))
    return render_template('Admin_login.html',form=form)

@app.route("/new_canidate")
def new_candidate():
    form=candidate()
    return render_template('new_candidate.html',form=form)

@app.route("/view_candidate")
def view_candidate():
    return render_template("view_candidate.html")

@app.route("/create_voter",methods=["GET","POST"])
def create_voter():
    voter=c_voter()
    return render_template("create_voter.html",voter=voter)

@app.route("/update_voter")
def update_voter():
    return render_template("update_voter.html")

@app.route("/voter_list")
def voter_list():
    return render_template("voter_list.html")

@app.route("/voting_result")
def voting_result():
    return render_template("voting_result.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route('/user_page',methods=['POST','GET'])
def user_page():
    use=user()
    return render_template('user_page.html',user=use)
if __name__=="__main__":
    app.run(debug=True)