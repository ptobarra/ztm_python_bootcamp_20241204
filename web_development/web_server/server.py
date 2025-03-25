from flask import Flask, render_template, send_from_directory, url_for, request, abort, redirect
import os
import csv

# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)
# print(__name__)


@app.route("/")
def my_home():
    # print(url_for("static", filename="favicon.ico"))  # jinja python templating engine - '/static/favicon.ico'
    return render_template("./index.html")
    # return "<p>Hello !!!!!!!!!!!</p>"


@app.route("/<string:page_name>")
def html_page(page_name):    
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        # print(data)  # Debugging: Check the data
        # write_to_file(data)
        write_to_csv(data)
        return redirect("/thankyou.html")
        # return "form submitted"
    else:
        return "Something went wrong. Try again!"
    # return 'form submitted hooorayyy!'

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/favicon.ico')
def favicon():
    if os.path.exists('static/assets/favicon.ico'):
        return send_from_directory('static', 'assets', 'favicon.ico')
    # if not, return a 404 error.
    else:
        abort(404)    

# If the file favicon.ico exists, put it in the static folder.

# @app.route("/index.html")
# def my_index():
#     return render_template("./index.html")


# @app.route("/works.html")
# def works():
#     return render_template("./works.html")


# @app.route("/about.html")
# def about():
#     return render_template("./about.html")
#     # return "<p>Hello !!!!!!!!!!!</p>"


# @app.route("/contact.html")
# def contact():
#     return render_template("./contact.html")


# @app.route("/components.html")
# def components():
#     return render_template("./components.html")


# @app.route("/thankyou.html")
# def thankyou():
#     return render_template("./thankyou.html")


# @app.route("/work.html")
# def work():
#     return render_template("./work.html")


# @app.route("/blog")
# def blog():
#     return "These are my thoughts on blogs!"


# @app.route("/favicon.ico")
# def favicon():
#     return send_from_directory("static", "favicon.ico")


# @app.route("/blog/2020/dogs")
# # @app.route("/blog")
# def blog2():
#     return "This is my dog!"


# On Windows (PowerShell)
# $env:FLASK_APP = 'C:\Users\TobarrP\ztm_python_bootcamp_20241204\web_development\web server\server.py'
# $env:FLASK_ENV = "development"
# python -m flask run
# python -m flask --app '.\web_development\web_server\server.py' run
# python -m flask --app '.\web_development\web_server\server.py' run --debug
# http://127.0.0.1:5000/

# On Windows (Command Prompt)
# set FLASK_APP=C:\Users\TobarrP\ztm_python_bootcamp_20241204\web_development\web_server\server.py
# set FLASK_ENV=development

# python -m flask run --debug
