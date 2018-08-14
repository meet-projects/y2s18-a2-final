# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_account,check_user_and_pass

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
        except:
            return render_template("signup.html", error_message = "Error: Username Taken")
        
@app.route('/log-in', methods = ['GET', 'POST'])
def signin():
    print("login")
    print(request.form)
    if request.method == 'POST':
        if check_user_and_pass(request.form['username'],request.form['password']) == True:
            session['logged_in'] = True
            session['username'] = request.form['username']
            print("success")
            return redirect(url_for('user_page'))
        else:
            print ('error:username or password are incorrect!!')
            return render_template('login.html',incorrect_user_or_pass ='error:username or password are incorrect!! ')

    return render_template('login.html')

@app.route('/user')
def user_page():
    print("chikens")
    if session.get('logged_in'):

        return render_template('user.html')
    else:
        print("ns")
        return redirect(url_for('signin'))


# Running the Flask app
if __name__ == "__main__":
    app.secret_key='super secret key'
    app.run(debug=True,port=8080)

