from flask import Flask, render_template, request
from dotenv import load_dotenv
import os, smtplib


load_dotenv("email.env")

OWN_EMAIL = os.getenv("email")
OWN_PASSWORD = os.getenv("password")


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        data = request.form
        send_email(
            data["name"],
            data["email"],
            data["phone"],
            data["service"],
            data["date"],
            data["message"],
        )
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)


def send_email(name, email, phone, service, date, message):
    email_message = f"Subject: New Appointment Request\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nService: {service}\nDate: {date}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


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


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_message(
            data["name"],
            data["email"],
            data["subject"],
            data["message"],
        )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_message(name, email, subject, message):
    email_message = f"Subject: New Appointment Request\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route("/appointment.html", methods=["GET", "POST"])
def appointment():
    if request.method == "POST":
        data = request.form
        send_email(
            data["name"],
            data["email"],
            data["phone"],
            data["service"],
            data["date"],
            data["message"],
        )
        return render_template("appointment.html", msg_sent=True)
    return render_template("appointment.html", msg_sent=False)


def send_email(name, email, phone, service, date, message):
    email_message = f"Subject: New Appointment Request\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nService: {service}\nDate: {date}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
