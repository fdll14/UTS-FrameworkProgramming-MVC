from flask import render_template, redirect, url_for, request, flash, session
from application import app
from application.models.database import mysql
import MySQLdb

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/checklogin', methods=['POST'])
def checklogin():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
 
        account = cursor.fetchone()

        if account:
            session['loggedin'] = True
            session["username"] = request.form.get("username")
            return redirect(url_for('dashboard'))
        else:

            return 'Incorrect username/password!'

@app.route('/logout')
def logout():
    session["username"] = None
    return redirect(url_for('login'))

