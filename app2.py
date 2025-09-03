from flask import Flask ,render_template,redirect,request
import pymysql

app=Flask(__name__)

def connection():
    conn=pymysql.connect(
        host="localhost",user="root",password="",database="company")
    
    return conn

@app.route("/")
def comapny():
    return render_template("company.html")

@app.route("/company_data",methods=["post"])
def company_data():
    conn=connection()
    id=request.form["id"]
    name=request.form["name"]
    contact=request.form["contact"]
    email=request.form["email"]
    print(id,name,contact,email)
    with conn.cursor() as cur:
        sql="INSERT INTO it(id,name,contact,email)VALUES(%s,%s,%s,%s)"
        cur.execute(sql,(id,name,contact,email))
        conn.commit()
    return redirect("/it")

@app.route("/it")
def it():
    conn=connection()
    with conn.cursor() as cur:
        sql="SELECT * FROM it"
        cur.execute(sql)
        conn.commit()
        data=cur.fetchall()
    return render_template("itr.html",data=data)


@app.route("/delete/id=<int:id>")
def delete(id):
    conn=connection()
    with conn.cursosr() as cur:
        sql="DELETE FROM it where id=%s"
        cur.exceute(sql,(id,))
        conn.commit()
    return redirect("/it")

@app.route("/update_it/id=<int:id>")
def update():
    conn=connection()
    with conn.cursor() as cur:
        sql="SELECT * FROM it where id=%s"
        cur.execute(sql,(id,))
        data=cur.fetchone()
    return render_template("update1.html", data=data)


@app.route("/update_data",methods=["post"])
def update():
    conn=connection()
    name=request.form["name"]
    contact=request.form["contact"]
    email=request.form["email"]
    print(name,contact,email)
    with conn.cursor() as cur:
        sql="UPDATE it set name=%s,conatct=%s,email=%s where id=%s"
        cur.execute(sql,(name,contact,email,id))
        conn.commit()
    return redirect("/it")


if __name__=="__main__":
    app.run(debug=True)