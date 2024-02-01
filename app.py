from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Add logic to handle registration data
        # For simplicity, you can print the received data
        username = request.form['username']
        password = request.form['password']
        # print(username+" "+password)
        # flash(f"Entered Username: {username}, Entered Password: {password}", 'success')
        print(f"Entered Username: {username}, Entered Password: {password}")
        
        return render_template('register.html', username=username, password=password)

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add logic to handle login data
        # For simplicity, you can print the received data
        print(request.form)
        return redirect(url_for('hello_world'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
