from flask import Flask, render_template, request
import pg8000

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        day = request.form["day"]
        return render_template("timetable.html", day=day, data=[], message="Loading timetable...")

    return render_template("index.html")

@app.route("/timetable", methods=["GET"])
def timetable():
    day = request.args.get('day')
    if not day:
        return "Day not provided", 400

    conn = pg8000.connect(
        user="hamidulla",
        password="hamidulla1234",
        host="",
        port=5432,
        database="hamidulla"
    )

    cur = conn.cursor()
    query = "SELECT * FROM Timetable WHERE day = %s;"
    cur.execute(query, (day,))
    rows = cur.fetchall()

    if rows:
        return render_template("timetable.html", day=day, data=rows, message="")
    else:
        return render_template("timetable.html", day=day, data=[], message="No data found for this day.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)