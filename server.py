from flask import Flask, render_template, request, url_for
import os
import json
import csv

app = Flask(__name__)


# home route
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/work")
def work():
    return render_template("work.html")


@app.route("/works")
def works():
    return render_template("works.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


def save_to_database_file(data):
    filename = "database.txt"
    with open(filename, mode="a") as file:
        file.write(str(data) + "\n")


def save_data_to_csv_file(data):
    filename = "database.csv"
    with open(filename, mode="a", newline="") as csv_file:
        email = data.get("email")
        subject = data.get("subject")
        message = data.get("message")

        fields = ["Email", "Subject", "Message"]

        writer = csv.DictWriter(csv_file, fields)

        # csv_writer = csv.writer(
        #     csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        # )
        writer.writeheader()
        writer.writerow({"Email": email, "Subject": subject, "Message": message})


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            save_data_to_csv_file(data)
            return render_template("thankyou.html")
        except Exception as exception:
            return {"Exception": exception}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5500))
    app.run(debug=True, host="0.0.0.0", port=port)
