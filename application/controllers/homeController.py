from flask import render_template, redirect, url_for, request, flash, session
from application import app
from application.models.database import mysql

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM testimoni")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html',testimoni=data)


@app.route('/profile')
def profile():
    return render_template('profile.html')