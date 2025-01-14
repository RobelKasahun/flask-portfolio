from flask import Flask, render_template, request, redirect
import os
import csv

app = Flask(__name__)


# home page route
@app.route("/")
@app.route("/index.html")
def index_page():
    return render_template("index.html")


@app.route("/<string:page>")
def page(page):
    return render_template(page)


def write_to_file(data):
    with open("database.txt", mode="a") as file:
        file.write(
            f"email = {data['email']}, subject = {data['subject']}, message = {data['message']}\n"
        )


def write_data_to_csv(data):
    with open("database.csv", mode="a", newline="") as csv_database:
        email, subject, message = data["email"], data["subject"], data["message"]
        csv_writer = csv.writer(
            csv_database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        try:
            data = data = request.form.to_dict()
            # write_to_file(data)
            write_data_to_csv(data)
            return redirect("thankyou.html")
        except Exception as exception:
            return f"Exception: {exception}"

    return f"Something went wrong. Please try again."


# @app.route("/works.html")
# def works():
#     return render_template("works.html")


# @app.route("/work.html")
# def work():
#     return render_template("work.html")


# @app.route("/about.html")
# def about():
#     return render_template("about.html")


# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")


# @app.route("/components.html")
# def components():
#     return render_template("components.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5500))
    print(port)
    app.run(debug=True, host="0.0.0.0", port=port)
