from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def main():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/service.html")
def service():
    return render_template("service.html")


@app.route("/feature.html")
def feature():
    return render_template("feature.html")


@app.route("/project.html")
def project():
    return render_template("project.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/appointment.html")
def appointment():
    return render_template("appointment.html")


if __name__ == "__main__":
    app.run(debug=True)
