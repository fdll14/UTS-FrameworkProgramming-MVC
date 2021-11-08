from flask import render_template, redirect, url_for, request, flash, session
from application import app
from application.models.database import mysql

@app.route('/dashboard')
def dashboard():
    if not session.get("username"):
        return redirect("/login")
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kontak_pesan")
    data = cur.fetchall()
    cur.close()
    return render_template('dashboard.html',kontak_pesan=data)

@app.route('/kirim_pesan',methods=["POST"])
def kirim_pesan():
    nama = request.form['nama']
    email = request.form['email']
    pesan = request.form['pesan']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO kontak_pesan (nama,email,pesan) VALUES (%s,%s,%s)",(nama,email,pesan))
    mysql.connection.commit()
    return redirect(url_for('index'))

@app.route('/hapus_pesan/<string:id_data>', methods=["GET"])
def hapus_pesan(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM kontak_pesan WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('dashboard'))

