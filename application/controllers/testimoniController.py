from flask import render_template, redirect, url_for, request, flash, session
from application import app
from application.models.database import mysql

@app.route('/testimoni')
def testimoni():
    if not session.get("username"):
        return redirect("/login")
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM testimoni")
    data = cur.fetchall()
    cur.close()
    return render_template('testimoni.html',testimoni=data)

@app.route('/simpan',methods=["POST"])
def simpan():
    nama = request.form['nama']
    pesan = request.form['pesan']
    pekerjaan = request.form['pekerjaan']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO testimoni (nama,pesan,pekerjaan) VALUES (%s,%s,%s)",(nama,pesan,pekerjaan))
    mysql.connection.commit()
    return redirect(url_for('testimoni'))


@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    nama = request.form['nama']
    pesan = request.form['pesan']
    pekerjaan = request.form['pekerjaan']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE testimoni SET nama=%s,pesan=%s,pekerjaan=%s WHERE id=%s", (nama,pesan,pekerjaan,id_data,))
    mysql.connection.commit()
    return redirect(url_for('testimoni'))

@app.route('/hapus_testimoni/<string:id_data>', methods=["GET"])
def hapus_testimoni(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM testimoni WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('testimoni'))