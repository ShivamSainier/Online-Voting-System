from flask import Flask,render_template,redirect,url_for
from forms import *

app=Flask(__name__)
app.secret_key="shivam"
@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/admin_login",methods=["GET","POST"])
def admin_login():
    admin=admin_form()
    if admin.validate_on_submit():
        return redirect(url_for('main'))
    return render_template('Admin_login.html',form=admin)

@app.route("/new_canidate")
def new_candidate():
    return render_template('new_candidate.html')

@app.route("/view_candidate")
def view_candidate():
    return render_template("view_candidate.html")

@app.route("/create_voter")
def create_voter():
    return render_template("create_voter.html")

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

if __name__=="__main__":
    app.run(debug=True)