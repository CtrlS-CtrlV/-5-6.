from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("home.html", title="Головна", number=5)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")

        if not name:
            flash("Ім'я обов'язкове!")
        else:
            flash("Успішно!")

        return redirect("/form")

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
