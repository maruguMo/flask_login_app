from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username and password are correct (you would typically check against a database)
    if username == 'your_username' and password == 'your_password':
        return 'Login successful'
    else:
        return 'Login failed'

if __name__ == '__main__':
    app.run(debug=True)