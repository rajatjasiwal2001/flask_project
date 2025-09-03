from flask import Flask,render_template,request,redirect
import pymysql

app=Flask(__name__)

def connection():
    conn=pymysql.connect(host="localhost",
                         user="root",
                         password="",
                         database="it",)
    return conn

@app.route("/")
def home():
    return render_template("it.html")

@app.route("/it_data",methods=["POST"])
def it_data():
    conn=connection()
    id=request.form["id"]
    name=request.form["name"]
    contact=request.form["contact"]
    email=request.form["email"]
    print(id,name,contact,email)
    with conn.cursor() as cur:
        sql="INSERT INTO data(id,name,contact,email)VALUES(%s,%s,%s,%s)"
        cur.execute(sql,(id,name,contact,email))
        conn.commit()

    return redirect("/register")

        