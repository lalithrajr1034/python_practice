from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-me"

@app.get("/")
def home():
    # Redirect homepage to login page
    return redirect(url_for("login_page"))

@app.get("/login")
def login_page():
    return render_template("index.html")

@app.post("/login")
def login_submit():
    identifier = request.form.get("identifier","").strip()
    password = request.form.get("password","")
    # TODO: check user in DB
    if identifier == "test@example.com" and password == "secret123":
        return redirect(url_for("dashboard"))
    # If invalid:
    flash("Invalid credentials")
    return redirect(url_for("login_page"))

@app.get("/dashboard")
def dashboard():
    return "You are logged in!"

app.run(debug=True)
