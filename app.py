from flask import Flask, render_template, redirect, request
import pymysql

app = Flask(__name__)

def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="student"
    )
    return conn
 
@app.route("/")
def home():
    return render_template("one.html")

@app.route("/student_data", methods=["POST"])
def student_data():
    conn = get_connection()
    id = request.form["id"]
    name = request.form["name"]
    address = request.form["address"]
    contact = request.form["contact"]
    print(id, name, address, contact)
    with conn.cursor() as cur:
        sql = "INSERT INTO list(id, name, address, contact) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (id, name, address, contact))
        conn.commit()
    return redirect("/show")

@app.route("/show")
def show():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM list")
        data = cur.fetchall()
    return render_template("user.html", data=data)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM list WHERE id=%s", (id,))
        conn.commit()
    return redirect("/show")

@app.route("/edit/<int:id>")
def edit(id):
    return redirect(f"/update/{id}")


@app.route("/update/<int:id>")
def update(id):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM list WHERE id=%s", (id,))
        data = cur.fetchone()
    return render_template("update.html", data=data)

@app.route("/list_data_update/<int:id>", methods=["POST"])
def list_data_update(id):
    conn = get_connection()
    name = request.form["name"]
    address = request.form["address"]
    contact = request.form["contact"]
    with conn.cursor() as cur:
        sql="UPDATE list SET name=%s, address=%s, contact=%s WHERE id=%s"
        cur.execute(sql, (name, address,contact, id))
        conn.commit()
    return redirect("/show")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
