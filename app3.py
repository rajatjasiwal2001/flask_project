from flask import Flask,render_template,redirect,request
import pymysql

app=Flask(__name__)

def connection():
    conn=pymysql.connect(host="localhost",user="root",password="",database="mviet")
    return conn

@app.route("/")
def mviet():
    return render_template("mviet.html")


@app.route("/college_data",methods=["post"]) 
def college_data():
    conn=connection()
    id=request.form["id"]
    name=request.form["name"]
    contact=request.form["contact"]
    college=request.form["college"]
    print(id,name,contact,college)
    with conn.cursor() as cur:
        sql="INSERT INTO college(id,name,college,contact)VALUES(%s,%s,%s,%s)"
        cur.execute(sql,(id,name,college,contact))
        conn.commit()
    return redirect("/coll")

@app.route("/coll")
def college():
    conn=connection()
    with conn.cursor() as cur:
        sql="SELECT * FROM college"
        cur.execute(sql)
        conn.commit()
        data=cur.fetchall()
    return render_template("college.html",data=data)

@app.route("/delete/id=<int:id>")
def delete(id):
    conn=connection()
    with conn.cursor() as cur:
        sql="DELETE FROM college where id=%s"
        cur.execute(sql,(id,))
        conn.commit()
    return redirect("/coll")

@app.route("/update/id=<int:id>")
def update(id):
    conn=connection()
    with conn.cursor() as cur:
        sql="SELECT * FROM college WHERE id=%s"
        cur.excute(sql,(id,))
        data=cur.fetchone()
    return render_template("update_college.html", data=data)

@app.route("/college_data_update/id=<int:id>",methods=["post"])
def college_data_update(id):
    conn=connection()
    name=request.form["name"]
    contact=request.form["contact"]
    college=request.form["college"]
    with conn.cursor() as cur:
        sql="UPDATE college SET name=%s,contact=%s,college=%s where id=%s"
        cur.execute(sql,(name,contact,college,id))
        conn.commit()
    return redirect("/coll")

if __name__=="__main__":
    app.run(debug=True,port=5000,host="0.0.0.0"))

