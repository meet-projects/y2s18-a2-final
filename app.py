# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_account, check_user_and_pass, check_user_exists, get_posts, add_post

# Starting the flask app
app = Flask(__name__)

# App routing code here


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        acc_type = request.form['acc_type']
        try:
            add_account(first_name, last_name, username,
                        password, gender, acc_type)
            return redirect(url_for('signin'))
        except:
            return render_template("signup.html", error_message="Error: Username Taken")


@app.route('/log-in', methods=['GET', 'POST'])
def signin():
    print("login")
    print(request.form)
    if request.method == 'POST':
        if check_user_and_pass(request.form['username'], request.form['password']) == True:
            session['logged_in'] = True
            session['username'] = request.form['username']
            print("success")
            return redirect(url_for('user_page'))
        else:
            print('error:username or password are incorrect!!')
            return render_template('login.html', incorrect_user_or_pass='error:username or password are incorrect!! ')

    return render_template('login.html')


@app.route('/user', methods=['GET', 'POST'])
def user_page():
    if session.get('logged_in'):
        posts = get_posts()
        if request.method == 'GET':
            return render_template('user.html', posts=posts, username=session['username'])
        else:
            title = request.form['title']
            content = request.form['content']
            picture = request.form['picture']
            add_post(title, content, picture, session['username'])
            return redirect(url_for('user_page'))
    else:
        print("ns")
        return redirect(url_for('signin'))

@app.route('/signout')
def signout():
    session.clear()
    return redirect(url_for('home'))



# Running the Flask app
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True, port=8080)
