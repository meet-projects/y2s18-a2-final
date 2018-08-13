# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_account

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    else:
        username=request.form['username']
        password=request.form['password']
        birth=request.form['birth']
        gender=request.form['gender']
        acc_type=request.form['acc_type']
        try:
            add_account(username,password,birth,gender,acc_type)
            return render_template('home.html')
        except Exception as e:
            print(e)
            return render_template("signup.html", error_message = "Error: Username Taken")
        
@app.route('/log-in')
def signin():
    return render_template('login.html')


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=8080)

