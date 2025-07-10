from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
STATUS_FILE = "status.json"

def read_status():
    with open(STATUS_FILE, "r") as f:
        return json.load(f)

def write_status(new_status):
    with open(STATUS_FILE, "w") as f:
        json.dump({"status": new_status}, f)

@app.route("/", methods=["GET", "POST"])
def index():
    status = read_status()["status"]
    if request.method == "POST":
        new_status = request.form.get("status")
        write_status(new_status)
        return redirect(url_for('index'))
    return render_template("index.html", status=status)

@app.route("/status")
def api_status():
    return read_status()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
